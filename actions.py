from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import random


class ActionCheckStatus(Action):
    def name(self):
        return "action_check_status"

    def run(self, dispatcher, tracker, domain):
        # return a random status, just a mockup
        statuses = ["received", "rejected", "interview", "unknown"]
        status = random.choice(statuses)
        return [SlotSet("status", status)]


class ActionCheckPositions(Action):
    def name(self):
        return "action_check_positions"

    def run(self, dispatcher, tracker, domain):
        # return hard-coded open positions, this would normally come from an API
        positions = {
            "technical": ["machine learning engineer", "ML product success engineer"],
            "business": ["Marketing Consultant", "Sales Engineer", "Equity Analyst"],
        }
        position_type = tracker.get_slot("role_type")
        if position_type == "any":
            relevant_positions = positions["technical"] + positions["business"]
        else:
            relevant_positions = positions.get(position_type, [])
        return [SlotSet("positions", (" and ").join(relevant_positions))]


class ActionProvideProcess(Action):
    def name(self):
        return "action_provide_process"

    def run(self, dispatcher, tracker, domain):
        processes = {
            "technical": """
            Following are the detailed steps for the process:
            * Interview with a Rasa team member who is familiar with the positions to discuss if the basic requirements - from both sides - are met
            * A small coding challenge for you so we can determine your skill level
            * A chat to review your take-home assignment
            * Meeting with HR executives to find out what you need to be happy and work productively and get an insight to Rasa’s values and how we work as a team
            * Our CEO Alex and Alan will tell you about their story, explain why they founded Rasa and where they see the company in the future
            *Another chat with HR to discuss things like salary
            Typically takes between 3-4 weeks to complete the process
          """,
            "Business": """
            Following are the detailed steps for the process:
            * Interview with a Rasa team member who is familiar with the positions to discuss if the basic requirements - from both sides - are met
            * Another round of interview to determine domain expertise for the specific role
            * Meeting with HR executives to find out what you need to be happy and work productively and get an insight to Rasa’s values and how we work as a team
            * Our CEO Alex and Alan will tell you about their story, explain why they founded Rasa and where they see the company in the future
            *Another chat with HR to discuss things like salary
            Typically takes between 3-4 weeks to complete the process
          """,
        }
        process_type = tracker.get_slot("role_type")
        if process_type == "technical":
            dispatcher.utter_message(processes["technical"])
        else:
            dispatcher.utter_message(processes["Business"])
        return []
