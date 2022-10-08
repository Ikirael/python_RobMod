import time

class MyTimer:
    def __init__(self, units):
            self.units = units

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.spent_time = self.end_time - self.start_time

    def elapsed_time(self):
        if self.units == "s":
            return round(self.spent_time,1)
        if self.units == "m":
            return self.spent_time/60
        if self.units == "h":
            return self.spent_time/3600
        else:
            print("Wrong name of time")
            return 0


print("Countdown has started...")
with MyTimer(units="z") as t:
    time.sleep(5)
print(t.elapsed_time())