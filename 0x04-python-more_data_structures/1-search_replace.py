#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = []
    for i in my_list:
        if search == i:
            li.append(replace)
        else:
            li.append(i)
    return li
