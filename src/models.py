import random
import typing
from odmantic import Model
from .db.mongodb import engine
from pydantic import BaseModel

alphabet = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class ShortLinkIndex(Model):
    index_number: int

    @staticmethod
    async def init_index():
        model = ShortLinkIndex(index_number=len(alphabet) ** 7 + 1)
        await engine.save(model)

class DBFileResponse(BaseModel):
    url: str

class DBFile(Model):
    filename: str
    content_type: str
    contents: typing.Union[bytes, str]
    short_link: typing.Optional[str]

    async def save_to_db(self) -> str:
        index_model = await engine.find_one(ShortLinkIndex)
        index_model.index_number += random.randint(1000, 10000)
        index = index_model.index_number

        short_link = ''
        while index:
            char = index % len(alphabet)
            short_link += alphabet[char]
            index //= len(alphabet)

        self.short_link = short_link

        await engine.save(self)
        await engine.save(index_model)

        return short_link
