# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 定义了 Scrapy 项目中的数据模型（Items），用于结构化存储爬取的数据
import scrapy


# 这是一个空的 Item 类，可能作为基类预留，供其他 Item 类继承，或在项目初期创建，后续被填充字段。
class Myscrapy02Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 与用户提供的视频信息数据完全匹配，用于存储视频相关字段
class MyscrapyItem(scrapy.Item):
    img_url = scrapy.Field()  # 视频封面图
    desc = scrapy.Field()  # 视频描述
    title = scrapy.Field()  # 视频标题
    play_num = scrapy.Field()  # 播放量
    like_num = scrapy.Field()  # 点赞量
    id = scrapy.Field()  # 唯一视频标识


# ：用于存储视频播放相关信息
class FilmPlayItem(scrapy.Item):
    id = scrapy.Field()  # 关联视频的唯一标识
    url_best = scrapy.Field()  # 最优播放地址


# 存储视频评论信息
class FilmCommentItem(scrapy.Item):
    id = scrapy.Field()  # 关联视频的唯一标识
    content = scrapy.Field()
