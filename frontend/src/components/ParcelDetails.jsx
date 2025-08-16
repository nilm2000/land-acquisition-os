import { useEffect, useState } from "react";
import { fetchParcelDetails, updateParcelStatus } from "../api";

export default function ParcelDetails({ parcelId, onClose }) {
  const [parcel, setParcel] = useState(null);

  useEffect(() => {
    if (parcelId) {
      fetchParcelDetails(parcelId).then(setParcel).catch(console.error);
    }
  }, [parcelId]);

  if (!parcel) return <div className="p-4">Loading...</div>;

  const handleStatusChange = (status) => {
    const reason = status === "Disqualified" ? prompt("Enter reason:") : "";
    updateParcelStatus(parcel.id, status, reason)
      .then(() => alert("Status updated"))
      .catch(console.error);
  };

  return (
    <div className="p-4 border-l bg-white max-w-md">
      <button className="mb-3 text-sm text-blue-500" onClick={onClose}>← Back</button>
      <h2 className="text-xl font-bold">{parcel.address}</h2>
      <p>{parcel.county} County</p>
      <p>Acreage: {parcel.acreage}</p>
      <p>Price: ${parcel.price.toLocaleString()}</p>
      <p>Zoning: {parcel.zoning}</p>
      <div className="mt-4 flex gap-2">
        <button onClick={() => handleStatusChange("Qualified")} className="bg-green-500 text-white px-3 py-1 rounded">Qualify</button>
        <button onClick={() => handleStatusChange("Disqualified")} className="bg-red-500 text-white px-3 py-1 rounded">Disqualify</button>
        <button onClick={() => handleStatusChange("Snoozed")} className="bg-yellow-500 text-white px-3 py-1 rounded">Snooze</button>
      </div>
    </div>
  );
}
