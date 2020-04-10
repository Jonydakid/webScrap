import scrapy


class WikiSpider(scrapy.Spider):
    name = "wikiscrap"

    def start_requests(self):
        urls = [
            'https://es.wikipedia.org/wiki/Web_scraping',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)