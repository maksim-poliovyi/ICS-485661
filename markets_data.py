# Польовий Максим


import operator
from dataclasses import dataclass
import json
import codecs
import dateparser

@dataclass
class Market:
    code: int
    name: str


@dataclass
class MarketData:
    date: str
    code: int
    potato: float
    cabbage: float
    onion: float

    def __eq__(self, other):
        return self.code == other.code and self.date == other.date

    def __lt__(self, other):
        return self.code < other.code and dateparser.parse(self.date) < dateparser.parse(other.date)


# Json був зроблений за допомогою Tabula
with codecs.open("tabula-zad5.json", "r", 'utf-8') as f:
    tabula_dict = json.load(f)

market_data_array = []

for json_item in tabula_dict:
    data_list = json_item['data']

    for data in data_list:
        market_data_array.append(MarketData(str(data[0]["text"]),
                                            int(data[1]["text"]),
                                            float(str(data[2]["text"])),
                                            float(str(data[3]["text"])),
                                            float(str(data[4]["text"]))))

markets_array = [Market(100, "Бесарабський"), Market(200, "Житній"), Market(300, "Володимирський")]


class AnalysisMarketsPrices:

    def __init__(self, code, name, date, potato, cabbage, onion):
        self.code = code  # Код ринку
        self.name = name  # Найменування ринку
        self.date = date  # Дата
        self.potato = potato  # Ціна, картопля
        self.cabbage = cabbage  # Ціна, капуста
        self.onion = onion  # Ціна, цибуля
        self.averagePrice = self.calculateAveragePrice(self.potato, self.cabbage, self.onion)  # Середня ціна

    def calculateAveragePrice(self, potato, cabbage, onion):
        return round((potato + cabbage + onion) / 3, 2)

    def __str__(self) -> str:
        return f"Code {self.code}, {self.name}, {self.date} {self.potato} {self.cabbage} {self.onion} {self.averagePrice}"


analysisMarketsPrices = []

for data in market_data_array:
    analysisMarketsPrices.append(AnalysisMarketsPrices(
        code=data.code,
        name=markets_array[int(data.code / 100 - 1)].name,
        date=data.date,
        potato=data.potato,
        cabbage=data.cabbage,
        onion=data.onion))

sorted_by_code = sorted(analysisMarketsPrices, key=operator.attrgetter("code"))
