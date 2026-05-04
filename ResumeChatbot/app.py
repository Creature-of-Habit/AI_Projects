import os
import dotenv 
import asyncio

from dotenv import load_dotenv
from chainlit.types import ThreadDict
import chainlit as cl

@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])