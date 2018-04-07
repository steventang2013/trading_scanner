import os
from service.api_service import APIService


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = 'movers.txt'


def load_me(full_path):
    stocks = []
    with open(full_path, 'r') as f:
        for line in f:
            line_stock = line.strip('\n').split(',')
            stock = line_stock[0]
            margin = line_stock[1] if len(line_stock) > 1 else None
            stocks.append((stock, margin))

    return stocks


def service_stocks(stocks_in_play):
    service = APIService(stocks_in_play)
    service.execute()


if __name__ == "__main__":
    file_path = '\stocks\{}'.format(FILENAME)
    full_path = ROOT_DIR + file_path
    if not os.path.isfile(full_path):
        raise ImportError('File: {} does not exist'.format(full_path))

    stocks_in_play = load_me(full_path)
    service_stocks(stocks_in_play)
