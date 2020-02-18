from abc import ABC

import scrapy

class PostsSpider(scrapy.Spider, ABC):
    name = "posts"

    #assign which page or url as my first scraping webpage
    start_urls = [
        "https://blog.scrapinghub.com/"
    ]

    #response is a whole html file, but we just need specific content
    def parse(self, response):
        for post in response.css("div.post-item"):
            # build the content
            yield{
                "title": post.css(".post-header h2 a::text")[0].get(),
                "date": post.css(".post-header a::text")[1].get(),
                "author": post.css(".post-header a::text")[2].get()
            }
