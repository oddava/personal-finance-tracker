from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, Router

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")