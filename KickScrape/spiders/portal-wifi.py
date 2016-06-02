import scrapy

class KickstarterSpider(scrapy.Spider):
    name = 'portal'
    allowed_domains = ['https://www.kickstarter.com']
    start_urls = ['https://www.kickstarter.com/projects/portalwifi/portal-turbocharged-wifi']

    def parse(self, response):
        f = open("test.txt", "wb")
        sel = scrapy.Selector(response)
        count = 0
        requests = sel.xpath('//li[@data-reward-id="5049870"]/div/p[@class="pledge__backer-count"]/span')
        for r in requests:
            if count == 1:
                name = r.xpath('normalize-space(text()[1])').extract()
                if name[0] == 'All gone!':
                    f.write('Sad')
                else:
                    f.write( 'AVAILABLE' )
                    f.write( `name` )
            count += 1
