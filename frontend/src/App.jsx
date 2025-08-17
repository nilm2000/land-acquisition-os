import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Parcels from "./pages/Parcels";
import ParcelDetails from "./pages/ParcelDetails";
import Navbar from "./components/Navbar";

function App() {
  const token = localStorage.getItem("token");

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/parcels"
          element={token ? <Parcels /> : <Navigate to="/login" />}
        />
        <Route
          path="/parcels/:id"
          element={token ? <ParcelDetails /> : <Navigate to="/login" />}
        />
        <Route path="*" element={<Navigate to="/parcels" />} />
      </Routes>
    </Router>
  );
}

export default App;
