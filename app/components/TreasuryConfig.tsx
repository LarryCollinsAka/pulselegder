"use client";
import useSWR from "swr";

const fetcher = (url: string) => fetch(url).then((res) => res.json());

export default function TreasuryConfig() {
  const { data, error } = useSWR("/api/treasury/config", fetcher);

  if (error) return <div>Error loading treasury config</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <div className="p-4 border rounded-md mt-4">
      <h3 className="font-semibold">Treasury Config:</h3>
      <pre className="bg-gray-100 p-2 rounded-md text-sm">
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}
