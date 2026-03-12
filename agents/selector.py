def choose_platforms(content):
    platforms = []

    if len(content) > 300:
        platforms += ["medium", "quora", "wordpress", "blogger"]

    if len(content) < 200:
        platforms += ["twitter", "instagram", "tiktok"]

    if "how to" in content.lower():
        platforms += ["quora"]

    return list(set(platforms))
