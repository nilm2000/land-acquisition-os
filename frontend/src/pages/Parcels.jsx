import { useEffect, useState } from "react";
import { fetchParcels, createParcel } from "../api";
import { Link } from "react-router-dom";

export default function Parcels() {
  const [parcels, setParcels] = useState([]);
  const [newParcel, setNewParcel] = useState({ address: "", parcel_id: "", owner_name: "" });

  useEffect(() => {
    loadParcels();
  }, []);

  const loadParcels = async () => {
    try {
      const res = await fetchParcels();
      setParcels(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleAdd = async (e) => {
    e.preventDefault();
    try {
      await createParcel(newParcel);
      setNewParcel({ address: "", parcel_id: "", owner_name: "" });
      loadParcels();
    } catch (err) {
      alert("Failed to add parcel");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Parcels</h2>

      <form onSubmit={handleAdd}>
        <input
          placeholder="Parcel ID"
          value={newParcel.parcel_id}
          onChange={(e) => setNewParcel({ ...newParcel, parcel_id: e.target.value })}
          required
        />
        <input
          placeholder="Address"
          value={newParcel.address}
          onChange={(e) => setNewParcel({ ...newParcel, address: e.target.value })}
          required
        />
        <input
          placeholder="Owner Name"
          value={newParcel.owner_name}
          onChange={(e) => setNewParcel({ ...newParcel, owner_name: e.target.value })}
        />
        <button type="submit">Add Parcel</button>
      </form>

      <ul>
        {parcels.map((p) => (
          <li key={p.id}>
            <Link to={`/parcels/${p.id}`}>
              {p.parcel_id} - {p.address} ({p.owner_name})
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
