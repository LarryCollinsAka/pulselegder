'use client';

import { useState } from 'react';

interface SetupResponse {
  treasury_address: string;
  status: string;
}

export default function SetupTreasury() {
  const [loading, setLoading] = useState<boolean>(false);
  const [walletAddress, setWalletAddress] = useState<string | null>(null);

  const handleSetup = async () => {
    setLoading(true);
    try {
      // Calls your FastAPI /setup endpoint on Vercel
      const response = await fetch('/api/setup', { method: 'POST' });
      const data: SetupResponse = await response.json();
      
      setWalletAddress(data.treasury_address);
    } catch (error) {
      console.error("Failed to establish trade signal:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="p-8 bg-[#0a0f1e] text-slate-100 rounded-2xl border border-slate-800 shadow-2xl">
      <div className="flex flex-col gap-6">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight">Pulse Treasury</h2>
          <p className="text-slate-400 text-sm mt-1">
            Foundation for Cross-Border African Trade.
          </p>
        </div>

        {!walletAddress ? (
          <button 
            onClick={handleSetup}
            disabled={loading}
            className="w-full md:w-max bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 px-8 py-3 rounded-lg font-medium transition-all shadow-lg shadow-blue-900/20"
          >
            {loading ? "Establishing Signal..." : "Initialize Trade Ledger"}
          </button>
        ) : (
          <div className="space-y-4 animate-in fade-in slide-in-from-bottom-2">
            <div className="flex items-center gap-2 text-emerald-400 bg-emerald-950/30 px-3 py-1 rounded-full w-max text-xs border border-emerald-500/30">
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              Signal Active
            </div>
            <div className="p-4 bg-black/40 rounded-xl border border-slate-700 font-mono text-xs break-all">
              <p className="text-slate-500 mb-2 uppercase tracking-widest text-[10px]">Vault Address</p>
              {walletAddress}
            </div>
          </div>
        )}
      </div>
    </section>
  );
}