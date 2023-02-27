from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCalculate(Action):

    def name(self) -> Text:
        return "action_calculate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        num1 = tracker.get_slot("num1")
        num2 = tracker.get_slot("num2")
        operation = tracker.latest_message["intent"].get("name")
        
        if operation == "addition":
            result = num1 + num2
            dispatcher.utter_message(text=f"The sum of {num1} and {num2} is {result}")
        elif operation == "subtraction":
            result = num1 - num2
            dispatcher.utter_message(text=f"The difference between {num1} and {num2} is {result}")
        elif operation == "multiplication":
            result = num1 * num2
            dispatcher.utter_message(text=f"The product of {num1} and {num2} is {result}")
        elif operation == "division":
            if num2 == 0:
                dispatcher.utter_message(text="I cannot divide by zero.")
            else:
                result = num1 / num2
                dispatcher.utter_message(text=f"The quotient of {num1} and {num2} is {result}")
        else:
            dispatcher.utter_message(template="utter_default")

        return []