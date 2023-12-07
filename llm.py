import json
import openai

class LLM:
    def __init__(self):
        self.completion = None
        self.chat_history = []
        self.init()


    def init(self):
        #openai.api_type = "azure"
        #openai.api_base = "https://xxxxx.openai.azure.com/"
        #openai.api_version = "2023-07-01-preview"
        openai.api_key = "XXXXXXXXXXXXXXXXXXXXXXX"
        self.add_system_prompt()


    def add_system_prompt(self):
        system_prompt = {
            "role": "system",
            "content": """You are GPT-API, the master of all APIs. I'll want you to perform tasks for me as an AI agent.
            I need a JSON response from you if you want to perform an action. Your answer must be strictly only JSON and no other text.
            Each action has 2 mandatory fields: action and parameters. The action field tells me what action you want to perform and the parameters field related to that action.
            I'll give you a set of actions that you can perform to complete a task.
            
            1) read_documentation: This action will give you the details of an API endpoint. You can use this to find out what parameters the endpoint accepts.
            Here's an example of how you can use this action:
            {
                "action": "read_documentation",
                "parameters": {"endpoint": "http://127.0.0.1:5000/geocoder", "documentation_url": "http://127.0.0.1:5000/docs/geocoder"}
            }
            
            2) call_endpoint: This action will call an API endpoint with the parameters you provide. NEVER CALL AN ENDPOINT WITHOUT READING THE DOCUMENTATION IT FIRST.
            Here's an example of how you can use this action:
            {
                "action": "call_endpoint",
                "parameters": {"endpoint": "http://127.0.0.1:5000/geocoder", "parameters": {"address": "87 Brompton Road"}}
            }
            
            3) ask_question: With this action you can ask the user the clarification you need. You can ask any question you want.
            Here's an example of how you can use this action:
            {
                "action": "ask_question",
                "parameters": {"question": "Are you looking for the Brompton Road in London or Portsmouth?"}
            }
             
            4) end_conversation: This action will end the conversation. You must add a final message to the user, this is where you have to answer their question.
            Here's an example of how you can use this action:
            {
                "action": "end_conversation",
                "parameters: {'final_message_to_user': 'Task completed: the coordinates of W3 7NP are 51.50632, -0.21775'}
            }
            
            You also have access multiple applications through APIs, you can use them to perform actions.
            Here are the applications you have access to:
            1) Geocoder: This application will give you the latitude and longitude of a postcode.
               Use the read_documentation action to find out what parameters the endpoint accepts.
               Endpoint URL: http://127.0.0.1:5000/postcode_geocoder
               Documentation URL: http://127.0.0.1:5000/docs/postcode_geocoder
               
            2) Sunset Sunrise: This application will give you the sunset and sunrise times of latitude and longitude coordinates.
                 Use the read_documentation action to find out what parameters the endpoint accepts.
                 Endpoint URL: http://127.0.0.1:5000/docs/sunset_sunrise
                 Documentation URL: http://127.0.0.1:5000/sunset_sunrise
            
            When completing a task first always setup a plan of actions in your mind. If you want to call an API endpoint, always read the documentation first to find out what parameters it accepts. 
            Only then call the endpoint with the parameters you want to pass.
            When the task is ready, the final action must be end_conversation.
            """
        }
        self.chat_history.append(system_prompt)

    def ask_llm(self, query):

        message = {'role': 'user', 'content': query}
        self.chat_history.append(message)

        completion = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=self.chat_history,
            temperature=0.0
        )

        answer = completion['choices'][0]['message']['content']
               

        try:
            # Occasionally the model fails to reply only JSON, this is just to make sure it gets a JSON.
            # Find the index of the first "{" and the last "}"
            first_brace_index = answer.find("{")
            last_brace_index = answer.rfind("}")

            # Extract the text between these indices, including the braces
            answer = answer[first_brace_index:last_brace_index + 1] if first_brace_index != -1 and last_brace_index != -1 else ""
            
            answer = json.loads(answer)
            history_answer = json.dumps(answer)
        except:
            history_answer = answer


        history_entry = {
                "role": "assistant",
                "content": str(history_answer)
            }


        self.chat_history.append(history_entry)

        return answer
