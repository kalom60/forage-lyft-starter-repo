from tire.tire import Tire


class OctoprimeTires(Tire):
    def __init__(self, array):
        self.array = array

    def needs_service(self):
        if sum(self.array) >= 3:
            return True
        return False