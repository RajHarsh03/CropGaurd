import React from "react";
import { X, Leaf, Code2, Target } from "lucide-react";

export default function AboutModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b border-gray-200 flex items-center justify-between p-6">
          <h2 className="text-2xl font-black text-gray-900">About CropGuard</h2>
          <button
            onClick={onClose}
            className="p-1 hover:bg-gray-100 rounded-lg transition-colors"
            aria-label="Close about"
          >
            <X className="w-6 h-6 text-gray-600" />
          </button>
        </div>

        <div className="p-6 space-y-6">
          <section>
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 bg-gradient-to-br from-green-600 to-green-700 rounded-lg flex items-center justify-center">
                <Leaf className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-lg font-bold text-gray-900">CropGuard</h3>
            </div>
            <p className="text-gray-600 leading-relaxed">
              CropGuard is an intelligent agricultural disease detection system powered by deep learning. We combine modern AI technology with agricultural expertise to help farmers detect crop diseases early and take corrective action.
            </p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3 flex items-center gap-2">
              <Target className="w-5 h-5 text-green-600" />
              Our Mission
            </h3>
            <p className="text-gray-600 leading-relaxed">
              To empower farmers and agricultural professionals with accessible, accurate AI-driven disease detection tools that improve crop yields, reduce losses, and promote sustainable farming practices worldwide.
            </p>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
              <Code2 className="w-5 h-5 text-green-600" />
              Technology Stack
            </h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-gray-50 p-3 rounded-lg border border-gray-200">
                <p className="text-sm font-bold text-gray-900 mb-1">Frontend</p>
                <p className="text-xs text-gray-600">React, Vite, Tailwind CSS</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg border border-gray-200">
                <p className="text-sm font-bold text-gray-900 mb-1">Backend</p>
                <p className="text-xs text-gray-600">Python, FastAPI, TensorFlow</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg border border-gray-200">
                <p className="text-sm font-bold text-gray-900 mb-1">ML Model</p>
                <p className="text-xs text-gray-600">Keras CNN Architecture</p>
              </div>
              <div className="bg-gray-50 p-3 rounded-lg border border-gray-200">
                <p className="text-sm font-bold text-gray-900 mb-1">Deployment</p>
                <p className="text-xs text-gray-600">Vercel, Render, Cloud</p>
              </div>
            </div>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Key Features</h3>
            <ul className="space-y-2">
              <li className="flex items-start gap-3">
                <span className="w-2 h-2 bg-green-600 rounded-full mt-2 flex-shrink-0"></span>
                <div>
                  <p className="text-sm font-medium text-gray-900">Real-time Detection</p>
                  <p className="text-xs text-gray-600">Instant analysis of crop disease images</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="w-2 h-2 bg-green-600 rounded-full mt-2 flex-shrink-0"></span>
                <div>
                  <p className="text-sm font-medium text-gray-900">High Accuracy</p>
                  <p className="text-xs text-gray-600">Deep learning models trained on diverse datasets</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="w-2 h-2 bg-green-600 rounded-full mt-2 flex-shrink-0"></span>
                <div>
                  <p className="text-sm font-medium text-gray-900">Expert Recommendations</p>
                  <p className="text-xs text-gray-600">Treatment and prevention advice from agricultural experts</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="w-2 h-2 bg-green-600 rounded-full mt-2 flex-shrink-0"></span>
                <div>
                  <p className="text-sm font-medium text-gray-900">Easy to Use</p>
                  <p className="text-xs text-gray-600">Intuitive interface requiring no technical knowledge</p>
                </div>
              </li>
              <li className="flex items-start gap-3">
                <span className="w-2 h-2 bg-green-600 rounded-full mt-2 flex-shrink-0"></span>
                <div>
                  <p className="text-sm font-medium text-gray-900">Multi-Crop Support</p>
                  <p className="text-xs text-gray-600">Detects diseases across various crop types</p>
                </div>
              </li>
            </ul>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Data & Training</h3>
            <p className="text-gray-600 text-sm leading-relaxed mb-3">
              Our AI models are trained on the PlantVillage dataset, which contains thousands of high-quality images of healthy and diseased crops. This diverse training data ensures robust performance across different environmental conditions and crop varieties.
            </p>
            <div className="bg-blue-50 border border-blue-200 p-3 rounded-lg">
              <p className="text-xs font-medium text-blue-900 mb-1">Privacy</p>
              <p className="text-xs text-blue-700">We do not store uploaded images. All processing happens securely and is deleted immediately after analysis.</p>
            </div>
          </section>

          <section>
            <h3 className="text-lg font-bold text-gray-900 mb-3">Development</h3>
            <p className="text-gray-600 text-sm leading-relaxed">
              CropGuard is built with open-source technologies and is continuously improved based on user feedback and advances in agricultural AI research. Our team combines expertise in machine learning, agriculture, and software engineering.
            </p>
          </section>

          <section className="bg-green-50 p-4 rounded-lg border border-green-200">
            <h3 className="text-sm font-bold text-green-900 mb-2">Want to contribute?</h3>
            <p className="text-xs text-green-700 mb-3">
              Check out our GitHub repository to contribute code, report issues, or suggest improvements.
            </p>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block px-3 py-1.5 bg-green-600 text-white text-xs font-medium rounded-lg hover:bg-green-700 transition-colors"
            >
              View on GitHub
            </a>
          </section>

          <section className="bg-gray-50 p-4 rounded-lg border border-gray-200 text-center">
            <p className="text-xs text-gray-600">
              <span className="font-medium text-gray-900">Made with</span> botanical care for farmers worldwide 🌱
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}
