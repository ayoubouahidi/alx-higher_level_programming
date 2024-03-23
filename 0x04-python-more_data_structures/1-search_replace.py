#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        ind = my_list.index(search)
    for i in my_list:
        if ind == i:
            my_list[ind] = replace
    return my_list
  

  
