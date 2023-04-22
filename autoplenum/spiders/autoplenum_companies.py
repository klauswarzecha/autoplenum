import scrapy


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
        pass

