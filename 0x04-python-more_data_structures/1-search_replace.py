#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = my_list.copy()
    if search in li:
        ind = li.index(search)
    for i in li:
        if ind == i:
            li[ind] = replace
    return li
  

  
