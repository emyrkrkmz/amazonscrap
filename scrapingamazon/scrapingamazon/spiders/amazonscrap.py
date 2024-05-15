from typing import Any
import scrapy
from scrapingamazon.items import Item#, asins


## ASIN => https://www.amazon.com.tr/dp/ASIN_CODE
class AmazonscrapSpider(scrapy.Spider):
    name = "amazonscrap"
    
    def start_requests(self):
        
        yield scrapy.Request(url="https://www.amazon.com.tr/samsung-s-pen/s?k=samsung+s+pen", callback=self.parse_asin)
        
    def parse_asin(self, response):
        
        
        products = response.xpath('//div[@data-asin != ""]/@data-asin')
        
        l = len(products)
        
        for i in range(l):
            asin = products[i].get()
            
            yield {
                'asin': asin
            }
        
 
