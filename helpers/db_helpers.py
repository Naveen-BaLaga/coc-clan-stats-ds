from decouple import config
import pymongo
import sys

MONGODB_CONNECTION_STRING = config('MONGODB_CONNECTION_STRING')
DB_NAME = config('DB_NAME')
TABLES_COLLECTION_NAME = config('TABLES_COLLECTION_NAME')
WARS_COLLECTION_NAME = config('WARS_COLLECTION_NAME')

try:
  client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received.")
  sys.exit(1)

def update_table(json_data, table_name):
  try:
    db = client[DB_NAME]   
    collection = db[TABLES_COLLECTION_NAME]

    # Find or insert entry with key "Table Name" equal to the table name
    entry = collection.find_one({"Table Name": table_name})
    if entry:
      # Update existing entry
      collection.update_one({"_id": entry["_id"]}, {"$set": json_data})
    else:
      # Insert new entry
      collection.insert_one(json_data)
    return True
  except Exception as e:
    print("Error in updating " + str(table_name) + ": " + str(e))
    return False
  
def update_wars(json_data, opponent_tag):
  try:
    db = client[DB_NAME]   
    collection = db[WARS_COLLECTION_NAME]
    opponent_tag = opponent_tag[1:]
    # Find or insert entry with key "Opponent Tag" equal to the opponent tag
    entry = collection.find_one({"_id": opponent_tag})
    if entry:
      # Update existing entry
      collection.update_one({"_id": opponent_tag}, {"$set": json_data})
    else:
      json_data["_id"] = opponent_tag
      # Insert new entry
      collection.insert_one(json_data)
    return True
  except Exception as e:
    print("Error in updating " + str(opponent_tag) + ": " + str(e))
    return False
  
'''
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
        print("Error in updating Highest Multiplayer Battles Won:", str(e))
        return False

def update_total_wall_destroyed(json_data):
  try:
    db = client[DB_NAME]   
    collection = db[TABLES_COLLECTION_NAME]

    # Find or insert entry with key "Table Name" equal to "Highest Walls Destroyed"
    entry = collection.find_one({"Table Name": "Highest Walls Destroyed"})
    if entry:
      # Update existing entry
      collection.update_one({"_id": entry["_id"]}, {"$set": json_data})
    else:
      # Insert new entry
      collection.insert_one(json_data)
    return True
  except Exception as e:
    print("Error in updating Highest Walls Destroyed:", str(e))
    return False
'''