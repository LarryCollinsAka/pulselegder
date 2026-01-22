import Link from 'next/link';

export default function LandingPage() {
  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-6 text-center">
      <h1 className="text-6xl md:text-8xl font-black tracking-tighter mb-6 bg-gradient-to-r from-blue-500 to-emerald-400 bg-clip-text text-transparent">
        PULSE LEDGER
      </h1>
      <p className="max-w-xl text-lg md:text-xl text-slate-400 mb-10">
        Empowering Pan-African trade with instant USDC settlement and a lasting legacy.
      </p>
      <Link 
        href="/dashboard"
        className="px-10 py-4 bg-white text-black font-bold rounded-full hover:bg-slate-200 transition-transform hover:scale-105"
      >
        Enter Command Center
      </Link>
    </main>
  );
}