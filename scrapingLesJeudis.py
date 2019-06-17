

import scrapy

class BlogSpider(scrapy.Spider):
	name = 'blogspider'

	start_urls = ['https://www.lesjeudis.com/recherche?utf8=✓&q=data+analyst&loc=Île-de-France']

	def parse(self, response):
		for rubrique in response.css('div.job-info'):
			yield {
					'Intitulé du poste': rubrique.css('a.job-title ::text').getall(),
					'Date de publication': rubrique.css('div.date a ::text').get(),
					'lieu': rubrique.css('a.snapshot-item ::text').getall(),
					'competences': rubrique.css('div.tags a::text').getall(),
					'Type de poste':rubrique.css('div.snapshot-item ::text').getall()
					}

		for next_page in response.css('a.btn-arrow::attr(href)').getall():
			print(next_page)
			if next_page is not None:
				next_page = response.urljoin(next_page)
				yield response.follow(next_page, self.parse)



# scrapy runspider scrapingLesJeudis.py -o scrapp.json
