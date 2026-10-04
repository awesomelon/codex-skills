LABELS = {"basic": "Basic", "pro": "Pro"}


def label_for(plan):
    return LABELS.get(plan, "Unknown")
