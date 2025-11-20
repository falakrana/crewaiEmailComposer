from agent import email_thinker, email_writer
from tools import tool
from crewai import Task

email_research_task = Task(
    description=(
        "Think on constructing email on topic: {topic}."
        "Focus on being specific if it's mentioned to draft an email to a professional or informal person."
    ),
    expected_output=(
        "A well-thought email on {topic} that will be sent to the audience: {audience}."
    ),
    tools=[tool],
    agent=email_thinker,
    # async_execution=True,
)

email_writer_task = Task(
    description=(
        "Write email on topic: {topic} while taking into account the audience: {audience}."
        " Write in such a way that if it's specified to write an informal mail, then write in an informal,"
        " attractive manner."
    ),
    expected_output=(
        "Output should be in proper structure with:\n"
        "Subject: ....\n\n"
        "Body: ...."
    ),
    tools=[tool],
    agent=email_writer,
    async_execution=False,
)