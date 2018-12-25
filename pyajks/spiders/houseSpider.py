import scrapy
import re
from scrapy.http import Request
from pyajks.items import PyajksItem
import time
import datetime

class houseSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["jinan.anjuke.com"]
    start_urls = ['https://jinan.anjuke.com/sale/licheng/p1']

    def parse(self, response):

        post_nodes = response.xpath('//div[@class="house-title"]').css('a::attr(href)').extract()
        # print ("url"+post_nodes[0])
        # yield Request(url=post_nodes[0],callback=self.parse_detail)
        for post_node in post_nodes:
            post_url = post_node
            time.sleep(2)
            yield Request(url=post_url,callback=self.parse_detail)

        #提取下一页并交给scrapy下载
        next_url = response.xpath('//div[@class="multi-page"]').css(".aNxt::attr(href)").extract_first("")
        print ("next_url",next_url)
        if next_url:
            yield Request(url=next_url,callback=self.parse)

    def parse_detail(self,response):
        '''
        获取房子的详细内容
        :param response:
        :return:
        '''
        print ("#################### detail ####################")
        house_item = PyajksItem()
        title = response.xpath('//h3[@class="long-title"]/text()').extract_first("")
        title = title.replace("\n","")
        print ("title : "+title)
        house_item["title"] = title

        houseInfo = response.xpath('//div[@class="houseInfoBox"]')
        # 房屋编号
        preHouseNo = houseInfo.xpath('//span[@class="house-encode"]/span[@id="houseCode"]/text()').extract_first()
        houseNo = re.findall("\d+",preHouseNo)[0]
        print ("houseNo : "+houseNo)
        house_item["houseNo"] = houseNo
        # 发布时间
        preTime = houseInfo.xpath('//span[@class="house-encode"]/text()').extract_first()
        times = preTime.split("：",1)[1]
        print ("time : "+times)
        house_item["time"] = times

        houseMeta = houseInfo.xpath('//li[@class="houseInfo-detail-item"][2]//div[@class="houseInfo-content"]/text()').extract()
        print ("-------"+houseMeta[0])
        # 小区
        preXiaoqu = houseInfo.xpath('//li[@class="houseInfo-detail-item"][1]').xpath('//div[@class="houseInfo-content"]/a/text()').extract_first()
        print ("小区"+preXiaoqu)
        xiaoqu= preXiaoqu
        house_item["xiaoqu"] = xiaoqu
        # 房屋户型
        preRoomType = houseInfo.xpath('//li[@class="houseInfo-detail-item"][2]//div[@class="houseInfo-content"]/text()').extract_first()
        preRoomType = preRoomType.replace("\n","")
        roomType = preRoomType.replace('	','')
        print ("房屋户型:"+roomType)
        house_item["roomType"] = roomType
        # 单价
        preUnitPrice = houseInfo.xpath('//li[@class="houseInfo-detail-item"][3]//div[@class="houseInfo-content"]/text()').extract_first()
        unitPrice = re.findall("\d+",preUnitPrice)[0]
        print ("unitPrice:"+unitPrice)
        house_item["unitPrice"] = unitPrice

        # 位置
        preLocation = houseInfo.xpath('//li[@class="houseInfo-detail-item"][4]//div[@class="houseInfo-content"]/p[@class="loc-text"]/text()').extract_first()
        location = preLocation
        print ("location:"+location)
        house_item["location"] = location
        # 房屋面积
        houseArea = houseInfo.xpath('//li[@class="houseInfo-detail-item"][5]//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseArea"] = houseArea
        print (houseArea)
        # 建造年代
        buildYear = houseInfo.xpath('//li[@class="houseInfo-detail-item"][7]//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["buildYear"] = buildYear
        # 房屋类型
        houseType = houseInfo.xpath('//li[@class="houseInfo-detail-item"][10]//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseType"] = houseType
        # 产权年限
        houseYearLimit = houseInfo.xpath('//li[@class="houseInfo-detail-item"][13]//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseYearLimit"] = houseYearLimit
        # 楼层
        floor = houseInfo.xpath('//li[@class="houseInfo-detail-item"][11]//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["floor"] = floor
        # 参考首付
        firstPay = houseInfo.xpath('//li[@class="houseInfo-detail-item"][6]//div[@class="houseInfo-content"]/text()').extract_first()
        firstPay.replace(" ","").replace("\t","")
        house_item["firstPay"] = firstPay
        # 参考月供
        MPay = houseInfo.xpath('//li[@class="houseInfo-detail-item"][9]//div[@class="houseInfo-content"]/span/text()').extract_first()
        house_item["MPay"] = MPay
        # 户型图
        roomTypeImgUrl = scrapy.Field()

        # url
        house_item["url"] = response.url
        # nowTime
        datetime.date.today()
        nowTime =  int(time.mktime(time.strptime(str(datetime.date.today()), '%Y-%m-%d')))
        house_item["nowTime"] = nowTime


        yield house_item