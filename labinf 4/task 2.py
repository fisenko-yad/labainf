import json
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    total_sum = 0.0
    for item in data:
        score = item["score"]
        weight = item["weight"]
        total_sum += score * weight
    return round(total_sum, 3)
if __name__ == "__main__":
    print(task())