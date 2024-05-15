# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import pandas as pd

#asins = pd.read_csv('asins.csv')

class Item(scrapy.Item):
    asin = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()