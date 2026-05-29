import { useState, useCallback } from "react";
import { predictDisease } from "../services/api";

const ALLOWED_TYPES = ["image/jpeg", "image/jpg", "image/png", "image/webp"];
const MAX_SIZE_MB = 10;

export function usePrediction() {
  const [state, setState] = useState({
    status: "idle",
    result: null,
    error: null,
    preview: null,
    file: null,
  });

  const validateFile = (file) => {
    if (!ALLOWED_TYPES.includes(file.type)) {
      throw new Error("Please upload a JPEG, PNG, or WebP image.");
    }
    if (file.size > MAX_SIZE_MB * 1024 * 1024) {
      throw new Error(`File too large. Maximum size is ${MAX_SIZE_MB} MB.`);
    }
  };

  const selectFile = useCallback((file) => {
    try {
      validateFile(file);
      const preview = URL.createObjectURL(file);
      setState({ status: "selected", result: null, error: null, preview, file });
    } catch (err) {
      setState((prev) => ({ ...prev, error: err.message, status: "error" }));
    }
  }, []);

  const predict = useCallback(async () => {
    setState((prev) => ({ ...prev, status: "loading", error: null, result: null }));
    try {
      const result = await predictDisease(state.file);
      setState((prev) => ({ ...prev, status: "success", result }));
    } catch (err) {
      setState((prev) => ({ ...prev, status: "error", error: err.message }));
    }
  }, [state.file]);

  const reset = useCallback(() => {
    if (state.preview) URL.revokeObjectURL(state.preview);
    setState({ status: "idle", result: null, error: null, preview: null, file: null });
  }, [state.preview]);

  return { ...state, selectFile, predict, reset };
}
