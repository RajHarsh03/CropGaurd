export const getSeverityColor = (severity) => {
  switch (severity) {
    case "low":    return "text-green-700 bg-green-100 border-green-200";
    case "medium": return "text-yellow-700 bg-yellow-100 border-yellow-200";
    case "high":   return "text-red-700 bg-red-100 border-red-200";
    default:       return "text-gray-700 bg-gray-100 border-gray-200";
  }
};

export const getSeverityLabel = (severity) => {
  switch (severity) {
    case "low":    return "Low Risk";
    case "medium": return "Medium Risk";
    case "high":   return "High Risk";
    default:       return "Unknown";
  }
};

export const getConfidenceColor = (pct) => {
  if (pct >= 80) return "bg-green-500";
  if (pct >= 50) return "bg-yellow-500";
  return "bg-red-500";
};

export const formatConfidence = (pct) => `${pct.toFixed(1)}%`;
