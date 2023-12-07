import requests
import json
import time

# ------------------ ACTIONS ------------------

def read_documentation(endpoint, documentation_url):
    print(f"Reading documentation of {endpoint} at {documentation_url}")
    response = requests.get(f"{documentation_url}")
    if response.status_code == 200:
        api_details = response.json()
        return json.dumps(api_details)
    else:
        return json.dumps({"message": f"Failed to read documentation of {endpoint} at {documentation_url}. Are you sure the endpoint exists?"})


def call_endpoint(endpoint, parameters):
    print(f"Calling endpoint: {endpoint} with parameters: {parameters}")
    response = _retry_api(endpoint, parameters)
    try:
        json_response = response.json()
        print("JSON response received")
        return f"The response from calling the {endpoint} is: {json_response}"
    except ValueError:
        print("Text response received")
        return f"The response from calling the {endpoint} is: {response.text}"


def ask_question(question):
    print("Clarification needed.")
    print(f"{question}")
    return input("Enter your answer: ")


def end_conversation(final_message_to_user):
    print(f"Ending conversation with message: {final_message_to_user}")



# ------------------ Private functions ------------------

def _retry_api(endpoint, parameters, retries=3, delay=5):
    for attempt in range(retries):
        response = requests.post(endpoint, json=parameters)
        if response.status_code in (200, 299):
            return response
        print(f"Attempt {attempt+1} failed. Retrying in {delay} seconds...")
        time.sleep(delay)
    raise ValueError(f"Failed to get a valid response after {retries} attempts.")

