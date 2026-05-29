import React, { useRef, useState } from "react";
import { Upload, X } from "lucide-react";

export default function UploadZone({ preview, file, onFileSelect, onClear, disabled }) {
  const inputRef = useRef(null);
  const [isDragging, setIsDragging] = useState(false);

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    const dropped = e.dataTransfer.files[0];
    if (dropped) onFileSelect(dropped);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => setIsDragging(false);

  const handleChange = (e) => {
    const selected = e.target.files[0];
    if (selected) onFileSelect(selected);
    e.target.value = "";
  };

  if (preview) {
    return (
      <div className="relative rounded-lg overflow-hidden border-2 border-gray-300 bg-white">
        <img
          src={preview}
          alt="Selected leaf"
          className="w-full h-64 sm:h-80 object-cover"
        />
        {!disabled && (
          <button
            onClick={onClear}
            className="absolute top-2 right-2 bg-red-500 text-white p-1.5 rounded hover:bg-red-600 transition-colors"
            aria-label="Remove image"
          >
            <X className="w-4 h-4" />
          </button>
        )}
        <div className="p-3 border-t border-gray-200">
          <p className="text-gray-800 text-sm font-medium truncate">{file?.name}</p>
          <p className="text-gray-500 text-xs mt-1">
            {file ? (file.size / 1024).toFixed(1) + " KB" : ""}
          </p>
        </div>
      </div>
    );
  }

  return (
    <div
      onClick={() => !disabled && inputRef.current?.click()}
      onDrop={handleDrop}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      className={`
        relative border-2 border-dashed rounded h-64 sm:h-72 flex flex-col items-center justify-center cursor-pointer select-none
        ${isDragging
          ? "border-green-600 bg-green-50"
          : "border-gray-300 bg-white"}
        ${disabled ? "opacity-50 cursor-not-allowed" : ""}
      `}
    >
      <input
        ref={inputRef}
        type="file"
        accept="image/jpeg,image/jpg,image/png,image/webp"
        className="hidden"
        onChange={handleChange}
        disabled={disabled}
      />
      <Upload className="w-8 h-8 text-gray-600 mb-2" />
      <p className="text-gray-800 text-sm font-medium">
        {isDragging ? "Drop here" : "Click to upload or drag"}
      </p>
      <p className="text-gray-500 text-xs mt-1">PNG, JPG, WebP (max 10 MB)</p>
    </div>
  );
}

