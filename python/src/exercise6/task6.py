import json

with open("input.txt", "r") as file:
    try:
        data_dict = json.load(file)
        new_list = data_dict['list1'] + data_dict['list2']
        sorted_list = sorted(new_list, key=lambda x: x['year'])
        new_dict = { 'list0': sorted_list }
        print(new_dict)
    except json.JSONDecodeError:
        print('incorrect input') 

