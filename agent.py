from crewai import Agent

from tools import tool


from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    # model="gemini-pro",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    # google_api_key="AIzaSyAMEeev0hI4xbL94ujCJn7cfpSu0zuAkso",
)

email_thinker = Agent(
    role="Email Thinker",
    goal="Think about the email to be sent",
    backstory="You are an expert in email marketing and you are responsible for thinking about the email to be sent to targeted audience: {audience} on topic {topic}.",
    memory=True,
    verbose=True,
    llm=llm,
    allow_delegation=True,
    tools=[tool],
)


email_writer = Agent(
    role="Email Writer",
    goal="Write an eye catching email based on the email to be sent",
    backstory="You are an expert in structuring email and you are responsible for writing the email to be sent to targeted audience: {audience} in an attractive way on topic {topic}. Use google for better news of the topic from current affairs.",
    memory=True,
    verbose=True,
    llm=llm,
    allow_delegation=False,
    tools=[tool],
)
