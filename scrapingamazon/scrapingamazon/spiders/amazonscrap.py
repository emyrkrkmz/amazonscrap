import scrapy
from scrapingamazon.items import Item, asins
from multiprocessing import Pool


## ASIN => https://www.amazon.com.tr/dp/ASIN_CODE
class AmazonscrapSpider(scrapy.Spider):
    name = "amazonscrap"
    
    #def start_requests(self):
    #    
    #    yield scrapy.Request(url="https://www.amazon.com.tr/s?k=tablet", callback=self.parse_to_asin)
        
    def start_requests(self):
        for asin in asins:
            url = f'https://www.amazon.com.tr/dp/{asin}'
            yield scrapy.Request(url=url, callback=self.parse_asin, meta={'asin': asin})
        
        
    def parse_asin(self, response):
        #title = response.xpath('//span[@id="productTitle"]/text()').get()
        price = response.xpath('//div[@id="corePriceDisplay_desktop_feature_div"]//span[@class="a-price-whole"]/text()').get()
        #date = response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tbody/tr[3]/td/text()').get()
        
        # item = Item()
        # item['asin'] = response.meta['asin']
        # item['price'] = price
        # item['date'] = date
        
        
        if price is None:
            # Retry the request
            yield scrapy.Request(url=response.url, callback=self.parse_asin, meta=response.meta)
        else:
            yield {
                'asin': response.meta['asin'],
                'price': price,
            }
        
    
    
    
    def parse_to_asin(self, response):
        
        
        products = response.xpath('//div[@data-asin != ""]/@data-asin')
        
        l = len(products)
        
        for i in range(l):
            asin = products[i].get()
            
            yield {
                'asin': asin
            }
        
 
