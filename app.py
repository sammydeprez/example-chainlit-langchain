import chainlit as cl
from langchain_openai.chat_models import AzureChatOpenAI

llm = AzureChatOpenAI(model="gpt-4o-mini")

@cl.on_message
async def on_message(message: cl.Message):
    
    llm_response = llm.invoke(cl.chat_context.to_openai())
    response_msg = cl.Message(content=llm_response.content)
    await response_msg.send()


if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)