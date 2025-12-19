import json
import random
from datetime import datetime

EVENT_TYPES = ["page_view", "add_to_cart", "checkout"]
PAGES = ["/home", "/product", "/cart", "/checkout"]

def generate_event():
	return {
		"user_id" : random.randint(1,100),
		"event_type" : random.choice(EVENT_TYPES),
		"page" : random.choice(PAGES),
		"event_timestamp" : datetime.utcnow().isoformat()
		}
if __name__ == "__main__":
    with open("data/events.json", "w") as f:
        for _ in range(100):
            event = generate_event()
            f.write(json.dumps(event) + "\n")

    print("Clickstream events generated (NDJSON format)")
