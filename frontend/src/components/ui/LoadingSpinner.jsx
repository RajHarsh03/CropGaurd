import React from "react";

export default function LoadingSpinner({ message = "Analyzing image..." }) {
  return (
    <div className="flex flex-col items-center justify-center py-16 gap-4">
      <div className="relative w-12 h-12">
        <div className="absolute inset-0 rounded-full border-4 border-gray-200" />
        <div className="absolute inset-0 rounded-full border-4 border-transparent border-t-green-600 animate-spin" />
      </div>
      <div className="text-center">
        <p className="text-gray-900 font-semibold">{message}</p>
        <p className="text-gray-500 text-sm mt-1">Please wait...</p>
      </div>
    </div>
  );
}
