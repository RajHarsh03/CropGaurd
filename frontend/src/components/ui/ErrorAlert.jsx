import React from "react";
import { AlertCircle, X } from "lucide-react";

export default function ErrorAlert({ message, onDismiss }) {
  return (
    <div className="bg-red-50 border border-red-200 rounded-lg p-4 flex items-start gap-3">
      <AlertCircle className="w-5 h-5 text-red-600 mt-0.5 shrink-0" />
      <div className="flex-1">
        <p className="text-red-900 font-semibold text-sm">Error</p>
        <p className="text-red-800 text-sm mt-0.5">{message}</p>
      </div>
      {onDismiss && (
        <button
          onClick={onDismiss}
          className="text-red-400 hover:text-red-600 transition-colors p-0.5"
          aria-label="Dismiss error"
        >
          <X className="w-4 h-4" />
        </button>
      )}
    </div>
  );
}
