import React from "react";
import { X } from "lucide-react";

export default function DocumentationModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b border-gray-200 flex items-center justify-between p-6">
          <h2 className="text-2xl font-black text-gray-900">Documentation</h2>
          <button
            onClick={onClose}
            className="p-1 hover:bg-gray-100 rounded-lg transition-colors"
            aria-label="Close documentation"
          >
            <X className="w-6 h-6 text-gray-600" />
          </button>
        </div>

        <div className="p-6 space-y-6">
          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Getting Started</h3>
            <p className="text-gray-600 leading-relaxed mb-4">
              CropGuard is an AI-powered crop disease detection system that helps farmers and agricultural professionals identify diseases in their crops quickly and accurately.
            </p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">How to Use</h3>
            <ol className="space-y-2 text-gray-600 list-decimal list-inside">
              <li>Upload an image of a leaf or crop affected by a potential disease</li>
              <li>The AI model will analyze the image and identify the disease</li>
              <li>Review the analysis results including confidence level</li>
              <li>Check treatment and prevention recommendations</li>
              <li>Apply remedies suggested by agricultural experts</li>
            </ol>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Supported Crops</h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-sm font-medium text-gray-900">Tomato</p>
                <p className="text-xs text-gray-500">Multiple disease variants</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-sm font-medium text-gray-900">Potato</p>
                <p className="text-xs text-gray-500">Blight detection</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-sm font-medium text-gray-900">Pepper</p>
                <p className="text-xs text-gray-500">Bell pepper diseases</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg">
                <p className="text-sm font-medium text-gray-900">Others</p>
                <p className="text-xs text-gray-500">More crops coming</p>
              </div>
            </div>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Image Requirements</h3>
            <ul className="space-y-2 text-gray-600">
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Clear, well-lit image of affected area</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Supported formats: JPG, PNG, WebP</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Minimum resolution: 256x256 pixels</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>File size limit: 5MB</span>
              </li>
            </ul>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Understanding Results</h3>
            <div className="bg-green-50 border border-green-200 p-4 rounded-lg space-y-3">
              <div>
                <p className="text-sm font-medium text-gray-900">Confidence Score</p>
                <p className="text-xs text-gray-600">Indicates how confident the model is about the prediction. Higher scores (80%+) are more reliable.</p>
              </div>
              <div>
                <p className="text-sm font-medium text-gray-900">Disease Information</p>
                <p className="text-xs text-gray-600">Learn about symptoms, causes, and why the disease was detected.</p>
              </div>
              <div>
                <p className="text-sm font-medium text-gray-900">Treatment & Prevention</p>
                <p className="text-xs text-gray-600">Get expert-recommended remedies and preventive measures.</p>
              </div>
            </div>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Tips for Best Results</h3>
            <ul className="space-y-2 text-gray-600">
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Ensure good lighting to avoid shadows</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Focus on the affected area of the leaf</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Include some healthy parts for comparison</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="w-1 h-1 bg-green-500 rounded-full mt-2 flex-shrink-0"></span>
                <span>Multiple images can help with accuracy</span>
              </li>
            </ul>
          </section>

          <section className="bg-gray-50 p-4 rounded-lg border border-gray-200">
            <h3 className="text-lg font-bold text-gray-900 mb-2">Note</h3>
            <p className="text-sm text-gray-600">
              CropGuard is an AI-assisted tool and should not replace professional agricultural diagnosis. Always consult local agricultural experts or specialists for critical decisions.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
