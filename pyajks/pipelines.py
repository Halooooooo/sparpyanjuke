# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PyajksPipeline(object):


    def process_item(self, item, spider):
        db = pymysql.connect(host="140.143.225.104",user="root",
                             password="DH5300dh",db="anjuke-jinan",port=3306)
        cur = db.cursor()

        sql_insert ="""insert into licheng(house_no,p_time, title, unit_price, xiaoqu, location, build_year,
            house_type, house_year_limit, room_type, house_area, floor, first_pay, m_pay, room_type_img_url, url, now_time
            ) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
        try:
            cur.execute(sql_insert % (item['houseNo'],item['time'],item['title'],item['unitPrice'],item['xiaoqu'],item['location'],
                                  item['buildYear'],item['houseType'],item['houseYearLimit'],item['roomType'],item['houseArea']
                                  ,item['floor'],item['firstPay'],item['MPay'],'',item['url'],item['nowTime']))
            db.commit()
            print ("*********************************************************")
        except Exception as e:
            #错误回滚
            print ('str(e):'+str(e))
            print ('repr(e):'+repr(e))
            print ('e.message:'+ e.message)
            db.rollback()
        finally:
            db.close()
        return item
