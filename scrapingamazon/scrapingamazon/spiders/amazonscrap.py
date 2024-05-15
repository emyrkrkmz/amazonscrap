import scrapy
from scrapingamazon.items import Item, asins


## ASIN => https://www.amazon.com.tr/dp/ASIN_CODE
class AmazonscrapSpider(scrapy.Spider):
    name = "amazonscrap"
    
    #def start_requests(self):
    #    
    #    yield scrapy.Request(url="https://www.amazon.com.tr/s?k=tablet", callback=self.parse_to_asin)
        
    def start_requests(self):
        for asin in asins:
            url = f'https://www.amazon.com.tr/dp/{asin}'
            yield scrapy.Request(url=url, callback=self.parse_asin)
        
        
    def parse_asin(self, response):
        title = response.xpath('//span[@id="productTitle"]/text()').get()
        
        yield {
            'title': title
        }
        
        
    
    
    
    def parse_to_asin(self, response):
        
        
        products = response.xpath('//div[@data-asin != ""]/@data-asin')
        
        l = len(products)
        
        for i in range(l):
            asin = products[i].get()
            
            yield {
                'asin': asin
            }
        
 
