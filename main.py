import os 
import warnings
warnings.filterwarnings('ignore')

from crewai import Crew
from tasks import venue_task, logistics_task, marketing_task
from utils import get_openai_api_key, get_serper_api_key
from dotenv import load_dotenv
load_dotenv()


openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'
serper_api_key = get_serper_api_key()


print("Welcome to Event plan pro!\n Please enter the following details to get started")

#Event details input from user
event_details = {
    "event_topic": input("Enter the event topic: "),
    "event_description": input("Enter a brief event description: "),
    "event_city": input("Enter the city where the event will be held: "),
    "tentative_date": input("Enter the tentative date (YYYY-MM-DD): "),
    "expected_participants": int(input("Enter the expected number of participants: ")),
    "budget": int(input("Enter the event budget: ")),
    "venue_type": input("Enter the type of venue (e.g., Conference Hall): "),
}

# Define crew
event_management_crew = Crew(
    agents=[venue_task.agent, logistics_task.agent, marketing_task.agent],
    tasks=[venue_task, logistics_task, marketing_task],
    verbose=True,
)

# Run crew tasks
result = event_management_crew.kickoff(inputs=event_details)

# Display outputs
import json
from pprint import pprint


# Display venue details JSON
with open("outputs/venue_details.json") as f:
    venue_data = json.load(f)
    pprint(venue_data)


# Display marketing report markdown
from IPython.display import Markdown


print("\nMarketing Report:\n")
Markdown("outputs/marketing_report.md")