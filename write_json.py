__author__ = '220152'

import json, codecs

with open("data.json", "r") as data:
    dictionary = json.load(data)

if len(dictionary) == 0:
    print("No data loaded")
    quit()
else:
    with open("mysql_data.json", "a+", encoding = "utf-16") as output:
        output.write("{")
        counter = 0
        for item in dictionary.items():
            counter += 1
            if type(item[1]) == list:
                definition_list = []
                for definition in item[1]:
                    expression = item[0].replace("[", "").replace("]", "").replace('"', "'")
                    definition = definition.replace("[", "").replace("]", "").replace('"', "'")
                    definition_list.append('"'+expression+'"'+':"'+definition+'"')

                output.write(",".join(definition_list))
            else:
                expression = item[0].replace("[", "").replace("]", "").replace('"', "'")
                definition = item[1].replace("[", "").replace("]", "").replace('"', "'")
                output.write('"'+expression+'"'+':"'+definition+'"')

            if len(dictionary) - counter > 0:
                output.write(",")

        output.write("}")





