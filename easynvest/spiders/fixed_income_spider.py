import json

import scrapy

from .constants import (
    COLUMNS_FIXED_INCOME,
    FIXED_INCOME,
    URL_LOGIN,
    URL_FIXED_INCOME,
)


class FixedIncomeSpider(scrapy.Spider):
    name = FIXED_INCOME
    start_urls = [URL_LOGIN]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "Conta": self.email,
                "AssinaturaEletronica": self.password,
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        print(f"{ response.xpath('//title/text()').extract_first() }")
        yield scrapy.Request(url=URL_FIXED_INCOME, callback=self.parse_fixed_income)

    def parse_fixed_income(self, response):
        """This method parses the fixed income from easynvest
        """

        print(response)
        fixed_incomes = response.xpath("//tbody/tr")
        self.all_incomes = []
        for fixed_income in fixed_incomes:
            income = {}
            for k, v in COLUMNS_FIXED_INCOME.items():
                income[k] = fixed_income.xpath(v).extract_first()
            self.all_incomes.append(income)
        self.save_fixed_incomes()
        

    def save_fixed_incomes(self):
        """Save income into a database
        """
        print(json.dumps(self.all_incomes, indent=4, sort_keys=True))
