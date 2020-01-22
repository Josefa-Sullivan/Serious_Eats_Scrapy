# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SeriousEatsItem(scrapy.Item):
    topic= scrapy.Field()
    subtopic = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    photographer = scrapy.Field()
    link = scrapy.Field()
    pub_date = scrapy.Field()
    servings = scrapy.Field()
    active_time = scrapy.Field()
    total_time = scrapy.Field()
    rating = scrapy.Field()
    ingredients = scrapy.Field()
    directions = scrapy.Field()
