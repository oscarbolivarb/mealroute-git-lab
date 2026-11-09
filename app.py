from scheduler import build_route_summary
from notifications import build_driver_message
from inventory import low_stock_items
from config import DEFAULT_REGION

def main():
    route = build_route_summary("Friday", DEFAULT_REGION)
    print(route)
    print(build_driver_message("Amina", "Friday"))
    print("Low stock items:", ", ".join(low_stock_items()))

if __name__ == "__main__":
    main()
