import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langsmith import traceable

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Prompt
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer this question clearly: {question}"
)

# Chain
chain = prompt | llm | StrOutputParser()

@traceable
def ask_ai(question: str):
    return chain.invoke({"question": question})

if __name__ == "__main__":
    print(ask_ai("What is LangSmith and why is it useful?"))
