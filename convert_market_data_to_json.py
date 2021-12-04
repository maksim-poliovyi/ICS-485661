# Польовий Максим


import markets_data
import json
import codecs

dict_of_data_for_plot = {}

for efficiency in markets_data.sorted_by_code:

    try:
        dict_of_data_for_plot[efficiency.name]
    except:
        dict_of_data_for_plot[efficiency.name] = {}

    for attr, value in vars(efficiency).items():
        if attr != 'name' and attr != 'code':
            try:
                dict_of_data_for_plot[efficiency.name][attr].append(value)
            except:
                dict_of_data_for_plot[efficiency.name][attr] = [value]

# json_data = json.dumps(dict_of_data_for_plot, ensure_ascii=False).encode('utf8')
with codecs.open('markets_data.json', 'w', 'utf-8') as json_file:
    json.dump(dict_of_data_for_plot, json_file, ensure_ascii=False)
