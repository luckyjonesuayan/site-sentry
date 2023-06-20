from custom_modules.models.Website import Website
from custom_modules.models.WebsiteBlocker import WebsiteBlocker
from custom_modules.models.FileReader import FileReader

def main():
    # todo: backup folder to contain list of websites that were blocked for contingency
    # backup should contain the date
    # backup should be created everytime a website is blocked
    # todo: logcat for code tracing
    # make executable
    
    file_reader = FileReader()
    blocker = WebsiteBlocker()
    websites = file_reader.get_website_list()
    
    for website in websites:
        print(website)
        
    blocker.block_all(websites)
    
    for website in websites:
        print(website)
    
    
if __name__ == "__main__":
    main()