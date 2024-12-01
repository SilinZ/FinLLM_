import os
from data_loader import load_transcripts, get_stock_prices, get_next_day_price_movement, price_movement_categories
from agents import agent_1_get_facts, agent_2_get_statements, store_statements_in_storage, agent_3_get_predictions, agent_4_get_feedback
from prompts import prompt_1, prompt_2, prompt_3, prompt_4
from tqdm import tqdm

import json
import openai

def run(dataset, prices, output_file="output/intermediate_results.jsonl"):
    dates = [t["time"] for t in dataset]
    movements = get_next_day_price_movement(prices, dates)
    labels = price_movement_categories(movements)
    storage = {}

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as file:
        for transcript in tqdm(dataset):
            date = transcript["time"]
            title = transcript["title"]
            facts = agent_1_get_facts(transcript, prompt_1)
            statements = agent_2_get_statements(facts, prompt_2)
            storage = store_statements_in_storage(statements, storage)
            prediction = agent_3_get_predictions(facts, storage, prompt_3)
            actual = labels.get(date, "Unknown")
            refined, eliminated = agent_4_get_feedback(facts, prediction, actual, prompt_4)

            # Update storage
            for id, statement in refined.items():
                if id in storage:
                    storage[id]['statement'] = statement
            for id in eliminated:
                storage.pop(id, None)

            # Log data
            log_data = {
                "title": title,
                "date": date,
                "facts": facts,
                "statements": statements,
                "prediction": prediction,
                "storage_snapshot": storage.copy(),
                "stats": {
                    "statements_generated": len(statements),
                    "statements_in_storage": len(storage),
                    "statements_used": len(prediction["statements used"]),
                    "refined_statements": list(refined.keys()),
                    "eliminated_statements": list(eliminated.keys()),
                },
                "actual_movement": actual
            }
            file.write(json.dumps(log_data) + "\n")

            # Optional: Print progress
            print(f"At {date}, predicted: {prediction['prediction']}, actual: {actual}")
            print(f"Statements generated: {len(statements)}, used: {len(prediction['statements used'])}")
            print(f"Refined statements: {list(refined.keys())}, eliminated: {list(eliminated.keys())}")
            print(f"Total statements in storage: {len(storage)}")
            print("---" * 10)

if __name__ == "__main__":
    dataset = load_transcripts("data/goog_calls.jsonl")
    symbol = 'GOOG'
    start_date = '2014-11-01'
    end_date = '2024-11-01'
    prices = get_stock_prices(symbol, start_date, end_date)

    output_file = "output/goog_intermediate_results.jsonl"
    run(dataset, prices, output_file)
