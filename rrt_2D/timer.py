import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0.0

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()
        self.elapsed_time = round(self.end_time - self.start_time, 4)
        

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0.0

    def __str__(self):
        return f'Elapsed time: {round(self.elapsed_time, 4)} seconds'