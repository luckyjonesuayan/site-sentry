import tldextract
from urllib.parse import urlparse
from modules.models.Website import Website

class FileProvider:
    def __init__(self):
        self._websites = []
        return
    
    # public
    def get_website_list(self):
        # get the websites from external file and convert it to Website object
        websites_str = self._website_list()
        for website in websites_str:
            if self._is_valid_url(website) or self._is_valid_domain_name(website):
                # only append the website if its a valid url or domain
                self._websites.append(Website(website))
        return self._websites
    
    # private
    # helper functions
    def _website_list(self):
        # returns the website list contents
        try:
            return self._read_website_list()
        except:
            # generates the initial website_list.txt file if it does not exist and return an empty array to indicate that no website is added yet.
            self._generate_initial_website_list()
            return []
            
    def _read_website_list(self):
        # reads the file website_list.txt and returns an array of websites that were separated by a new line
        with open("website_list.txt", "r") as file:
            contents = file.read()
            return contents.splitlines()
        
    # validators
    def _is_valid_url(self, url):
        # check if valid url
        parsed_url = urlparse(url)
        return all([parsed_url.scheme, parsed_url.netloc])
    
    def _is_valid_domain_name(self, domain):
        # check if the content is a valid domain
        extracted = tldextract.extract(domain)
        return all([extracted.domain, extracted.suffix])
    
    def _get_time_duration_str(self):
        with open("website_list.txt", "r") as file:
            time_str = file.read()
            return
        
    # generators
    def _generate_initial_website_list(self):
        # generate the initial website list
        with open("website_list.txt", "w") as file:
            file.write("# WEBSITE LIST - List the websites you want to be blocked below this line:\n\n")
    
    def _generate_initial_config(self):
        return    