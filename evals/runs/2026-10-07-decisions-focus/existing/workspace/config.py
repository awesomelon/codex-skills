def read_timeout(config):
    return config.get("timeout_seconds", config.get("timeout", 30))
