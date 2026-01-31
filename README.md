LLM-Driven Interactive Data Dashboard

Dataset: titanic.csv
LLM: OpenAI (API key via .env)
Frontend: Streamlit
Charts: Plotly
Logic: LLM → JSON plan → Python execution

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


We’ll code in this order:

1. Minimal Streamlit app

2. Load Titanic dataset

3. Hardcode one chart (baseline)

4. Add LLM → JSON output

5. Parse & validate LLM output

6. Dynamic chart generation

7. Error handling

8. Resume-ready README# csv_visualization