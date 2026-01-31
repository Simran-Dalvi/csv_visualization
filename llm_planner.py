import os
import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_analysis_plan(user_prompt, columns):
    system_prompt = '''
    You are a data analyst

    your task :
    - Convert user questions into a JSON plan for data visualization.

    Rules:
    - Use ONLY the given columns
    - Supported charts: bar, line, histogram, pie
    - Aggregations: mean, sum, count
    - Output ONLY valid JSON (no explanation)

    JSON format:
    {
    "chart": "",
    "x": "",
    "y": "",
    "aggregation": "",
    "title": ""
    }
    '''


    user_message = f"""
    Dataset columns:
    {columns}

    User question:
    {user_prompt}
    """

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)