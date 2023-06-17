from datetime import datetime
from custom_modules.exceptions.exceptions import InvalidTimeDuration, ZeroTimeDuration
from custom_modules.enums.enums import Duration

class WebsiteBlocker:
    def __init__(self):
        self.__website_list = []
        self.__duration = 0

    # Core methods
    def add_website(self, website, time_start=0, time_end=0):
        # returns true if website is successfully added
        if not self.search(website):
            self.block(website, time_start, time_end)
            self.__website_list.append(website)
            return True
        return False
    
    def size(self):
        # gets the size of the website list
        return len(self.__website_list)
    
    def display_websites(self):
        # display the blocked websites
        for website in self.__website_list:
            print(website)
            
    def search(self, website_in_question):
        # search if a website already exists
        for website in self.__website_list:
            if website is website_in_question:
                return True
        return False

    def block(self, website, time_start = None, time_end = None):
        # blocks a website and sets the calculated time duration
        self.set_duration(time_start, time_end)
        website.set_blocked_duration(self.__duration)
        self.__set_website_variables(website, time_start, time_end, True)

    def block_all(self, websites, time_start = None, time_end = None):
        # blocks all websites in the list
        self.set_websites(websites)
        for website in websites:
            self.block(website, time_start, time_end)

    def __set_website_variables(self, website, time_start = None, time_end = None, is_blocked_value = False):
        # set appropriate website varibales if they are to be blocked
        website.set_start_blocked_time(time_start)
        website.set_end_blocked_time(time_end)
        website.set_is_blocked(is_blocked_value)
        
    def __reset_website_variables(self, website):
        # reset website variables to their original states
        self.__set_website_variables(website)
    
    def unblock(self, website):
        # unblocks a website
        website.set_blocked_duration(Duration.NO_DURATION.value)
        self.__reset_website_variables(website)
        

    def unblock_all(self):
        # unblocks all websites in the list
        websites = self.__website_list
        for website in websites:
            self.unblock(website)
            
    # time operations
    def __convert_time(self, time):
        # converts the time to 00:00 AM/PM format
        time_format = "%I:%M %p"
        return datetime.strptime(time, time_format)
    
    def __calculate_duration(self, time_start, time_end):
        # returns the time difference from end time to start time
        time_start = self.__convert_time(time_start)
        time_end = self.__convert_time(time_end)
        
        time_difference = time_end - time_start
        return int(time_difference.total_seconds())
    
    def is_current_time(self, input_time):
        # check if the input time is equal to the current time
        now = datetime.now()
        time = self.__convert_time(input_time)
        return time == now

    # Setters
    def set_websites(self, websites):
        self.__website_list = websites
        
    def set_duration(self, time_start = None, time_end = None):
        # sets the blocked duration of the website
        duration = float("inf")
        
        if time_start is not None and time_end is not None:
            duration = self.__calculate_duration(time_start, time_end)
            if duration == 0:
                raise ZeroTimeDuration("Start time should not be equal to the end time. If you want to set an infinite duration, remove start and end time paramenters.")
            
        if duration < 0:
            raise InvalidTimeDuration("End time should be later than the start time.")
            
        self.__duration = duration

    # Getters
    def get_websites(self):
        return self.__website_list
    
    def get_duration(self):
        return self.__duration
    
    # to string
    def __str__(self):
        return f"There are {self.size()} websites blocked."
