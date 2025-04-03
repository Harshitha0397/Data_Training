from pymongo import MongoClient

def mongodb_crud_operations():
    # Connect to MongoDB. Change the URI if needed.
    client = MongoClient("mongodb://localhost:27017/")
    db = client["training_db"]
    collection = db["users"]

    # CREATE: Insert a new document
    new_user = {"name": "Bob", "age": 28, "city": "Los Angeles"}
    result = collection.insert_one(new_user)
    print("Inserted document id:", result.inserted_id)

    # READ: Find a document
    user = collection.find_one({"name": "Bob"})
    print("Found document:", user)

    # UPDATE: Modify the user's age
    update_result = collection.update_one({"name": "Bob"}, {"$set": { "age": 29}})
    print("Documents updated:", update_result.modified_count)

    # DELETE: Remove the document
    delete_result = collection.delete_one({"name": "Bob"})
    print("Documents deleted:", delete_result.deleted_count)

    # Close the connection
    client.close()

if __name__ == "__main__":
    mongodb_crud_operations()
