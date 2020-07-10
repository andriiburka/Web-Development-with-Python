# ```py
class Time:
    max_hours, max_minutes, max_seconds = 23, 59, 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        # return v1.0
        # if len(str(self.hours)) == 1:
        #     self.hours = f"{0}{self.hours}"
        # if len(str(self.minutes)) == 1:
        #     self.minutes = f"{0}{self.minutes}"
        # if len(str(self.seconds)) == 1:
        #     self.seconds = f"{0}{self.seconds}"
        # return f"{self.hours}:{self.minutes}:{self.seconds}"

        # return sexy v2.0
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
# ```


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
