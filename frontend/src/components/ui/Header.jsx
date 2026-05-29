import React, { useState } from "react";
import { Leaf, Github } from "lucide-react";
import DocumentationModal from "./DocumentationModal";
import AboutModal from "./AboutModal";

export default function Header() {
  const [docOpen, setDocOpen] = useState(false);
  const [aboutOpen, setAboutOpen] = useState(false);

  return (
    <>
      <header className="bg-white border-b border-gray-100 sticky top-0 z-10 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-11 h-11 bg-gradient-to-br from-green-600 to-green-700 rounded-lg flex items-center justify-center shadow-md">
              <Leaf className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-black text-gray-900 tracking-tight">CropGuard</h1>
              <p className="text-xs text-gray-500 font-medium">Smart Disease Detection</p>
            </div>
          </div>
          <nav className="hidden sm:flex items-center gap-8 text-sm">
            <button
              onClick={() => setDocOpen(true)}
              className="text-gray-600 font-medium hover:text-green-600 hover:underline underline-offset-4 transition-colors cursor-pointer bg-transparent border-0"
            >
              Documentation
            </button>
            <button
              onClick={() => setAboutOpen(true)}
              className="text-gray-600 font-medium hover:text-green-600 hover:underline underline-offset-4 transition-colors cursor-pointer bg-transparent border-0"
            >
              About
            </button>
            <a href="#" className="inline-flex items-center gap-2 text-gray-600 font-medium hover:text-green-600 transition-colors">
              <Github className="w-4 h-4" />
              GitHub
            </a>
          </nav>
        </div>
      </header>

      <DocumentationModal isOpen={docOpen} onClose={() => setDocOpen(false)} />
      <AboutModal isOpen={aboutOpen} onClose={() => setAboutOpen(false)} />
    </>
  );
}
