import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // backend URL
});

// Attach token if available
API.interceptors.request.use((req) => {
  const token = localStorage.getItem("token");
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});

// Auth
export const login = (email, password) =>
  API.post("/auth/login", new URLSearchParams({ username: email, password }));

// Users
export const register = (user) => API.post("/users/", user);

// Parcels
export const fetchParcels = () => API.get("/parcels/");
export const createParcel = (parcel) => API.post("/parcels/", parcel);

export default API;
