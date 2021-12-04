# Польовий Максим

from numpy import *
from convert_market_data_to_json import dict_of_data_for_plot
import codecs

output_str = "# Польовий Максим"
for enterprise in dict_of_data_for_plot.items():
    output_str = output_str + "\n" + str(enterprise)

with codecs.open('txt_markets_data.txt', 'w', 'utf-8') as file:
    file.write(output_str)
