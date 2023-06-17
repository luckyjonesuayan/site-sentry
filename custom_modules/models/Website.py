import math

class Website:
    def __init__(self, url, is_blocked = False):
        self.__url = url
        self.__is_blocked = is_blocked
        self.__blocked_duration = 0
        self.__start_blocked_time =  None
        self.__end_blocked_time = None
    
    # setters
    def set_url(self, url):
        self.__url = url
    
    def set_is_blocked(self, bool_val):
        self.__is_blocked = bool_val
        
    def set_blocked_duration(self, duration):
        self.__blocked_duration = duration
        
    def set_start_blocked_time(self, time_start):
        self.__start_blocked_time = time_start
        
    def set_end_blocked_time(self, time_end):
        self.__end_blocked_time = time_end
        
    # getters
    def get_url(self):
        return self.__url
    
    def get_is_blocked(self):
        return self.__is_blocked
    
    def get_blocked_duration(self):
        return self.__blocked_duration
        
    def get_start_blocked_time(self):
        return self.__start_blocked_time
        
    def get_end_blocked_time(self):
        return self.__end_blocked_time
    
    # object's str
    def __str__(self):
        duration_txt = f"{self.__blocked_duration} secs OR {self.__blocked_duration/60} min/s\nSTART BLOCKED TIME: {self.__start_blocked_time}\nEND BLOCKED TIME: {self.__end_blocked_time}\n" if self.__is_blocked else "0\n"
        if (math.isinf(self.__blocked_duration)):
            duration_txt = "Infinite\n"
        return f"Website URL: {self.__url}\nBLOCKED: {self.__is_blocked}\nBLOCKED DURATION: {duration_txt}" 