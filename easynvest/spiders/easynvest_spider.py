import scrapy

from .constants import (
    COLUMNS_RENDA_FIXA,
    RENDA_FIXA,
    URL_LOGIN,
    URL_RENDA_FIXA
)


class EasynvestSpider(scrapy.Spider):
    name = RENDA_FIXA
    start_urls = [URL_LOGIN]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"Conta": self.email, "AssinaturaEletronica": self.password},
            callback=self.after_login,
        )

    def after_login(self, response):
        print(f"{ response.xpath('//title/text()').extract_first() }")
        yield scrapy.Request(url=URL_RENDA_FIXA, callback=self.renda_fixa)

    def renda_fixa(self, response):
        ativos = response.xpath("//tbody/tr")
        a = []
        for ativo in ativos:
            obj = {}
            for k, v in COLUMNS_RENDA_FIXA.items():
                obj[k] = ativo.xpath(v).extract_first()
            a.append(obj)
        print(a)
