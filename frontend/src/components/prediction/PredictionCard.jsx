import React from "react";
import {
  CheckCircle2, AlertTriangle, XCircle, Leaf,
  Stethoscope, FlaskConical, ShieldCheck, ChevronDown, ChevronUp,
  BarChart3,
} from "lucide-react";
import { getSeverityColor, getSeverityLabel } from "../../utils/helpers";
import ConfidenceBar from "./ConfidenceBar";

const SeverityIcon = ({ severity }) => {
  if (severity === "low")    return <CheckCircle2 className="w-5 h-5 text-green-500" />;
  if (severity === "medium") return <AlertTriangle className="w-5 h-5 text-yellow-500" />;
  return <XCircle className="w-5 h-5 text-red-500" />;
};

function BulletList({ items, colorClass = "bg-gray-400" }) {
  return (
    <ul className="space-y-2">
      {items.map((item, i) => (
        <li key={i} className="flex items-start gap-2 text-sm text-gray-700">
          <span className={`mt-1.5 w-1.5 h-1.5 rounded-full shrink-0 ${colorClass}`} />
          {item}
        </li>
      ))}
    </ul>
  );
}

function SectionView({ icon, title, children }) {
  return (
    <div className="border border-gray-200 rounded-lg overflow-hidden">
      <div className="flex items-center gap-2 px-4 py-3 bg-gray-50">
        {icon}
        <span className="font-semibold text-gray-800 text-sm">{title}</span>
      </div>
      <div className="px-4 py-4">{children}</div>
    </div>
  );
}

export default function PredictionCard({ result, sectionIndex = 0 }) {
  const {
    display_name, plant, disease, confidence_pct, severity,
    description, symptoms, causes, remedies, prevention, top5_predictions,
  } = result;

  const isHealthy = disease === "Healthy";

  // Define sections array
  const sections = [
    {
      icon: <Stethoscope className="w-4 h-4 text-blue-500" />,
      title: "About this condition",
      content: (
        <>
          <p className="text-sm text-gray-700 leading-relaxed">{description}</p>
          {!isHealthy && (
            <div className="mt-3 p-3 bg-gray-50 rounded-lg border border-gray-200">
              <p className="text-xs font-medium text-gray-600 mb-1">Root Cause</p>
              <p className="text-sm text-gray-700">{causes}</p>
            </div>
          )}
        </>
      ),
    },
    ...((!isHealthy) ? [{
      icon: <AlertTriangle className="w-4 h-4 text-yellow-500" />,
      title: "Symptoms to look for",
      content: <BulletList items={symptoms} colorClass="bg-yellow-400" />,
    }] : []),
    {
      icon: <FlaskConical className="w-4 h-4 text-green-600" />,
      title: isHealthy ? "Care tips" : "Treatment & Remedies",
      content: <BulletList items={remedies} colorClass="bg-green-500" />,
    },
    {
      icon: <ShieldCheck className="w-4 h-4 text-purple-500" />,
      title: "Prevention",
      content: <BulletList items={prevention} colorClass="bg-purple-400" />,
    },
    {
      icon: <BarChart3 className="w-4 h-4 text-indigo-500" />,
      title: "Top predictions",
      content: (
        <div className="space-y-3">
          {top5_predictions.map((pred, i) => (
            <ConfidenceBar
              key={pred.class_name}
              value={pred.confidence_pct}
              label={`${i + 1}. ${pred.class_name.replace(/_/g, " ").replace(/__/g, " – ")}`}
            />
          ))}
        </div>
      ),
    },
  ];

  const currentSection = sections[sectionIndex];

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className={`rounded-lg p-4 border-2 ${isHealthy ? "bg-green-50 border-green-200" : severity === "high" ? "bg-red-50 border-red-200" : "bg-yellow-50 border-yellow-200"}`}>
        <div className="flex items-start justify-between gap-3 mb-3">
          <div className="flex items-center gap-2">
            <SeverityIcon severity={severity} />
            <span className={`text-xs font-semibold px-2 py-1 rounded ${getSeverityColor(severity)}`}>
              {getSeverityLabel(severity)}
            </span>
          </div>
          <span className="text-2xl font-bold text-gray-900">{confidence_pct.toFixed(1)}%</span>
        </div>
        <h2 className="text-xl font-bold text-gray-900 mb-2">{display_name}</h2>
        <div className="flex items-center gap-3 text-sm text-gray-600">
          <span className="flex items-center gap-1"><Leaf className="w-3.5 h-3.5" />{plant}</span>
          <span>•</span>
          <span>{disease}</span>
        </div>
        <div className="mt-3">
          <ConfidenceBar value={confidence_pct} isMain />
        </div>
      </div>

      {/* Carousel Section */}
      <SectionView icon={currentSection.icon} title={currentSection.title}>
        {currentSection.content}
      </SectionView>
    </div>
  );
}
