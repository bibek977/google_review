from file import Driver as review
from file import data
from images import Driver as image
from office_data import Driver as info
import json

api = {

}

api["Title"] = info.getTitle()
api["Name"] = info.getName()
api["Rating"] = info.getRating()
api["OfficeInfo"] = info.getOfficeData()
api["OfficeImages"] = image.getImages()
api["Reviews"] = data

with open("review.json",'w') as f:
    json.dump(api,f)
