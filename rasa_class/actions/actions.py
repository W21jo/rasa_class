from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionSayShirtSize(Action):

#     def name(self) -> Text:
#         return "action_say_shirt_size"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         shirt_size = tracker.get_slot("shirt_size")
#         if not shirt_size:
#             dispatcher.utter_message(text="I don't know your shirt size.")
#         else:
#             dispatcher.utter_message(text=f"Your shirt size is {shirt_size}!")
#         return []
# class ActionSayName(Action):

#     def name(self) -> Text:
#         return "action_say_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name = tracker.get_slot("name")
#         if not name:
#             dispatcher.utter_message(text="I don't know your name .")
#         else:
#             dispatcher.utter_message(text=f"Your shirt size is {name}!")
#         return []




class ActionReturnName(Action):
    def name(self) -> Text:
        return "action_return_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the name slot value from the tracker
        name = tracker.get_slot("name")

        # Check if the name slot has a value
        if name:
            # Respond with the stored name
            dispatcher.utter_message(f" Welcome {name}.")
        else:
            # If the name slot is not set, respond with a default message
            dispatcher.utter_message("I don't have a name. Please provide a name.")

        return []