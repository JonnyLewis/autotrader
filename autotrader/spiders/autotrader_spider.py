# -*- coding: utf-8 -*-
import scrapy
import re

class AutotraderSpiderSpider(scrapy.Spider):
	name = 'autotrader_spider'
	allowed_domains = ['autotrader.com']
	start_urls = ['https://www.autotrader.com/cars-for-sale/searchresults.xhtml?zip=20005&marketExtension=on&startYear=1981&endYear=2019&searchRadius=50&sortBy=relevance&numRecords=25&firstRecord=0']

	def parse(self, response):
		XPATH_CAR_LISTINGDS = "//div[@class='item-card-body']"
		cars = response.xpath(XPATH_CAR_LISTINGDS)
		raw_searched_zipcode = re.findall("zip=(.*?)&",response.url)
		searched_zipcode = raw_searched_zipcode[0] if raw_searched_zipcode else None

		for car in cars:
			XPATH_PRICE = ".//div[@data-cmp='pricing']//text()"
			XPATH_TITLE = ".//h2//text()"
			XPATH_MILES = ".//span[@class='text-bold']//text()"
			XPATH_COLOR = ".//li[contains(span/text(),'Color')]/text()"
			XPATH_MPG = ".//li[contains(span/text(),'MPG')]/text()"
			XPATH_DRIVE_TYPE = ".//li[contains(span/text(),'Drive Type')]/text()"
			XPATH_ENGINE = ".//li[contains(span/text(),'Engine')]/text()"
			XPATH_LINK = ".//a/@href"
			XPATH_LISTING = ".//a[contains(@href,'cars-for-sale')]/parent::div/span/text()"
			
			price = car.xpath(XPATH_PRICE).extract_first()
			title = car.xpath(XPATH_TITLE).extract_first()
			miles_used = car.xpath(XPATH_MILES).extract_first()
			color = car.xpath(XPATH_COLOR).extract_first()
			mpg = car.xpath(XPATH_MPG).extract_first()
			drive_type = car.xpath(XPATH_DRIVE_TYPE).extract_first()
			engine = car.xpath(XPATH_ENGINE).extract_first()
			link = car.xpath(XPATH_LINK).extract_first()
			list_type = car.xpath(XPATH_LISTING).extract_first()
			absolute_link = "https://www.autotrader.com"+link if link else None

			data = {"price":price,
					"title":title,
					"miles_used":miles_used,
					"color":color,
					"mpg":mpg,
					"drive_type":drive_type,
					"engine":engine,
					"link":absolute_link,
					"list_type":list_type,
					"searched_zipcode":searched_zipcode
			}
			yield data