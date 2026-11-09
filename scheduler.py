from config import DEFAULT_STOP_LIMIT, DEFAULT_REGION

def build_route_summary(day, region=DEFAULT_REGION):
    stops = DEFAULT_STOP_LIMIT
    return f"MealRoute schedule for {day} in {region}: {stops} delivery stops planned."

def can_add_stop(current_stop_count):
    return current_stop_count < DEFAULT_STOP_LIMIT

def route_label(day):
    return f"{day}-community-route"
