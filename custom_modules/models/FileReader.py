from custom_modules.models.Website import Website

class FileReader:
    def __init__(self):
        self._websites = []
        return
    
    def __read_webiste_list(self):
        # reads the file website_list.txt and returns an array of websites that were separated by a new line
        try:
            with open("website_list.txt", "r") as file:
                contents = file.read()
                return contents.splitlines()
        except:
            # todo: generate website_list if it does not exist
            return []
            
        
    def get_website_list(self):
        # get the websites from external file and convert it to Website object
        websites_str = self.__read_webiste_list()
        for website in websites_str:
            self._websites.append(Website(website))
        return self._websites
    
    def generate_initial_website_list(self):
        return
    
    def _is_txt_comment(self):
        return
    
    def _is_config_comment(self):
        return
    
        