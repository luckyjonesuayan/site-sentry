from custom_modules.models.Website import Website
from custom_modules.models.WebsiteBlocker import WebsiteBlocker

def main():
    # TODO: should be able to read a text file that contains the websites to be blocked
    # TODO: scheduler
    # TODO: unblock if today's time is equal to the end time
    # TODO: os and/or browser operations
    
    blocker = WebsiteBlocker()
    s1 = Website("facebook.com")
    s2 = Website("youtube.com")
    s3 = Website("twitter.com")
    s4 = Website("instagram.com")
    
    websites = [s1, s2, s3]
    blocker.block_all(websites)
    blocker.display_websites()
    
    print("----UNBLOCKED")
    blocker.unblock_all()
    blocker.display_websites()
    
    print("----SINGLE WEBSITE")
    blocker.block(s4)
    print(s4)
    
    print("----WITH TIME SET")
    blocker.block(s4, "10:30 AM", "10:31 AM")
    print(s4)
    
    print("----UNBLOCK")
    blocker.unblock(s4)
    print(s4)
    
    
if __name__ == "__main__":
    main()