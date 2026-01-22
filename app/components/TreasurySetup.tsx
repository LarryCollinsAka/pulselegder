"use client";
import { useState } from "react";

export default function TreasurySetup() {
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function setupTreasury() {
    setLoading(true);
    try {
      const res = await fetch("/api/treasury/setup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-4 border rounded-md">
      <button
        onClick={setupTreasury}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700"
      >
        {loading ? "Creating..." : "Initialize Treasury Wallets"}
      </button>

      {result && (
        <div className="mt-4">
          <h3 className="font-semibold">Treasury Setup Result:</h3>
          <pre className="bg-gray-100 p-2 rounded-md text-sm">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
