import json

result_list = []
dict_plus_profit = {}
dict_minus_profit = {}
with open("File7") as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)
    result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})

with open("File7.json", "w") as file:
    json.dump(result_list, file)
