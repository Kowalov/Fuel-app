class Calculator:
    def __init__(self, laptime, fuelxlap):
        self.laptime = sum(x * int(t) for x, t in zip([3600, 60, 1], laptime.split(":")))               #lap time in seconds
        self.fuelxlap = int(fuelxlap)                                                                   #fuel for one lap i liters

    def time_based(self, time):
        self.time = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))                     #race time in seconds
        self.lapsamount = self.time / self.laptime
        self.fuel = self.lapsamount * self.fuelxlap
        return self.fuel

    def laps_based(self, laps):
        self.laps = int(laps)                                                                            #Number of laps
        self.fuel = self.laps * self.fuelxlap
        return self.fuel

