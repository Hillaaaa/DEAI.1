def profile_analyser(profile):
    total_connections = profile.get("followers",0) + profile.get("following",0)
    if profile.get("followers",0) >= 100:
        popularity = "high"
    else:
        popularity = "low"
    return {
        "username": profile.get("username", "doesn't exist"),
        "total_connections": total_connections,
        "popularity": popularity,
    }
profile = {
    "username": "hillary",
    "posts": 34,
    "followers": 120,
    "following": 80
}
print(profile_analyser(profile))
