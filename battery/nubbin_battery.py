from battery.battery import Battery
from helper import curr_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        should_be_serviced = curr_date(self.last_service_date, 4)
        if should_be_serviced < self.current_date:
            return True
        return False
