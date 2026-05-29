import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: `${BASE_URL}/api/v1`,
  timeout: 60000,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      const { status, data } = error.response;
      const message =
        data?.detail ||
        (status === 413 ? "Image file is too large (max 10 MB)." :
         status === 415 ? "Unsupported image format. Use JPEG, PNG, or WebP." :
         status === 503 ? "AI model is not ready. Please try again shortly." :
         "An unexpected server error occurred.");
      return Promise.reject(new Error(message));
    }
    if (error.request) {
      return Promise.reject(
        new Error("Cannot reach the server. Make sure the backend is running on port 8000.")
      );
    }
    return Promise.reject(error);
  }
);

export const predictDisease = async (imageFile) => {
  const formData = new FormData();
  formData.append("file", imageFile);
  const response = await api.post("/predict", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};

export const checkHealth = async () => {
  const response = await api.get("/health");
  return response.data;
};

export default api;
