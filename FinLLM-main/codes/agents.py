from utils import get_gpt_response, parse_prediction_response, parse_refine_response

def agent_1_get_facts(transcript, prompt):
    title = transcript['title']
    content = transcript['content']
    message = [
        {"role": "system", "content": "You are an expert financial analyst specializing in earnings call analysis and stock market prediction."},
        {"role": "user", "content": prompt + content}
    ]
    response = get_gpt_response(message)
    return {'title': title, 'facts': response}

def agent_2_get_statements(facts, prompt):
    statements = {}
    message = [
        {"role": "system", "content": "You are an expert financial analyst specializing in earnings call analysis and stock market prediction."},
        {"role": "user", "content": prompt + facts['facts']}
    ]
    response = get_gpt_response(message)
    statements_list = response.strip().split('\n\n')
    for idx, statement in enumerate(statements_list):
        statements[idx] = {"title": facts['title'], "statement": statement.strip()}
    return statements

def store_statements_in_storage(statements, storage):
    last_id = max(storage.keys(), default=-1) + 1
    for content in statements.values():
        storage[last_id] = content
        last_id += 1
    return storage

def agent_3_get_predictions(facts, storage, prompt):
    title = facts['title']
    fact_text = facts['facts']
    statements_text = '\n\n'.join([f"{id}. {content['statement']}" for id, content in storage.items()])
    message = [
        {"role": "system", "content": "You are an expert financial analyst specializing in earnings call analysis and stock market prediction."},
        {"role": "user", "content": prompt + '\nFacts:\n' + fact_text + '\nStatements:\n' + statements_text}
    ]
    response = get_gpt_response(message)
    parsed_response = parse_prediction_response(response)
    used_statement_ids = parsed_response.get('statements_used', [])
    used_statements = {id: storage[id] for id in used_statement_ids if id in storage}
    return {
        "title": title,
        "statements used": used_statements,
        "prediction": parsed_response.get('prediction'),
        "analysis": parsed_response.get('analysis')
    }

def agent_4_get_feedback(facts, prediction, actual, prompt):
    statements_used_text = '\n'.join([f"{id}. {s['statement']}" for id, s in prediction['statements used'].items()])
    message = [
        {"role": "system", "content": "You are an expert financial analyst."},
        {"role": "user", "content": f"{prompt}\n**Prediction Results**: {prediction['prediction']}\n**Facts Used**:\n{facts['facts']}\n**Statements Used**:\n{statements_used_text}\n**Actual Stock Movement**: {actual}"}
    ]
    response = get_gpt_response(message)
    refined, eliminated = parse_refine_response(response)
    return refined, eliminated
