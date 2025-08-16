import { useEffect, useRef } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

export default function MapView({ parcels, onParcelClick }) {
  const mapRef = useRef(null);

  useEffect(() => {
    if (!mapRef.current) {
      mapRef.current = L.map("map").setView([37.8, -96], 4);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors"
      }).addTo(mapRef.current);
    }

    parcels.forEach(parcel => {
      if (parcel.polygon) {
        const poly = L.polygon(parcel.polygon.coordinates[0].map(([lng, lat]) => [lat, lng]), {
          color: parcel.status === "Qualified" ? "green" :
                 parcel.status === "Disqualified" ? "red" : "blue",
          weight: 2
        }).addTo(mapRef.current);

        poly.on("click", () => onParcelClick(parcel.id));
      }
    });
  }, [parcels, onParcelClick]);

  return <div id="map" className="h-[500px] w-full" />;
}
