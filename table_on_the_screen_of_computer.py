# Польовий Максим


from prettytable import PrettyTable
from markets_data import market_data_array
from markets_data import markets_array

first_table = PrettyTable()

date_format = "%d.%m.%y"

market_data_field_names = ['Дата', 'Код ринку', 'Картопля', 'Капуста',
                           'Цибуля']

first_table.field_names = market_data_field_names

for market_data in market_data_array:
    first_table.add_row([market_data.date,
                         market_data.code,
                         market_data.potato,
                         market_data.cabbage,
                         market_data.onion])

code_one_table = PrettyTable()

code_one_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 100:
        code_one_table.add_row([market_data.date,
                                market_data.code,
                                market_data.potato,
                                market_data.cabbage,
                                market_data.onion])

code_two_table = PrettyTable()

code_two_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 200:
        code_two_table.add_row([market_data.date,
                                market_data.code,
                                market_data.potato,
                                market_data.cabbage,
                                market_data.onion])

code_three_table = PrettyTable()

code_three_table.field_names = market_data_field_names

for market_data in market_data_array:
    if market_data.code == 300:
        code_three_table.add_row([market_data.date,
                                  market_data.code,
                                  market_data.potato,
                                  market_data.cabbage,
                                  market_data.onion])

second_table = PrettyTable()

second_table.field_names = ['Код ринку', 'Найменування ринку']

for market in markets_array:
    second_table.add_row([market.code, market.name])

while True:
    command = str(input(
        "Для виводу Табл.1 натисніть 1. Для виводу Табл.2 натисніть 2. \n"
        "Для виводу ринку за кодом напишіть Код і номер ринку, наприклад Код 100\n"
        "Щоб завершити роботу натисніть "
        "будь-яку іншу клавішу \n"))

    if command == "1":
        print(first_table)
    elif command == "2":
        print(second_table)
    elif command == "Код 100":
        print(code_one_table)
    elif command == "Код 200":
        print(code_two_table)
    elif command == "Код 300":
        print(code_three_table)
    else:
        print("Кінець роботи")
        break
