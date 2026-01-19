from fastapi import FastAPI

# Define app with custom docs paths to avoid Next.js routing conflicts
app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

@app.get("/api/health")
def health_check():
    return {"status": "Pulse Ledger API Online", "runtime": "Python 3.12 on Vercel"}