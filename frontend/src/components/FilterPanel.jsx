export default function FilterPanel({ onApply }) {
  const handleApply = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    onApply(Object.fromEntries(formData.entries()));
  };

  return (
    <form onSubmit={handleApply} className="bg-white p-3 border rounded mb-4">
      <label className="block mb-2">
        Min Acreage:
        <input type="number" name="minAcreage" className="border ml-2 p-1 w-20" />
      </label>
      <label className="block mb-2">
        Max Price:
        <input type="number" name="maxPrice" className="border ml-2 p-1 w-24" />
      </label>
      <button type="submit" className="bg-blue-500 text-white px-3 py-1 rounded">Apply</button>
    </form>
  );
}
