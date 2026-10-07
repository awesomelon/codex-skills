import json

def emit(job_id, token):
    return json.dumps({"id": job_id, "_ack": token})
