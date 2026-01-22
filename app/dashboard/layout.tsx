// app/dashboard/layout.tsx
import React from "react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen flex bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r p-4">
        <h2 className="text-xl font-bold mb-6">Pulse Ledger</h2>
        <nav className="space-y-2">
          <a href="/dashboard" className="block px-2 py-1 hover:bg-gray-100 rounded">
            Treasury
          </a>
          <a href="/dashboard/escrow" className="block px-2 py-1 hover:bg-gray-100 rounded">
            Escrow Deals
          </a>
          <a href="/dashboard/transactions" className="block px-2 py-1 hover:bg-gray-100 rounded">
            Transactions
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6">{children}</main>
    </div>
  );
}
