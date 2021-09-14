from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from ..config import MONGO_USER,MONGO_HOST,MONGO_PORT,MONGO_PASSWORD


client = AsyncIOMotorClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")
engine = AIOEngine(motor_client=client, database="short_links")