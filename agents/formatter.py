def format_for_platform(platform, content):
    if platform == "quora":
        return {"action": "post", "payload": {"text": content}}

    if platform == "medium":
        return {"action": "post", "payload": {"text": content}}

    if platform == "twitter":
        return {"action": "post", "payload": {"text": content[:280]}}

    return {"action": "post", "payload": {"text": content}}
