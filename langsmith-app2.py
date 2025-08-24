import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langsmith import traceable

# Load environment variables from .env
load_dotenv()

# Shared LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# ------------------------
# Step 1: Rephrase Question
# ------------------------
@traceable
def rephrase_question(question: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Rephrase the following question to make it clearer:\n\n{q}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"q": question})

# ------------------------
# Step 2: Answer Question
# ------------------------
@traceable
def answer_question(question: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Answer clearly:\n\n{q}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"q": question})

# ------------------------
# Step 3: Summarize Answer
# ------------------------
@traceable
def summarize_answer(answer: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Summarize the following answer in one sentence:\n\n{a}"
    )
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"a": answer})

# ------------------------
# Main Orchestration
# ------------------------
@traceable
def ask_ai(question: str):
    new_q = rephrase_question(question)
    ans = answer_question(new_q)
    summary = summarize_answer(ans)
    return {"question": new_q, "answer": ans, "summary": summary}

if __name__ == "__main__":
    result = ask_ai("Can you tell me what LangSmith does?")
    print(result)
