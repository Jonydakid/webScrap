import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    def start_requests(self):
        urls = [
            'https://blog.scrapinghub.com/',
            'https://blog.scrapinghub.com/page/2',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.css('div.post-item'):
            description=post.css('.post-content span::text').get()
            if description is None:
                description=post.css('.post-content p::text').get()
            yield{
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get(),
                'desc': description
            }

            
        next_page= response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)