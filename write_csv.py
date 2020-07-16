__author__ = '220152'

import json

with open("data.json", "r") as data:
    dictionary = json.load(data)

if len(dictionary) == 0:
    print("No data loaded")
    quit()
else:
    with open("mysql_data.csv", "a+", encoding = "utf-16") as output:
        counter = 0
        for item in dictionary.items():
            counter += 1
            if type(item[1]) == list:
                definition_list = []
                for definition in item[1]:
                    # expression = item[0].replace("[", "").replace("]", "").replace('"', "'")
                    # definition = definition.replace("[", "").replace("]", "").replace('"', "'")
                    definition_list.append(item[0] + "\t" + definition)

                output.write("\n".join(definition_list))
            else:
                output.write(item[0] + "<>" + item[1])

            if len(dictionary) - counter > 0:
                output.write("\n")





