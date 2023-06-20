from custom_modules.models.Website import Website
from custom_modules.models.WebsiteBlocker import WebsiteBlocker
from custom_modules.models.FileReader import FileReader

def main():
    file_reader = FileReader()
    blocker = WebsiteBlocker()
    websites = file_reader.get_website_list()
    
    for website in websites:
        print(website)
    
    
if __name__ == "__main__":
    main()