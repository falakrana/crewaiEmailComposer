from crewai import Process, Crew
from agent import email_thinker, email_writer
from task import email_research_task, email_writer_task
import os

crew = Crew(
    agents=[email_thinker, email_writer],
    tasks=[email_research_task, email_writer_task],
    process=Process.sequential,
)

result = crew.kickoff(
    inputs={
        "topic": "Write email to HR of parul university, for re-opening the application link for company capture x(ml). As I forgot to apply in it on time.",
        "audience": "Formal letter",
    }
)

print(result)

