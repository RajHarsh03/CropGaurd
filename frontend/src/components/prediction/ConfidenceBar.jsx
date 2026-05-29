import React from "react";
import { getConfidenceColor, formatConfidence } from "../../utils/helpers";

export default function ConfidenceBar({ value, label, isMain = false }) {
  const color = getConfidenceColor(value);

  return (
    <div className={`${isMain ? "mb-2" : ""}`}>
      {label && (
        <div className="flex justify-between items-center mb-1.5">
          <span className={`text-sm truncate pr-2 ${isMain ? "font-semibold text-gray-900" : "font-medium text-gray-700"}`}>
            {label}
          </span>
          <span className={`text-sm font-bold shrink-0 ${isMain ? "text-gray-900 text-base" : "text-gray-700"}`}>
            {formatConfidence(value)}
          </span>
        </div>
      )}
      <div className="w-full bg-gray-200 rounded-full h-2 overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-500 ${color}`}
          style={{ width: `${Math.min(value, 100)}%` }}
        />
      </div>
    </div>
  );
}
