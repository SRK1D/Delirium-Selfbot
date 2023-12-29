import requests
import re
import ressources.utils.randomizer as randomizer
import settings

class subreddit:
    def __init__(self, subreddit) -> None:
        self._subreddit = subreddit
        
    def getRandomImage(self, headers):
        content = requests.get(f"https://old.reddit.com/{self._subreddit}/new/", headers=headers, cookies={
            "over18": "1" # To go over the "Are you 18" check
        })
        images = re.findall(r'href="(https:\/\/i\.redd\.it\/.*?)"', content.content.decode()) # Find images :poggers:
        if images != None and len(images) != 0:
            return randomizer.Randomizer(list(images)).returnRandomWithOffset()
        else:
            settings.log("Warning", "[DELERIUM] Recursive call for reddit image parser...")
            try:
                return self.getRandomImage(headers)
            except:
                settings.log("Error", "[DELERIUM] Too many recursive calls for reddit")
                return "https://upload.wikimedia.org/wikipedia/commons/f/f7/Generic_error_message.png"
            
    def getRandomPost(self, headers):
        content = requests.get(f"https://old.reddit.com/{self._subreddit}/new/", headers=headers, cookies={
            "over18": "1" # To go over the "Are you 18" check
        })
        
        
        formatttedSubreddit = self._subreddit.replace("/", "\/")
        posts = ["https://old.reddit.com" + post for post in re.findall(rf'(?i)data-permalink="(\/{formatttedSubreddit}\/comments\/.*?\/.*?\/)"', content.content.decode())] # Find posts url
        if posts != None and len(posts) != 0:
            return randomizer.Randomizer(list(posts)).returnRandomWithOffset()
        else:
            settings.log("Warning", "[DELERIUM] Recursive call for reddit image parser...")
            try:
                return self.getRandomPost(headers)
            except:
                settings.log("Error", "[DELERIUM] Too many recursive calls for reddit")
                return "https://upload.wikimedia.org/wikipedia/commons/f/f7/Generic_error_message.png"
            
    def getContentFromPost(self, headers, postLink):
        content = requests.get(postLink, headers=headers, cookies={
            "over18": "1" # To go over the "Are you 18" check
        })
        
        if content.status_code != 200:
            return None
        
        titleOfPost = re.findall(r'property="og:title"\scontent="(.*?)">', content.content.decode()) # Gets the title
        descOfPost = re.findall(r'property="og:description"\scontent="(.*?)">', content.content.decode()) # Gets the description
        
        if (len(titleOfPost) + len(descOfPost)) >= 1:
            return {
                "Title": titleOfPost[0],
                "Description": descOfPost[0]
            }
        else:
            return None