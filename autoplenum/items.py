# Define here the models for your scraped items
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy.item import Field
from itemloaders.processors import Compose, MapCompose, TakeFirst

class AutoplenumItem(Item):
    

    companyname = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )
    street = Field(
        output_processor=Compose(
            TakeFirst(), str, str.strip, lambda x: x.strip(',')
        )
    )
    postalcode = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )
    locality = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )

    phone = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )
    fax = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )
    website = Field(
        output_processor=Compose(TakeFirst(), str.strip)
    )
    
    services = Field(
        output_processor=Compose(TakeFirst(), lambda x: x.split(','))
    )

    review_count = Field(
        output_processor=Compose(TakeFirst(), int)
    )
    rating_count = Field(
        output_processor=Compose(TakeFirst(), int)
    )
    rating_average = Field(
     output_processor=Compose(TakeFirst(), float)
    )
    latitude = Field(
        output_processor=Compose(TakeFirst(), float)
    )
    longitude = Field(
        output_processor=Compose(TakeFirst(), float)
    )