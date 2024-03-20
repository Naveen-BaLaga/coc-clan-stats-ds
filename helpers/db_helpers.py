from decouple import config
import pymongo
import sys

MONGODB_CONNECTION_STRING = config('MONGODB_CONNECTION_STRING')
DB_NAME = config('DB_NAME')
TABLES_COLLECTION_NAME = config('TABLES_COLLECTION_NAME')

try:
  client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received.")
  sys.exit(1)

def update_total_multiplayer_battles_won(json_data):
    try:
        db = client[DB_NAME]
        
        collection = db[TABLES_COLLECTION_NAME]

        # Find or insert entry with key "Table Name" equal to "Highest Multiplayer Battles Won"
        entry = collection.find_one({"Table Name": "Highest Multiplayer Battles Won"})
        if entry:
            # Update existing entry
            collection.update_one({"_id": entry["_id"]}, {"$set": json_data})
        else:
            # Insert new entry
            collection.insert_one(json_data)
        return True
    except Exception as e:
        print("Error in updating total multiplayer battles won:", str(e))
        return False