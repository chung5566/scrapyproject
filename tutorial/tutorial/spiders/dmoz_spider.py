from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
from scrapy.http import FormRequest


class DmozSpider(Spider):
    name = "dmoz"
    #allowed_domains = ["http://eli.npa.gov.tw/NPA97-217Client/oP01A01Q_01Action.do"]
    start_urls = [
        "http://eli.npa.gov.tw/NPA97-217Client/oP01A01Q_01Action.do?mode=query&method=doList"
    ]


    def parse(self, response):
       
        return  [FormRequest.from_response(response,
                formname='oP01A01Q_01Form',
                method='doQuery',
                formdata={
                            #'method':'doQuery',
                            #'action':'/NPA97-217Client/oP01A01Q_01Action.do',
                            'currentPage':'d-3657963-p=null',
                            'unit1Cd':'',
                            'unit2Cd':'',
                            'unit3Cd':'',
                            'puDateBeg':'1030607',
                            'puDateEnd':'1031205',
                            'objNm':'',
                            'objPuPlace':'',
                            },
                callback=self.parse1)]

        #method=doQuery&action=&currentPage=d-3657963-p%3Dnull&unit1Cd=&unit2Cd=&unit3Cd=&puDateBeg=1030607&puDateEnd=1031205&objNm=&objPuPlace=

        """cmrResultRequest = FormRequest("http://eli.npa.gov.tw/NPA97-217Client/oP01A01Q_01Action.do",
                            
                            method='doQuery',
                            formdata={
                                    'unit1Cd':'AW000',
                                    'unit2Cd':'AW300',
                                    'unit3Cd':'AW3O1',
                                    'puDateBeg':'1030607',
                                    'puDateEnd':'1031205'
                                    },
                            callback=self.parse1)
        return [cmrResultRequest]"""
        

    def parse1(self, response):
        print('aaaaaaaa')
        sel = Selector(response)
        sites = sel.xpath('//table[@class="ListTable"]/tbody/tr')
        item = DmozItem()
        items = []
        for site in sites:
            item['key'] = site.xpath('td[2]/text()').extract()
            item['unit'] = site.xpath('td[3]/text()').extract() 
            item['time'] = site.xpath('td[4]/text()').extract()
            item['place'] = site.xpath('td[5]/text()').extract() 
            item['content'] = site.xpath('td[6]/text()').extract() 

            items.append(item)
        return items

    
