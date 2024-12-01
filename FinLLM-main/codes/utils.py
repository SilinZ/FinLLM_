import openai
import re

# API key 
openai.api_key = "  "

def get_gpt_response(message, model="gpt-4", max_tokens=5000):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=message,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return ""

def parse_prediction_response(gpt_response):
    parsed_data = {}
    response = re.sub(r"\s*\n\s*", "\n", gpt_response).strip()

    # Extract Analysis
    analysis_match = re.search(r"Analysis[:\s]*\n*(.+?)\n(?:Statements Used|Statements used|Statements)", response, re.DOTALL)
    parsed_data["analysis"] = analysis_match.group(1).strip() if analysis_match else None

    # Extract Statements Used
    statements_match = re.search(r"(?:Statements Used|Statements used|Statements)[:\s]*\n*([\d,\s]+)\n", response)
    if statements_match:
        statements_str = statements_match.group(1).strip()
        parsed_data["statements_used"] = [int(s.strip()) for s in statements_str.split(',') if s.strip().isdigit()]
    else:
        parsed_data["statements_used"] = []

    # Extract Prediction
    prediction_match = re.search(r"Prediction[:\s]*\n*(.+)", response)
    parsed_data["prediction"] = prediction_match.group(1).strip() if prediction_match else None

    return parsed_data

def parse_refine_response(response):
    refined_statements = {}
    eliminated_statements = {}

    # Extract Refined Statements
    refined_matches = re.findall(r"Original:\s*(\d+)\.\s*(.*?)\s*Refined:\s*(.*?)(?=\n\n|$)", response, re.DOTALL)
    for statement_id, _, refined_statement in refined_matches:
        refined_statements[int(statement_id)] = refined_statement.strip()

    # Extract Eliminated Statements
    eliminated_section = re.search(r"Statements to Eliminate:\s*(.*)", response, re.DOTALL)
    if eliminated_section:
        eliminated_ids = re.findall(r"(\d+)", eliminated_section.group(1))
        for statement_id in eliminated_ids:
            eliminated_statements[int(statement_id)] = None

    return refined_statements, eliminated_statements



# %%
