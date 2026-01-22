'use client';

import SetupTreasury from '../components/SetupTreasury';
// import BalanceDisplay from '../components/BalanceDisplay'; 

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-[#020617] p-8">
      <div className="max-w-5xl mx-auto space-y-8">
        {/* Header Section */}
        <header className="flex justify-between items-end border-b border-slate-800 pb-6">
          <div>
            <h1 className="text-3xl font-bold text-white">Trade Command</h1>
            <p className="text-slate-400 mt-2">Manage your cross-border liquidity and legacy.</p>
          </div>
          <div className="text-right">
            <span className="text-[10px] text-slate-500 uppercase tracking-widest">Network</span>
            <p className="text-blue-400 font-mono text-sm">Polygon Amoy</p>
          </div>
        </header>

        {/* Grid for Components */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <SetupTreasury />
          
          {/* We will place the BalanceDisplay and Transfer components here */}
          <div className="p-8 bg-slate-900/50 rounded-2xl border border-slate-800 border-dashed flex items-center justify-center">
            <p className="text-slate-500 text-sm">Additional tools will appear after setup.</p>
          </div>
        </div>
      </div>
    </div>
  );
}