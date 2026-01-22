export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-slate-900 text-white">
      {/* Sidebar - Navigation for Trade, Treasury, & Compliance */}
      <aside className="w-64 border-r border-slate-800 p-6 hidden md:block">
        <h2 className="text-xl font-bold mb-10 text-blue-500">Pulse Ledger</h2>
        <nav className="space-y-4">
          <p className="text-xs uppercase text-slate-500 font-semibold">Main</p>
          <div className="hover:text-blue-400 cursor-pointer">Overview</div>
          <div className="hover:text-blue-400 cursor-pointer">Treasury</div>
          <div className="hover:text-blue-400 cursor-pointer">Compliance</div>
        </nav>
      </aside>
      <main className="flex-1 p-8">{children}</main>
    </div>
  );
}