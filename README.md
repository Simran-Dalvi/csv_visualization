# LLM-Driven Interactive Data Dashboard

An end-to-end LLM-powered data visualization system that converts natural language queries into interactive dashboards using structured reasoning and deterministic Python execution.

This project demonstrates how Large Language Models can be used for planning and intent understanding, while all data processing and visualization remain fully controlled and reproducible.


# What This Project Does

1. Loads a structured CSV dataset (titanic.csv)

2. Accepts user queries in natural language

3. Uses an LLM (OpenAI) to interpret user intent

4. Converts the query into a structured JSON analysis plan

5. Executes the plan using Pandas

6. Renders interactive Plotly dashboards

7. Displays everything in a Streamlit web application

# Tech Stack

* Language: Python

* Frontend: Streamlit

* Data Processing: Pandas

* Visualization: Plotly

* LLM: OpenAI API

* Environment Management: venv + .env


# Project Architecture

```bash
csv-visualization/
│
├── data/
│   └── titanic.csv
│
├── app.py              # Streamlit UI
├── llm_planner.py      # LLM → JSON logic
├── dashboard.py        # Pandas + Plotly
├── .env                # OpenAI key
├── requirements.txt
└── README.md
```
# File Responsibilities
 ## app.py — Streamlit Frontend

    User interface for entering natural language queries

    Displays dataset preview

    Sends user prompt to the LLM planner

    Displays the generated JSON plan

    (Optionally) renders interactive charts


## llm_planner.py — LLM Reasoning Layer

    Sends dataset schema + user prompt to OpenAI

    Forces the LLM to return strict JSON

    Produces a structured visualization plan such as:

    No data access, no plotting, no execution

## dashboard.py — Execution & Visualization

    Validates the LLM-generated plan

    Executes aggregation logic using Pandas

    Generates interactive charts using Plotly

    Returns figures to be rendered in Streamlit

## .env

    Stores the OpenAI API key securely

    Loaded at runtime using python-dotenv

    Excluded from version control

# End-to-End Workflow

``` bash

User Prompt
   ↓
Streamlit UI
   ↓
LLM (intent understanding & planning)
   ↓
Structured JSON plan
   ↓
Python execution (Pandas)
   ↓
Interactive Plotly dashboard
   ↓
Web display

```

# Example Queries

* Show survival rate by gender

* Compare survival across passenger classes

* Show age distribution of passengers