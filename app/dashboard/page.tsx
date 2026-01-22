// app/dashboard/page.tsx
"use client";
import TreasurySetup from "../components/TreasurySetup";
import TreasuryConfig from "../components/TreasuryConfig";
import TransferTokens from "../components/TransferTokens";

export default function DashboardPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Treasury Dashboard</h1>

      {/* Wallet Setup */}
      <TreasurySetup />

      {/* Wallet Config */}
      <TreasuryConfig />

      {/* Transfer Tokens */}
      <TransferTokens />
    </div>
  );
}
