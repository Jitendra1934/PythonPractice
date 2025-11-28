li = input("enter the list\n")
split_li = li.split(":")
print(split_li)

my_dic = {
    'ten':split_li[0], 'twenty':split_li[1]
}
print(my_dic)

print(my_dic['ten'])
print(my_dic['twenty'])
print(type(my_dic))