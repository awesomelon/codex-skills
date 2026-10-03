CACHE = {}

def read_record(tenant, record_id, load):
    key = (tenant, record_id)
    if key not in CACHE:
        CACHE[key] = load(tenant, record_id)
    return CACHE[key]
