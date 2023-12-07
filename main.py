import requests
import actions
from llm import LLM
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


llm = LLM()

ACTIONS = {
    "read_documentation": actions.read_documentation,
    "call_endpoint": actions.call_endpoint,
    "ask_question": actions.ask_question,
    "end_conversation": actions.end_conversation,
}


def handle_action(action, params):
    if action in ACTIONS:
        return ACTIONS[action](**params)
    else:
        raise ValueError(f"Unsupported action: {action}")


def main():
    query = input("Enter your query: ")

    while query:
        print("------------------------")
        response = llm.ask_llm(query)

        if "action" in response and response["action"] == "end_conversation":
            handle_action(response["action"], response["parameters"])
            break

        query = handle_action(response["action"], response["parameters"])


if __name__ == "__main__":
    main()
