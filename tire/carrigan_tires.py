from tire.tire import Tire


class CarriganTires(Tire):
    def __init__(self, array):
        self.array = array

    def needs_service(self):
        if any(x >= 0.9 for x in self.array):
            return True
        return False