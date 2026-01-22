import os
from google import genai
from google.genai import types
from api.services.circle_service import get_balance

# 1. Initialize the new Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Define the System Instructions
# This tells the AI who it is and how to behave.
SYSTEM_PROMPT = """
You are the Pulse Ledger Treasury Manager. 
You help users manage their Circle Developer-Controlled wallets.
When a user asks about money, crypto, or balances, use the 'get_balance' tool.
"""

async def run_treasury_agent(user_prompt: str):
    # 3. Generate content with Tool Use enabled
    response = client.models.generate_content(
        model="gemini-2.0-flash", # Highly recommended for fast tool-use
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[get_balance], # Pass your Circle function here
            # 'auto' allows Gemini to decide when to call the tool
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=False
            )
        )
    )
    
    return response.text