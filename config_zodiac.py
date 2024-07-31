APP_TITLE = "Zodiac Symbol"
APP_INTRO = """This is a demonstration app that determines a users zodiac symbol based on their birth month and date. 
"""

APP_HOW_IT_WORKS = """
This app collects the name, birth Month, and birth date of the user, and provides them their Zodiac symbol. 
It utilizes the OpenAI and other AI APIs to send a custom prompt to AI with the user's inputs and returns the AI's response. 
"""

SHARED_ASSET = {
}

HTML_BUTTON = {
    
}

SYSTEM_PROMPT = """You are an expert in zodiac symbols. You know the accurate zodiac symbol based on a person's birth month and date, and you """

PHASES = {
    "name": {
        "name": "User Details",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "helper": "First name only, please",
                "value": "",
            },
            "month": {
                "type": "radio",
                "label": """What is your birth month?""",
                "options": ["January","February","March","April","May","June","July","August","September","October","November","December"],
            },
            "day": {
                "type": "number_input",
                "label": """What is your birth day?""",
                "min_value": 1,
                "max_value":31
            },
            "year": {
                "type": "number_input",
                "label": """What is your birth year?""",
                "min_value": 1900,
                "max_value":2020
            },
            "system": {
                "type": "selectbox",
                "label": """Astrology System""",
                "options": ["Western","Chinese"],
            },
        },
        "phase_instructions": "",
        "user_prompt": "My name is {name}. I was born on {month} {day}, {year}. Please provide me my zodiac symbol, and give a short horoscope for the day, according to the {system} astrology system.",
        "ai_response": True,
        "allow_skip": True,
        "show_prompt": True,
    }
}

def prompt_conditionals(prompt, user_input, phase_name=None):
    # Construct the user prompt with user inputs
    if phase_name in PHASES:
        phase = PHASES[phase_name]
        user_prompt = phase["user_prompt"].format(
            name=user_input.get("name", ""),
            month=user_input.get("month", ""),
            day=user_input.get("day", ""),
            year=user_input.get("year", ""),
            system=user_input.get("system", "")
        )
        return user_prompt
    return prompt

selected_llm = "gpt-4o-mini"

LLM_CONFIGURATIONS = {
    "gpt-4o-mini": {
        "model": "gpt-4o-mini",
        "frequency_penalty": 0,
        "max_tokens": 1000,
        "presence_penalty": 0,
        "temperature": 1,
        "top_p": 1,
        "price_input_token_1M":0.50,
        "price_output_token_1M":1.50
    },
    # ... other configurations
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

# Example user input
user_input = {
    "name": "Alice",
    "month": "April",
    "day": 25,
    "year": 1990,
    "system": "Western"
}

# Construct the prompt and print it for debugging
constructed_prompt = prompt_conditionals(SYSTEM_PROMPT, user_input, "name")
print("Constructed Prompt:", constructed_prompt)

# Function to send the prompt to the selected LLM
def get_ai_response(prompt, model="gpt-4o-mini"):
    # Dummy function to represent sending the prompt to the model
    print(f"Sending prompt to model {model}: {prompt}")
    # Simulate AI response
    return "This is a simulated AI response."

# Get the AI response and print it for debugging
ai_response = get_ai_response(constructed_prompt, selected_llm)
print("AI Response:", ai_response)
