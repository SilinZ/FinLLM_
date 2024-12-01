import json

def check_response(path):
    with open(path, "r") as f:
        data = [json.loads(line) for line in f]
    return data

if __name__ == "__main__":
    output_file = "output/goog_intermediate_results.jsonl"
    results = check_response(output_file)
    # You can add code here to analyze or display the results
    print(results)
