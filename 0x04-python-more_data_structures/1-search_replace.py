#!/usr/bin/python3
def search_replace(my_list, search, replace):
    li = my_list.copy()
    
    for i in li:
        if search == i:
             li.append(replace)
        else:
            li.append(i)
    return li
  

  
