import { useEffect, useState } from "react";
import MapView from "./components/MapView";
import ParcelList from "./components/ParcelList";
import ParcelDetails from "./components/ParcelDetails";
import FilterPanel from "./components/FilterPanel";
import { fetchParcels } from "./api";

export default function App() {
  const [parcels, setParcels] = useState([]);
  const [selectedParcel, setSelectedParcel] = useState(null);

  useEffect(() => {
    fetchParcels(1) // Project ID hardcoded for now
      .then(setParcels)
      .catch(console.error);
  }, []);

  const handleFilterApply = (filters) => {
    console.log("Filters applied:", filters);
    // TODO: Call backend with filters
  };

  return (
    <div className="flex">
      <div className="flex-1 p-4">
        <FilterPanel onApply={handleFilterApply} />
        <MapView parcels={parcels} onParcelClick={setSelectedParcel} />
        <ParcelList parcels={parcels} onSelect={setSelectedParcel} />
      </div>
      {selectedParcel && (
        <ParcelDetails parcelId={selectedParcel} onClose={() => setSelectedParcel(null)} />
      )}
    </div>
  );
}
