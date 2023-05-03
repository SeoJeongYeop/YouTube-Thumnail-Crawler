# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YtCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class YoutubeVideoItem(scrapy.Item) :
    video_id = scrapy.Field()
    channelId = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    period = scrapy.Field()
    view = scrapy.Field()
    like = scrapy.Field()
    thumnail_low = scrapy.Field()
    thumnail_medium = scrapy.Field()
    thumnail_high = scrapy.Field()
    
    

class YoutubeChannelItem(scrapy.Item) :
    channel_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    published_at = scrapy.Field()
    view_count = scrapy.Field()
    subscriber_count = scrapy.Field()
    video_count = scrapy.Field()
    country = scrapy.Field()
    crawled_at = scrapy.Field()
    period_day = scrapy.Field()
