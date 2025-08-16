// src/api.js
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

// Helper: get token from localStorage
function getAuthHeaders() {
  const token = localStorage.getItem("token");
  return token ? { Authorization: `Bearer ${token}` } : {};
}

// ---------- AUTH ----------
export async function registerUser(data) {
  const res = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function loginUser(data) {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error(await res.text());
  const json = await res.json();
  localStorage.setItem("token", json.access_token);
  return json;
}

export async function getCurrentUser() {
  const res = await fetch(`${API_URL}/auth/me`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// ---------- USERS ----------
export async function listUsers() {
  const res = await fetch(`${API_URL}/users`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// ---------- PARCELS ----------
export async function createParcel(data) {
  const res = await fetch(`${API_URL}/parcels`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// This matches ParcelDetails.jsx
export async function fetchParcelDetails(id) {
  const res = await fetch(`${API_URL}/parcels/${id}`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// Update parcel status (Qualify, Disqualify, Snooze)
export async function updateParcelStatus(id, status, reason = "") {
  const res = await fetch(`${API_URL}/parcels/${id}/status`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
    body: JSON.stringify({ status, reason }),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function getRegridParcel(lat, lon) {
  const res = await fetch(`${API_URL}/parcels/regrid/${lat}/${lon}`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// Get all parcels
export async function fetchParcels() {
  const res = await fetch(`${API_URL}/parcels`, {
    headers: { ...getAuthHeaders() },
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
