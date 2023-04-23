# Define here the models for your scraped items
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class AutoplenumItem(scrapy.Item):
    companyname = Field()
    street = Field()
    postalcode = Field()
    locality = Field()

    phone = Field()
    fax = Field()
    website = Field()
    
    services = Field()

    review_count = Field()
    rating_count = Field()
    rating_average = Field()
