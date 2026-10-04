QUOTAS = {"basic": 5, "pro": 10}


def quota_for(plan):
    return QUOTAS.get(plan, 0)
