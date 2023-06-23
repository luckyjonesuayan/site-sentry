import math

class Website:
    def __init__(self, url, is_blocked = False):
        self._url = url
        self._is_blocked = is_blocked
        self._blocked_duration = 0
        self._start_blocked_time =  None
        self._end_blocked_time = None
    
    # setters
    def set_url(self, url):
        self._url = url
    
    def set_is_blocked(self, bool_val):
        self._is_blocked = bool_val
        
    def set_blocked_duration(self, duration):
        self._blocked_duration = duration
        
    def set_start_blocked_time(self, time_start):
        self._start_blocked_time = time_start
        
    def set_end_blocked_time(self, time_end):
        self._end_blocked_time = time_end
        
    # getters
    def get_url(self):
        return self._url
    
    def get_is_blocked(self):
        return self._is_blocked
    
    def get_blocked_duration(self):
        return self._blocked_duration
        
    def get_start_blocked_time(self):
        return self._start_blocked_time
        
    def get_end_blocked_time(self):
        return self._end_blocked_time
    
    # object's str
    def __str__(self):
        duration_txt = f"{self._blocked_duration} secs OR {self._blocked_duration/60} min/s\nSTART BLOCKED TIME: {self._start_blocked_time}\nEND BLOCKED TIME: {self._end_blocked_time}\n" if self._is_blocked else "0\n"
        if (math.isinf(self._blocked_duration)):
            duration_txt = "Infinite\n"
        return f"Website URL: {self._url}\nBLOCKED: {self._is_blocked}\nBLOCKED DURATION: {duration_txt}"