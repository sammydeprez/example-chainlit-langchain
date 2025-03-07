import chainlit as cl
from langchain_openai.chat_models import AzureChatOpenAI

llm = AzureChatOpenAI(model="gpt-4o-mini")

@cl.on_message
async def on_message(message: cl.Message):

    chat_conversation = cl.chat_context.to_openai()
    
    # Sync
    # llm_response = llm.invoke(chat_conversation)
    # response_msg = cl.Message(content=llm_response.content)
    # await response_msg.send()

    # Async
    response_msg = cl.Message(content="")
    llm_response = llm.stream(input = chat_conversation)
    for response in llm_response:
        await response_msg.stream_token(response.content)
    await response_msg.send()