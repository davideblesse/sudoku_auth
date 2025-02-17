import os
from motor.motor_asyncio import AsyncIOMotorClient

# Environment variable set in Render dashboard.
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in the environment variables.")

# Connect to MongoDB Atlas using the provided URI.
client = AsyncIOMotorClient(MONGO_URI)

# Explicitly set your database name.
db = client["SudokuAuth"]
users_collection = db["users"]
