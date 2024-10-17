import json
import yaml


# def read_file_json():
#     name_file = 'russian-cities.json'
#     with open(f'{name_file}') as openfile:
#         read_list = json.load(openfile)
#         return read_list
# # JSON data
# json_data = read_file_json()
#
#
#
# def save_file_yaml(json_data):
#     name_file = 'russian-cities.yaml'
#     with open(f'{name_file}', 'w', encoding="utf-8") as file:
#         yaml.dump(json_data, file, allow_unicode=True)
#
# save_file_yaml(json_data)


name_file = 'russian-cities.yaml'

def read_file_yaml(name_file):
    with open(f'{name_file}') as file:
        read_list = yaml.load(file, Loader=yaml.FullLoader)
        return read_list

read_data = read_file_yaml(name_file=name_file)
# city = {}
# for i in range(0, len(read_data)):
#     # print(read_data[i]['name'], read_data[i]['coords'])
#     city[read_data[i]['name']] = read_data[i]['coords']
# print(city)
#     # l = []
#     # for key, value in read_data[i].items():
#     #     print(key[1])
#
#        # if key == 'coords':
#        #     l.append((key, value))
# def save_file_yaml(name_file):
#     with open(f'{name_file}', 'w', encoding="utf-8") as file:
#         yaml.dump(city, file, allow_unicode=True)
#
# save_file_yaml('cities_coords.yaml')
#
#     # print(l)
#     # print(type(l))

read_data = read_file_yaml(name_file='cities_coords.yaml')

print(read_data['Москва'])






val = "EURGBP","EURJPY","EURRUB","EURUSD","GBPJPY","GBPRUB","JPYRUB","USDGBP","USDJPY","USDRUB","BTCRUB","BTCUSD"
print(type(val))
# for v in val:
d = dict()

for i in val:
    d[i] = i

print(d)
dict(d)

print(type(d))
def save_file_yaml(name_file = 'currency.yaml'):
    with open(f'{name_file}', 'w', encoding="utf-8") as file:
        yaml.dump(d, file, allow_unicode=True)


def read_file_yaml(name_file = 'currency.yaml'):
    with open(f'{name_file}') as file:
        read_list = yaml.load(file, Loader=yaml.FullLoader)
        print(type(read_list))
        print(read_list)

        return read_list

# save_file_yaml()
read_file_yaml()
