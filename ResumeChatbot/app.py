import os
import chainlit as cl
from tool_handler import handle_tool_calls
from tools import tools
from system_prompt import system_prompt
from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv(override=True)

groq_api_key = os.getenv('GROQ_API_KEY')

groq = AsyncOpenAI( 
    base_url="https://api.groq.com/openai/v1", 
    api_key=groq_api_key
    )

cl.instrument_openai()

MODEL = 'llama-3.3-70b-versatile'


@cl.on_message
async def chat(message: cl.Message):
    history = cl.user_session.get("history", [])
    
    messages = [{'role': 'system', 'content': system_prompt}] + history + [{'role': 'user', 'content': message.content}]
    
    done = False
    while not done:
        response = await groq.chat.completions.create(model=MODEL, messages=messages, tools=tools)
        finish_reason = response.choices[0].finish_reason

        if finish_reason == 'tool_calls':
            tool_message = response.choices[0].message
            tool_calls = tool_message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(tool_message)
            messages.extend(results)
        else:
            done = True

    reply = response.choices[0].message.content

    # Update history
    history.append({'role': 'user', 'content': message.content})
    history.append({'role': 'assistant', 'content': reply})
    cl.user_session.set("history", history)

    await cl.Message(content=reply).send()