import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load .env ONLY if running locally (Render provides environment variables automatically)
if not os.getenv("RENDER"):
    load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is not set. Ensure environment variables are configured.")

# Connect to MongoDB Atlas
client = AsyncIOMotorClient(MONGO_URI)
db = client["SudokuAuth"]
users_collection = db["users"]
