import scrapy
import json
from scrapy import Request,http
# from scrapy_splash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger
import pandas as pd

class TenderSunnywaleSpider(scrapy.Spider):
    name = 'tender_sunnywale'
    allowed_domains = ['https://www.demandstar.com/']
    start_urls = ['https://api.demandstar.com/contents/agency/search?id=e9a860f4-8f17-43af-aae7-e5dc8389f36e']
 
    
    def parse(self, response):
          data=json.loads(response.body)
          details=data.get('result')
          for detail in details:

              yield {
                  'bidId':detail.get('bidId'),
                  'bidName':detail.get('bidName'),
                  'agency':detail.get('agency'),
                  'bidIdentifier':detail.get('bidIdentifier'),
                  'broadCastDate':detail.get('broadCastDate'),
                  'dueDate':detail.get('dueDate'),
                  'internalStatus':detail.get('internalStatus'),
                  'mi':detail.get('mi'),
                  'percentage':detail.get('percentage'),
                  'planholders':detail.get('planholders'),
                  'postalCode':detail.get('postalCode'),
                  'state':detail.get('state'),
                  'status':detail.get('status')
              } 
            