import logging
import scrapy
from ..items import AutoplenumItem
from scrapy.loader import ItemLoader


class AutoplenumCompaniesSpider(scrapy.Spider):
    name = "autoplenum_companies"
    allowed_domains = ["autoplenum.de"]
    start_urls = [
        'https://www.autoplenum.de/autohaus/bardowick/frs-autotechnik-gmbh-78360', 
        'https://www.autoplenum.de/autohaus/bremen/carpoint-107081', 
        'https://www.autoplenum.de/autohaus/bad-soden/autohaus-lanz-gmbh-17860', 
        'https://www.autoplenum.de/autoteile/dortmund/ersatzteillager-tengert-118762', 
        'https://www.autoplenum.de/autoteile/gelsenkirchen/s-b-autoteile-und-lacke-gmbh-co-kg-22800', 
        'https://www.autoplenum.de/kfz-werkstatt/alzenau/otto-rosenberger-4172', 
        'https://www.autoplenum.de/kfz-werkstatt/ibbenbueren/vergoelst-gmbh-120735', 
        'https://www.autoplenum.de/kfz-werkstatt/soest/christian-huelsmann-70552', 
        'https://www.autoplenum.de/waschanlage/berlin/cosi-wasch-gmbh-119162', 
        'https://www.autoplenum.de/waschanlage/berlin/autoreinigung-berlin-122180', 
        'https://www.autoplenum.de/waschanlage/berlin/jet-waschboxen-118137'
    ]

    def parse(self, response):
        loader = ItemLoader(item=AutoplenumItem())
        companyname = response.xpath(
            '//section[@id="header"]//h1[@itemprop="name"]/text()'
        ).get()
        loader.add_value('companyname', companyname)
        contact = response.xpath('//section[@id="contact"]')
        address = contact.xpath('.//div[@itemprop="address"]')
        street = address.xpath(
            './span[@itemprop="streetAddress"]/text()'
        ).get()
        loader.add_value('street', street)
        postalcode = address.xpath(
            './span[@itemprop="postalCode"]/text()'
        ).get()
        loader.add_value('postalcode', postalcode)
        locality = address.xpath(
            './span[@itemprop="addressLocality"]/text()'
        ).get()
        loader.add_value('locality', locality)

        geo = contact.xpath('.//span[@itemprop="geo"]')
        latitude = geo.xpath(
            './meta[@itemprop="latitude"]/@content'
        ).get()
        loader.add_value('latitude', latitude)
        longitude = geo.xpath(
            './meta[@itemprop="longitude"]/@content'
        ).get()
        loader.add_value('longitude', longitude)



        reviews = response.xpath(
            '//section[@id="reviews"]/h2[@itemprop="aggregateRating"]'
        )
        review_count = reviews.xpath(
            './span[@itemprop="reviewCount"]/@content'
        ).get()
        loader.add_value('review_count', review_count)
        rating_count = reviews.xpath(
            './span[@itemprop="reviewCount"]/@content'
        ).get()
        loader.add_value('rating_count', rating_count)
        rating_average = reviews.xpath(
            './span[@itemprop="ratingValue"]/@content'
        ).get()
        loader.add_value('rating_average', rating_average)

        item = loader.load_item()
    
        yield item