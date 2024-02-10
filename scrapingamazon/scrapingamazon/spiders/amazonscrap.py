import scrapy
from scrapingamazon.items import tabletItem

class AmazonscrapSpider(scrapy.Spider):
    name = "amazonscrap"
    allowed_domains = ["amazon.com.tr"]
    start_urls = ["https://www.amazon.com.tr/s?k=iPads"]

    def parse(self, response):
        product_urls = response.css("a.a-link-normal::attr('href')")
        
        for product_url in product_urls:
            url = product_url.get()
            product_page = "https://www.amazon.com.tr" + url
            yield response.follow(url=product_page, callback=self.parse_product_page)
        
        
        next_url = response.css("li.a-last a::attr('href')").get()
        if next_url is not None:
            next_page = "https://www.amazon.com.tr" + next_url
            response.follow(url=next_page, callback=self.parse)

    def parse_product_page(self, response):
        tabletproduct = tabletItem()
        
        title = response.css("span#productTitle::text").get()
        price = response.css("span.a-price-whole::text").get()
        tabletproduct["title"] = title
        tabletproduct["price"] = price
        
        yield tabletproduct
        
