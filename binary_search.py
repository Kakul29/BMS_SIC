def binary_search(search_element,input_list):
    low=0
    high=len(input_list)-1
    while low<=high:
        middle_index=(low+high)//2
        if search_element==input_list[middle_index]:
            return middle_index
        elif search_element < input_list[middle_index]:
            high = middle_index - 1 #searching first part of list
        else:
            low = middle_index + 1    #searching last part of list
            