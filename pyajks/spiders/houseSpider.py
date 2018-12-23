import scrapy
import re
from scrapy.http import Request
from pyajks.items import PyajksItem

class houseSpider(scrapy.Spider):
    name = "anjuke"
    allowed_domains = ["jinan.anjuke.com"]
    start_urls = ['https://jinan.anjuke.com/sale/licheng/p1']

    def parse(self, response):

        post_nodes = response.xpath('//div[@class="house-title"]').css('a::attr(href)').extract()
        print ("url"+post_nodes[0])
        yield Request(url=post_nodes[0],callback=self.parse_detail)
        # for post_node in post_nodes:
        #     post_url = post_node
        #     yield Request(url=post_url,callback=self.parse_detail)

        #提取下一页并交给scrapy下载
        # next_url = response.xpath('//div[@class="multi-page"]').css(".aNxt::attr(href)").extract_first("")
        # print ("next_url",next_url)
        # if next_url:
        #     yield Request(url=next_url,callback=self.parse)

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
        time = preTime.split("：",1)[1]
        print ("time : "+time)
        house_item["time"] = time

        houseMeta = houseInfo.xpath('//li[@class="houseInfo-detail-item"]')
        print ("houseMeta"+houseMeta)
        # 小区
        preXiaoqu = houseMeta[0].xpath('//div[@class="houseInfo-content"]/a/text()').extract_first()
        print ("小区"+preXiaoqu)
        xiaoqu= preXiaoqu
        house_item["xiaoqu"] = xiaoqu
        # 房屋户型
        preRoomType = houseMeta[1].xpath('//div[@class="houseInfo-content"]/text()').extract_first("")
        print ("房屋户型"+preRoomType)
        roomType= preRoomType.replace("\n","").replace(" ","")
        print ("房屋户型:"+roomType)
        house_item["roomType"] = roomType
        # 单价
        preUnitPrice = houseMeta[2].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        unitPrice = re.findall("\d+",preUnitPrice)[0]
        house_item["unitPrice"] = unitPrice

        # 位置
        preLocation = houseMeta[3].xpath('//div[@class="houseInfo-content"]/p[@class="loc-text"]/text()').extract_first()
        location = preLocation
        house_item["location"] = location
        # 房屋面积
        houseArea = houseMeta[4].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseArea"] = houseArea

        # 建造年代
        buildYear = houseMeta[6].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["buildYear"] = buildYear
        # 房屋类型
        houseType = houseMeta[9].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseType"] = houseType
        # 产权年限
        houseYeatLimit = houseMeta[12].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["houseYeatLimit"] = houseYeatLimit
        # 楼层
        floor = houseMeta[10].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["floor"] = floor
        # 参考首付
        firstPay = houseMeta[5].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["firstPay"] = firstPay
        # 参考月供
        MPay = houseMeta[8].xpath('//div[@class="houseInfo-content"]/text()').extract_first()
        house_item["MPay"] = MPay
        # 户型图
        roomTypeImgUrl = scrapy.Field()
        # url
        url = scrapy.Field()

        yield house_item