from pymongo import MongoClient
import certifi

# MongoDB Connection URL
url = "mongodb+srv://rehan007313_db_user:zljcEIl6vVooyTxX@practice01.39suw1y.mongodb.net/?appName=practice01"

# Initialize MongoClient with SSL certificate verification using certifi
# and a 5-second timeout for server selection.
client = MongoClient(url, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)

try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB Atlas")
except Exception as e:
    print(f"Error: Could not connect to MongoDB. Check IP Whitelisting/Network. \nDetails: {e}")

db = client.todo_db
collection_name = db["todo_collection"]
