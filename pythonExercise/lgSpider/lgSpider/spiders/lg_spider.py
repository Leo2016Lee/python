# -*- coding:utf-8 -*-
import scrapy


from lgSpider.items import LgspiderItem


class lg_spider(scrapy.Spider):
    name = 'lg'  # 爬虫名字
    allowed_domains = ['www.51job.com']

    #  3个开始链接，分别为python，php，java职位信息
    start_urls = [
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%2594%25B5%25E6%25B0%2594,2,1.html?lang=c&stype=&postchannel=0000 \
        &workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99 \
        &providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0 \
        &confirmdate=9&fromType=&dibiaoid=0&address=&line= \
        &specialarea=00&from=&welfare='

    ]

    def parse(self, response):
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_job_info,
            meta={},
            dont_filter=True
        )

    def parse_next_page(self, response):
        """
        解析下一页
        :param response:
        :return:
        """
        next_page = response.xpath(
            "//li[@class='bk'][2]/a/@href").extract_first('')
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_job_info,
                meta={},
                dont_filter=True
            )
        """
        递归:如果一个函数内部自己调用自己
             这种形式就叫做递归
        """

    def parse_job_info(self, response):
        """
        解析工作信息
        :param response:
        :return:
        """
        job_div_list = response.xpath(
            "//div[@id='resultList']/div[@class='el']")
        for job_div in job_div_list:
            job_name = job_div.xpath(
                "p/span/a/@title").extract_first('无工作名称').strip().replace(",", "/")
            job_company_name = job_div.xpath(
                "span[@class='t2']/a/@title").extract_first('无公司名称').strip()
            job_place = job_div.xpath(
                "span[@class='t3']/text()").extract_first('无地点名称').strip()
            job_salary = job_div.xpath(
                "span[@class='t4']/text()").extract_first('面议').strip()
            job_time = job_div.xpath(
                "span[@class='t5']/text()").extract_first('无时间信息').strip()
            job_type = '51job' if '51job.com' in response.url else '其它'
            print(job_type, job_name, job_company_name,
                  job_place, job_salary, job_time)
            """
            数据清洗:负责清除数据两端的空格,空行,特殊符号等
            常用操作一般是strip
            包括清除无效数据,例如数据格式不完整的数据
            以及重复的数据
            """
            item = LgspiderItem()
            item['title'] = job_name
            item['company'] = job_company_name
            item['position'] = job_place
            item['salary'] = job_salary
            item['time'] = job_time

            yield item
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_next_page,
            dont_filter=True,
        )
