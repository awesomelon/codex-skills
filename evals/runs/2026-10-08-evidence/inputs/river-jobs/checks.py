import json
from producer import emit

assert json.loads(emit("job-1", "token-1"))["id"] == "job-1"
print("Producer ID check passed")
