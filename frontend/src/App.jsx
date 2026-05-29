import React, { useEffect, useState } from "react";
import { Scan, RotateCcw, WifiOff, ChevronLeft, ChevronRight } from "lucide-react";
import Header from "./components/ui/Header";
import UploadZone from "./components/upload/UploadZone";
import PredictionCard from "./components/prediction/PredictionCard";
import LoadingSpinner from "./components/ui/LoadingSpinner";
import ErrorAlert from "./components/ui/ErrorAlert";
import { usePrediction } from "./hooks/usePrediction";
import { checkHealth } from "./services/api";

function ApiStatusBanner({ online }) {
  if (online === null) return null;
  if (online) return null;
  return (
    <div className="bg-yellow-50 border border-yellow-200 rounded-lg px-5 py-4 flex items-start gap-3 text-sm text-yellow-900 shadow-sm">
      <WifiOff className="w-5 h-5 shrink-0 mt-0.5 text-yellow-600" />
      <div>
        <p className="font-semibold mb-1">Backend server is offline</p>
        <p className="text-yellow-700">Start the backend with: <code className="font-mono bg-yellow-100 px-2 py-1 rounded">uvicorn app.main:app</code></p>
      </div>
    </div>
  );
}

export default function App() {
  const { status, result, error, preview, file, selectFile, predict, reset } = usePrediction();
  const [apiOnline, setApiOnline] = useState(null);
  const [sectionIndex, setSectionIndex] = useState(0);

  useEffect(() => {
    checkHealth()
      .then(() => setApiOnline(true))
      .catch(() => setApiOnline(false));
  }, []);

  const isLoading  = status === "loading";
  const isSuccess  = status === "success";
  const isSelected = status === "selected";

  const handlePrevSection = () => {
    setSectionIndex((prev) => (prev === 0 ? 4 : prev - 1));
  };

  const handleNextSection = () => {
    setSectionIndex((prev) => (prev === 4 ? 0 : prev + 1));
  };

  const handleReset = () => {
    setSectionIndex(0);
    reset();
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />

      <main className="max-w-6xl mx-auto px-4 py-12">
        {/* Page Title Section */}
        <div className="mb-12">
          <div className="mb-5">
            <span className="inline-block text-xs font-bold text-green-700 bg-green-50 px-3 py-1.5 rounded-full mb-4 border border-green-200 uppercase tracking-wider">Agriculture Intelligence</span>
          </div>
          <h2 className="text-5xl font-black text-gray-900 mb-4 leading-tight">Crop Disease Detection</h2>
          <p className="text-lg text-gray-700 max-w-2xl font-light">Identify crop diseases instantly with AI-powered analysis. Get actionable treatment recommendations and prevention strategies.</p>
        </div>

        <ApiStatusBanner online={apiOnline} />

        <div className="grid gap-8 mt-8 lg:grid-cols-2">
          <div className="space-y-4">
            <div className="card p-6">
              <h3 className="text-sm font-semibold text-gray-700 mb-4 uppercase tracking-wide">
                Select Image
              </h3>
              <UploadZone
                preview={preview}
                file={file}
                onFileSelect={selectFile}
                onClear={handleReset}
                disabled={isLoading}
              />
            </div>

            {error && (
              <ErrorAlert
                message={error}
                onDismiss={handleReset}
              />
            )}

            {(isSelected || status === "error") && (
              <button
                onClick={predict}
                disabled={isLoading || !file}
                className="btn-primary w-full flex items-center justify-center gap-2"
              >
                <Scan className="w-4 h-4" />
                Analyze
              </button>
            )}
          </div>

          {isLoading && (
            <div className="card p-6">
              <LoadingSpinner />
            </div>
          )}

          {isSuccess && result && (
            <div className="card p-6 flex flex-col h-full">
              <div className="flex items-center justify-between gap-4 mb-4 shrink-0">
                <h3 className="text-sm font-semibold text-gray-700 uppercase tracking-wide">
                  Analysis Results
                </h3>
                <div className="flex items-center gap-2">
                  <button
                    onClick={handlePrevSection}
                    className="btn-secondary flex items-center justify-center w-8 h-8 p-0"
                  >
                    <ChevronLeft className="w-4 h-4" />
                  </button>
                  <span className="text-xs text-gray-600 font-medium whitespace-nowrap min-w-8 text-center">
                    {sectionIndex + 1}/5
                  </span>
                  <button
                    onClick={handleNextSection}
                    className="btn-secondary flex items-center justify-center w-8 h-8 p-0"
                  >
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>
              </div>
              <div className="overflow-y-auto flex-1">
                <PredictionCard result={result} sectionIndex={sectionIndex} />
              </div>
              <button onClick={handleReset} className="btn-secondary w-full flex items-center justify-center gap-2 mt-4 shrink-0">
                <RotateCcw className="w-4 h-4" />
                Start Over
              </button>
            </div>
          )}

          {!isLoading && !isSuccess && (
            <div className="card p-8 flex flex-col items-center justify-center text-center">
              <div className="text-gray-400 mb-4">
                <svg className="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-gray-700 font-semibold mb-2">No results yet</h3>
              <p className="text-gray-500 text-sm">Upload and analyze an image to see results</p>
            </div>
          )}
        </div>

        {/* Footer */}
        <footer className="mt-20 pt-16 border-t border-gray-100 bg-gradient-to-b from-white to-gray-50">
          <div className="max-w-6xl mx-auto px-4 py-12">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
              <div>
                <h3 className="text-base font-bold text-gray-900 mb-4 tracking-tight">About</h3>
                <p className="text-sm text-gray-600 leading-relaxed">CropGuard is an AI-powered disease detection system designed to help farmers identify crop diseases early and take preventive action.</p>
              </div>
              <div>
                <h3 className="text-base font-bold text-gray-900 mb-4 tracking-tight">Features</h3>
                <ul className="text-sm text-gray-600 space-y-2.5">
                  <li className="flex items-center gap-2">
                    <span className="w-1 h-1 bg-green-500 rounded-full"></span>
                    Real-time disease detection
                  </li>
                  <li className="flex items-center gap-2">
                    <span className="w-1 h-1 bg-green-500 rounded-full"></span>
                    Treatment recommendations
                  </li>
                  <li className="flex items-center gap-2">
                    <span className="w-1 h-1 bg-green-500 rounded-full"></span>
                    Confidence scoring
                  </li>
                  <li className="flex items-center gap-2">
                    <span className="w-1 h-1 bg-green-500 rounded-full"></span>
                    Multi-crop support
                  </li>
                </ul>
              </div>
              <div>
                <h3 className="text-base font-bold text-gray-900 mb-4 tracking-tight">Support</h3>
                <ul className="text-sm space-y-2.5">
                  <li><a href="#" className="text-gray-600 hover:text-green-600 hover:font-medium transition-all duration-200">Documentation</a></li>
                  <li><a href="#" className="text-gray-600 hover:text-green-600 hover:font-medium transition-all duration-200">GitHub</a></li>
                  <li><a href="#" className="text-gray-600 hover:text-green-600 hover:font-medium transition-all duration-200">Report Issue</a></li>
                </ul>
              </div>
            </div>
            <div className="border-t border-gray-200 pt-8 text-center">
              <p className="text-sm text-gray-600 mb-2">For educational and research purposes only. Always consult with agronomists for critical decisions.</p>
              <p className="text-xs text-gray-400">&copy; 2024 CropGuard. All rights reserved.</p>
            </div>
          </div>
        </footer>
      </main>
    </div>
  );
}
