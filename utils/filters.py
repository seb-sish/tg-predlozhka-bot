from aiogram.types import Message
from aiogram.filters import Filter

class InMessageFilter(Filter):
    def __init__(self, my_text: str) -> None:
        self.my_text = my_text

    async def __call__(self, message: Message) -> bool:
        if message.text is None:
            return False
        return self.my_text in message.text\

