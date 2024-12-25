from crewai import Task
from models import VenueDetails
from agents import venue_coordinator, logistics_manager, marketing_communications_agent

venue_task = Task(
    description  = "Find a venue in {event_city} that meets criteria for {event_topic}",
    expected_output = "All details of the chosen venue", 
    human_input = True,
    output_json=VenueDetails,
    output_file="outputs/venue_details.json",
    agent=venue_coordinator,
)

logistics_task = Task(
    description="Coordinate catering and equipment for an event with {expected_participants} participants on {tentative_date}.",
    expected_output="Confirmation of all logistics arrangements, including catering and equipment setup.",
    human_input=True,
    async_execution=True,
    agent=logistics_manager,
)

marketing_task = Task(
    description="Promote the {event_topic} aiming to engage at least {expected_participants} attendees.",
    expected_output="Report on marketing activities and attendee engagement formatted as markdown.",
    async_execution=True,
    output_file="outputs/marketing_report.md",
    agent=marketing_communications_agent,
)