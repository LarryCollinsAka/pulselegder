import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        // In production, Vercel routes /api/ naturally to the /api folder.
        // In development, we point to our local FastAPI port.
        destination: process.env.NODE_ENV === "development"
          ? "http://127.0.0.1:8000/api/:path*" 
          : "/api/", 
      },
    ];
  },
};

export default nextConfig;