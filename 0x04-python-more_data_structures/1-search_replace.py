#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elm(item):
        return (item if item != search else replace)
    return list(map(s_r_elm, my_list))
