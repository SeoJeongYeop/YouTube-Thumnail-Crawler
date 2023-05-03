# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import *
import pymysql

import sys
import regex as re

from .secret import *

# emoji_filter = re.compile("["u"\U00010000-\U0010FFFF""]+", flags=re.UNICODE)

class YtCrawlerPipeline:
    def process_item(self, item, spider):
        
        if type(item) == YoutubeChannelItem :
            # 채널명과 설명에서 이모지 제거
            # item['title'] = emoji_filter.sub(r'', item['title'])
            # item['description'] = emoji_filter.sub(r'', item['description'])

            insert_sql = '''INSERT INTO channel(channel_id, title, description, published_at, view_count, subscriber_count, video_count, country, crawled_at, period_day) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            
            insert_arg = [item['channel_id'], item['title'], item['description'], 
                          item['published_at'], item['view_count'], item['subscriber_count'], item['video_count'], item['country'], item['crawled_at'], item['period_day']]

        try :
            self.cursor.execute(insert_sql, insert_arg)
            self.crawlDB.commit()
        except:
            print(insert_sql, insert_arg)
            sys.exit(1)
        return item


    def __init__(self):
        try :
            self.crawlDB = pymysql.connect(
                user=SQL_USER,
                passwd=SQL_PW,
                host=SQL_HOST,
                port=SQL_PORT,
                db=SQL_DB
            )
            self.cursor = self.crawlDB.cursor()
        except :
            print('ERROR: DB connection failed')
            sys.exit(1)
