import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Debug: Print MONGO_URI to check if it's loaded
MONGO_URI = os.getenv("MONGO_URI")
print(f"🔍 Loaded MONGO_URI: {MONGO_URI}")  # Add this for debugging

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is not set in .env file. Check if the .env file exists and is loaded correctly.")

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)

# Explicitly set the database name
db = client["SudokuAuth"]  
users_collection = db["users"]  # Reference to users collection
