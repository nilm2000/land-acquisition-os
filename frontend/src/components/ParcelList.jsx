export default function ParcelList({ parcels, onSelect }) {
  return (
    <div className="overflow-y-auto max-h-[500px] border p-2 bg-white">
      {parcels.map(parcel => (
        <div
          key={parcel.id}
          className="p-3 border-b cursor-pointer hover:bg-gray-100"
          onClick={() => onSelect(parcel.id)}
        >
          <h3 className="font-semibold">{parcel.address}</h3>
          <p>{parcel.acreage} acres · ${parcel.price.toLocaleString()}</p>
          <p className="text-sm text-gray-500">{parcel.status}</p>
        </div>
      ))}
    </div>
  );
}
