
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):
    """
    Action to greet the user with a "Hello World!" message.

    This action sends a message to the user containing the text "Hello World!"
    using the provided `dispatcher` object.

    Attributes:
        None

    Methods:
        name(self) -> Text:
            Returns the name of the action, which is used to identify it in the
            domain file.

        run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            Executes the action by sending a message to the user.

    """

    def name(self) -> Text:
        """
        Returns the name of the action, which is used to identify it in the
        domain file.

        Args:
            None

        Returns:
            A string representing the name of the action.

        """
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Executes the action by sending a message to the user.

        Args:
            dispatcher: An object used to send messages to the user.
            tracker: An object representing the conversation tracker.
            domain: A dictionary containing the domain configuration.

        Returns:
            A list of dictionaries representing the events to be processed
            after the action is executed. In this case, it contains a single
            event representing the message sent to the user.

        """
        dispatcher.utter_message(text="Hello World!")
        return []


class ActionFlightDetails(Action):
    """
    Action to query a database for flight details.

    This action sends a message to the user indicating that the system is
    querying a database for flight details, using the provided `dispatcher`
    object. The action does not actually query the database, but simulates the
    behavior of a real action.

    Attributes:
        None

    Methods:
        name(self) -> Text:
            Returns the name of the action, which is used to identify it in the
            domain file.

        run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            Executes the action by sending a message to the user.

    """

    def name(self) -> Text:
        """
        Returns the name of the action, which is used to identify it in the
        domain file.

        Args:
            None

        Returns:
            A string representing the name of the action.

        """
        return "action_flight_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Executes the action by sending a message to the user.

        This action simulates the behavior of querying a database for flight
        details by sending a message to the user indicating that the system is
        performing the query.

        Args:
            dispatcher: An object used to send messages to the user.
            tracker: An object representing the conversation tracker.
            domain: A dictionary containing the domain configuration.

        Returns:
            A list of dictionaries representing the events to be processed
            after the action is executed. In this case, it contains a single
            event representing the message sent to the user.

        """
        dispatcher.utter_message(text="I am querying the database and will get back to you soon!")
        return []
