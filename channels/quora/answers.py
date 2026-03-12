def answer(question_id, text, **kwargs):
    print(f"[Quora Answer] Would answer question {question_id}: {text}")
    return {"platform": "quora", "type": "answer", "status": "stub"}
