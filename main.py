# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_str = ['qweqwr', 'qweq', 'qwe', 'ersgversvdsrv','evfsevsevsevsevse', 'rt','rt','jj']
list_in_list = list()


list_in_list.append(list_test)
list_in_list.append(list_str)
list_in_list.append(123)

dict_test = {'key1': 'value1', 'key2': 'value2'}
dict_test2 = {'key3': 'value3', 'key4': 'value4'}
dict_test3 = dict()
for key, value in dict_test.items():
    dict_test3[key] = value
for key, value in dict_test2.items():
    dict_test3[key] = value

print(dict_test3)


#
# for key, value in dict_test.items():
#     print(f'{key}-{value}')


# print (list_in_list)
#
#
# for i in list_in_list:
#     if hasattr(i, "__iter__"):
#         for j in i:
#          print(j)
#     else:
#         print(i)


    # if len(i)>5:
    #     print(i)

