from config import DRIVER_MESSAGE_PREFIX

def build_driver_message(driver_name, day):
    return f"{DRIVER_MESSAGE_PREFIX} {driver_name}. Your delivery route for {day} is ready."

def build_site_message(site_name):
    return f"Site update: {site_name} will receive its next meal drop during the scheduled route window."
