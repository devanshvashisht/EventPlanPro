import os
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from utils import get_openai_api_key, get_serper_api_key
from dotenv import load_dotenv
load_dotenv()

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'
serper_api_key = get_serper_api_key()


#initializing the tools
search_tool = SerperDevTool(api_key=serper_api_key)
scrape_tool = ScrapeWebsiteTool(api_key=openai_api_key)



#Define agents
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Identify and book an appropriate venue based on event requirements",
    tools = [search_tool,scrape_tool],
    verbose=True,
    backstory=(
        "With a keen sense of space and "
        "understanding of event logistics, "
        "you excel at finding and securing "
        "the perfect venue that fits the event's theme, "
        "size, and budget constraints."
    )    
)

logistics_manager = Agent(
    role="Logistics Manager",
    goal="Manage all logistics for the event, including catering and equipment",
    tools = [search_tool,scrape_tool],
    verbose=True,
    backstory=(
        "Organized and detail-oriented, "
        "you ensure that every logistical aspect of the event "
        "from catering to equipment setup "
        "is flawlessly executed to create a seamless experience."
    )
)

marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Market the event effectively and engage participants",
    tools = [search_tool,scrape_tool],
    verbose=True,
    backstory=(
        "Creative and communicative, "
        "you craft compelling messages and "
        "engage with potential attendees "
        "to maximize event exposure and participation."
    )
)