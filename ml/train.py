import os
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, callbacks
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# ── Config ────────────────────────────────────────────────────────────────────
IMG_SIZE    = 224
BATCH_SIZE  = 32
EPOCHS_HEAD = 10
EPOCHS_FINE = 15
LEARNING_RATE_HEAD = 1e-3
LEARNING_RATE_FINE = 1e-5

DATASET_DIR = Path("../Dataset/PlantVillage")
OUTPUT_DIR   = Path("outputs")
MODEL_PATH   = Path("../backend/trained_model/crop_disease_model.keras")
CLASSES_PATH = Path("../backend/trained_model/class_names.json")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

# ── Class discovery ────────────────────────────────────────────────────────────
class_names = sorted([
    d.name for d in DATASET_DIR.iterdir()
    if d.is_dir() and not d.name.startswith(".")
])
num_classes = len(class_names)
print(f"Found {num_classes} classes: {class_names}")

with open(CLASSES_PATH, "w") as f:
    json.dump(class_names, f, indent=2)
print(f"Class names saved to {CLASSES_PATH}")

# ── Data generators ────────────────────────────────────────────────────────────
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    zoom_range=0.25,
    horizontal_flip=True,
    vertical_flip=False,
    brightness_range=[0.8, 1.2],
    fill_mode="nearest",
    validation_split=0.2,
)

val_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,
)

train_gen = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True,
    seed=42,
)

val_gen = val_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False,
    seed=42,
)

# Verify class ordering matches our saved list
gen_classes = [k for k, v in sorted(train_gen.class_indices.items(), key=lambda x: x[1])]
assert gen_classes == class_names, "Class order mismatch!"

print(f"Training samples  : {train_gen.samples}")
print(f"Validation samples: {val_gen.samples}")

# ── Model: Phase 1 – train head only ──────────────────────────────────────────
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights="imagenet",
)
base_model.trainable = False

inputs = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
x = base_model(inputs, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.BatchNormalization()(x)
x = layers.Dense(512, activation="relu")(x)
x = layers.Dropout(0.4)(x)
x = layers.Dense(256, activation="relu")(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(num_classes, activation="softmax")(x)

model = models.Model(inputs, outputs)
model.summary()

model.compile(
    optimizer=optimizers.Adam(learning_rate=LEARNING_RATE_HEAD),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

cb_head = [
    callbacks.EarlyStopping(monitor="val_accuracy", patience=5, restore_best_weights=True),
    callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=3, min_lr=1e-7),
    callbacks.ModelCheckpoint(
        str(OUTPUT_DIR / "best_head.keras"),
        monitor="val_accuracy",
        save_best_only=True,
    ),
]

print("\n── Phase 1: Training head layers ──")
history_head = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS_HEAD,
    callbacks=cb_head,
)

# ── Model: Phase 2 – fine-tune top layers ─────────────────────────────────────
base_model.trainable = True
fine_tune_at = 100
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

model.compile(
    optimizer=optimizers.Adam(learning_rate=LEARNING_RATE_FINE),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

cb_fine = [
    callbacks.EarlyStopping(monitor="val_accuracy", patience=7, restore_best_weights=True),
    callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.3, patience=4, min_lr=1e-8),
    callbacks.ModelCheckpoint(
        str(OUTPUT_DIR / "best_fine.keras"),
        monitor="val_accuracy",
        save_best_only=True,
    ),
]

print("\n── Phase 2: Fine-tuning ──")
history_fine = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS_FINE,
    callbacks=cb_fine,
)

# ── Save final model ───────────────────────────────────────────────────────────
model.save(str(MODEL_PATH))
print(f"\nModel saved to {MODEL_PATH}")

# ── Plot training curves ───────────────────────────────────────────────────────
def merge_histories(h1, h2):
    merged = {}
    for key in h1.history:
        merged[key] = h1.history[key] + h2.history[key]
    return merged

history = merge_histories(history_head, history_fine)
epochs_range = range(1, len(history["accuracy"]) + 1)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(epochs_range, history["accuracy"], label="Train Accuracy", color="#2563eb")
axes[0].plot(epochs_range, history["val_accuracy"], label="Val Accuracy", color="#16a34a")
axes[0].axvline(EPOCHS_HEAD, color="gray", linestyle="--", alpha=0.6, label="Fine-tune start")
axes[0].set_title("Model Accuracy", fontsize=14, fontweight="bold")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Accuracy")
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].plot(epochs_range, history["loss"], label="Train Loss", color="#dc2626")
axes[1].plot(epochs_range, history["val_loss"], label="Val Loss", color="#ea580c")
axes[1].axvline(EPOCHS_HEAD, color="gray", linestyle="--", alpha=0.6, label="Fine-tune start")
axes[1].set_title("Model Loss", fontsize=14, fontweight="bold")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Loss")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle("Crop Disease Detection – Training History", fontsize=16, fontweight="bold")
plt.tight_layout()
plot_path = OUTPUT_DIR / "training_history.png"
plt.savefig(str(plot_path), dpi=150, bbox_inches="tight")
plt.close()
print(f"Training plot saved to {plot_path}")

# ── Evaluate ───────────────────────────────────────────────────────────────────
val_gen.reset()
loss, acc = model.evaluate(val_gen, verbose=1)
print(f"\nFinal validation accuracy: {acc:.4f} ({acc*100:.2f}%)")
print(f"Final validation loss    : {loss:.4f}")

results = {
    "val_accuracy": float(acc),
    "val_loss": float(loss),
    "num_classes": num_classes,
    "class_names": class_names,
    "img_size": IMG_SIZE,
}
with open(OUTPUT_DIR / "training_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("Training results saved.")
