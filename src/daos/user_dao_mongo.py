import os
from bson import ObjectId
from dotenv import load_dotenv
import pymongo
from models.user import User

class UserDAOmongo:
    def __init__(self):
        try:
            env_path = "../.env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)

            mongodb_host = os.getenv("MONGODB_HOST")
            mongodb_user = os.getenv("DB_USERNAME")
            mongodb_pass = os.getenv("DB_PASSWORD")

            mongo_uri = f"mongodb://{mongodb_user}:{mongodb_pass}@{mongodb_host}:27017/"
            self.client = pymongo.MongoClient(mongo_uri)
            self.db = self.client["labo01"]
            self.mydoc = self.db["users"]

        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        all_users = self.mydoc.find()
        return [User(str(user["_id"]), user["name"], user["email"]) for user in all_users]

    def insert(self, user):
        """ Insert given user into MongoDB """
        result = self.mydoc.insert_one({
            "name": user.name,
            "email": user.email
        })
        return result.inserted_id

    def update(self, user):
        """ Update given user in MongoDB """
        self.mydoc.update_one(
            {"_id": user.id},
            {"$set": {"name": user.name, "email": user.email}}
        )

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        self.mydoc.delete_one({"_id": ObjectId(user_id)})