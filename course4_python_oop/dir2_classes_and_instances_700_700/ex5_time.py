class Time:
    max_hours, max_minutes, max_seconds = 23, 59, 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds >= self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= self.max_hours:
                    self.hours = 0

        return self.get_time()
