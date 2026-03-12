def post_to_space(space_name, text, **kwargs):
    print(f"[Quora Space] Would post to space '{space_name}': {text}")
    return {"platform": "quora", "type": "space", "status": "stub"}
