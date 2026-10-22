
from fastapi import FastAPI
from pydantic import BaseModel
from collections import Counter

app = FastAPI(title="Big Small AI Analysis Tool")

class Results(BaseModel):
    numbers: list[int]

@app.get("/")
def home():
    return {
        "message": "Big Small Analysis API is running!",
        "status": "success"
    }

@app.post("/analyze")
def analyze(data: Results):
    if not data.numbers:
        return {"error": "Please enter some numbers"}

    big = sum(1 for n in data.numbers if n >= 5)
    small = sum(1 for n in data.numbers if n < 5)

    return {
        "total_results": len(data.numbers),
        "big_count": big,
        "small_count": small,
        "most_common_numbers": Counter(data.numbers).most_common(3),
        "note": "Past results analysis only; next result is not guaranteed."
    }
