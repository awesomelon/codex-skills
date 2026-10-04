def label_for(code):
    return {"ground": "Ground", "pickup": "Pickup"}.get(code, "Unavailable")
