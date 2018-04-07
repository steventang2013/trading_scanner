import time

import schedule

from config import Config
from .request_processor import RequestProcessor


class APIService(object):

    def __init__(self, stocks):
        self.api = Config.API
        self.key = Config.API_KEY
        self.queries = self._prepare_query(stocks)

    def _prepare_request(self, ticker):
        return '{}/query?function=TIME_SERIES_INTRADAY&symbol={}' \
               '&interval=1min&apikey={}&outputsize=compact'.format(self.api, ticker, self.key)

    def _prepare_query(self, stocks):
        return [self._prepare_request(stock) for stock, margin in stocks]

    # This method will continue to execute every minute
    def execute(self):
        processor = RequestProcessor()
        schedule.every(1).minutes.do(processor.make_requests(self.queries))
        while True:
            schedule.run_pending()
            time.sleep(1)
