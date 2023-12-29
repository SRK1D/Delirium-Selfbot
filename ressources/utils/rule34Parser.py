import ressources.utils.randomizer as randomizer
from random import randint
import requests
import settings

endpointURL = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={}&json=1&limit=1000&pid={}"

def tagParser(tableOfTags):
    rule34JSON = []
    for tagsString in tableOfTags:
        rule34JSON.append('+' + tagsString)
    return ''.join(rule34JSON)

def fromVJSONResultToValidContentURL(vJSON):
    # $- Check for edge cases, handles different sized 
    contentLinks = []
    for individualImage in vJSON:
        fileURL = individualImage['file_url']
        if fileURL == 'https://api-cdn.rule34.xxx/images//':
            pass

        contentLinks.append({
            'width': individualImage['width'],
            'height': individualImage['height'],
            'tags': individualImage['tags'],
            'fileurl': fileURL,
            'image': individualImage['image']
        })

    return contentLinks

class r34:
    def __init__(self, tags) -> None:
        self._tags = tags
        pass

    def getRandomImage(self):
        pID = randint(0, 15)
        contentReq = requests.get(endpointURL.format(self._tags, pID))
        if '<response success="false"' in contentReq.content.decode():
            settings.log("Warning", "[DELERIUM] Recursive call for reddit image parser...")
            try:
                return self.getRandomImage(self)
            except:
                settings.log("Error", "[DELERIUM] Too many recursive calls for reddit")
                return
        else:
            return randomizer.Randomizer(fromVJSONResultToValidContentURL(contentReq.json())).returnRandomWithOffset()["fileurl"]