from modules.models.WebsiteBlocker import WebsiteBlocker
from modules.models.FileProvider import FileProvider

def main():
    file_reader = FileProvider()
    blocker = WebsiteBlocker()
    websites = file_reader.get_website_list()
    
    blocker.block_all(websites)
    
if __name__ == "__main__":
    main()
