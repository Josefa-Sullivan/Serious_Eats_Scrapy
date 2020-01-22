import scrapy
from Serious_Eats.items import SeriousEatsItem 
import IPython
# throw into code to inspect the state of the code wherever you put it
# IPython.embed()


class SeriousSpider(scrapy.Spider):

    # Start scraping recipes from the cuisine page of Seriouseats.com
    name = 'serious_spider'
    allowed_domains = ['seriouseats.com']
    start_urls = ['https://www.seriouseats.com/recipes/topics']
    

    def parse(self, response):
        topic_lis = ['/ingredient', '/cuisine', '/meal', '/method']
        topic_urls = [response.url + x for x in topic_lis]

        for i, topic_url in enumerate(topic_urls):
            yield scrapy.Request(topic_url, callback=self.parse_topic, meta={'Topic': topic_lis[i]})

    # Parse each list page for a given topic that has recipes
    def parse_topic(self, response):
        npages = int(response.xpath('//div[@class="ui-pagination-jump-links"]//a[3]/text()').extract_first())
        next_urls = [response.url + '?page=%d#recipes' %page_num for page_num in range(2,npages+1) ]

        for url in next_urls:
            yield scrapy.Request(url, callback=self.parse_list_page, meta= response.meta)

    # Get the link and subtopic for each recipe(total of 24) on a list page and pass to next parse method
    def parse_list_page(self, response):
        
        print("parsing list page")

        # Examples: {Cuisine: Chinese, Method: Braising, Ingredient: Tomato, Meal: Sides}
        subtopic = response.xpath('//div[@class="module"]//a[@class="category-link"]/span/text()').extract()[:24]

        recipes = response.xpath('//div[@class="module__wrapper"]/a[@class="module__image-container module__link"]/@href').extract()[:24]

        for i, recipe in enumerate(recipes):
            yield scrapy.Request(recipe, callback=self.parse_recipe, meta={'Subtopic': subtopic[i], 'Link': recipes[i], 'Topic': response.meta['Topic']})

    # Parse an individual recipe page for various features, including title, servings, and ingredients
    def parse_recipe(self, response):
        # save response
        #  get all my data
        # print("I have an item")
        topic = response.meta['Topic']
        subtopic = response.meta['Subtopic']
        link = response.meta['Link']


        # Get title as a string, Uses join to avoid incomplete data caused by formatting tags
        try:
            title = " ".join((response.xpath('//h1[@class="title recipe-title"]//text()').extract()))
        except:
            title = ""

        try:
            author = response.xpath('//span[@class="author-name"]/a//text()').extract_first()
        except:
            author = ""

        try:
            pub_date = response.xpath('//span[@class="publish-date"]/time/text()').extract_first()
        except:
            pub_date = ""

        try:
            photographer = response.xpath('//div/p[@class="caption"]/text()').extract_first().split(":")[1]
       
        except:
            photographer = ""

        try:
            servings = response.xpath('//span[@class="info yield"]/text()').extract_first()

        except:
            servings = ""

        try:
            active_time = response.xpath('//li/span[@class="info"]/text()').extract_first()
        except:
            active_time = ""
        
        try:
            total_time = response.xpath('//li/span[@class="info"]/text()').extract()[1]
        except:
            total_time = ""

        try:
            rating = float(response.xpath('//span[@class="info rating-value"]/text()').extract_first())
        
        except:
            rating = ""

        try:
            ingredients = response.xpath('//li[@class="ingredient"]//text()').extract()
        except:
            ingredients = ""

        try:
            directions = response.xpath('//li[@class="recipe-procedure"]//p/text()').extract()
        except:
            directions =""


        item = SeriousEatsItem()
        item['topic'] = topic
        item['title'] = title
        item['subtopic'] = subtopic
        item['link'] = link
        item['author'] = author
        item['pub_date'] = pub_date
        item['photographer'] = photographer
        item['servings'] = servings
        item['active_time'] = active_time
        item['total_time'] = total_time
        item['rating'] = rating
        item['ingredients'] = ingredients
        item['directions'] = directions


        yield item