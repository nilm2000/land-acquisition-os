import { useParams } from "react-router-dom";

export default function ParcelDetails() {
  const { id } = useParams();

  return (
    <div style={{ padding: "20px" }}>
      <h2>Parcel Details</h2>
      <p>Parcel ID: {id}</p>
      <p>🗺️ (You can integrate a map with Regrid or Leaflet here later)</p>
    </div>
  );
}
