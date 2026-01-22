"use client";
import { useState } from "react";

export default function TransferTokens() {
  const [sourceWalletId, setSourceWalletId] = useState("");
  const [destinationAddress, setDestinationAddress] = useState("");
  const [amount, setAmount] = useState(1000000); // 1 USDC in base units
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function handleTransfer() {
    setLoading(true);
    try {
      const res = await fetch("/api/treasury/transfer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          source_wallet_id: sourceWalletId,
          destination_address: destinationAddress,
          amount: amount,
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error("Transfer failed:", err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-4 border rounded-md mt-4">
      <h3 className="font-semibold mb-2">Transfer Tokens</h3>

      <div className="space-y-2">
        <input
          type="text"
          placeholder="Source Wallet ID"
          value={sourceWalletId}
          onChange={(e) => setSourceWalletId(e.target.value)}
          className="w-full px-3 py-2 border rounded-md"
        />
        <input
          type="text"
          placeholder="Destination Address"
          value={destinationAddress}
          onChange={(e) => setDestinationAddress(e.target.value)}
          className="w-full px-3 py-2 border rounded-md"
        />
        <input
          type="number"
          placeholder="Amount (base units)"
          value={amount}
          onChange={(e) => setAmount(Number(e.target.value))}
          className="w-full px-3 py-2 border rounded-md"
        />
        <button
          onClick={handleTransfer}
          disabled={loading}
          className="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
        >
          {loading ? "Transferring..." : "Transfer USDC"}
        </button>
      </div>

      {result && (
        <div className="mt-4">
          <h4 className="font-semibold">Transfer Result:</h4>
          <pre className="bg-gray-100 p-2 rounded-md text-sm">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
