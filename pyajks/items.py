# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PyajksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房屋编码
    houseNo = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 单价
    unitPrice = scrapy.Field()
    # 小区
    xiaoqu= scrapy.Field()
    # 位置
    location= scrapy.Field()
    # 建造年代
    buildYear= scrapy.Field()
    # 房屋类型
    houseType = scrapy.Field()
    # 产权年限
    houseYeatLimit = scrapy.Field()
    # 房屋户型
    roomType = scrapy.Field()
    # 房屋面积
    houseArea = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 参考首付
    firstPay = scrapy.Field()
    # 参考月供
    MPay = scrapy.Field()
    # 户型
    roomTypeImgUrl = scrapy.Field()
    # url
    url = scrapy.Field()
    pass
