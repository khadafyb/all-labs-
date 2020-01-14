def list_evaluation(list1,list2):
    for i in list1:
        if i in list1 and i in list2:
            print(i, "in list 1 and 2")
        elif i in list1 and  i not in list2:
            print(i, "in list 1 but not 2")
    for i in list2:
        if i in list2 and  i not in list1:
            print(i, "in list 2 but not 1")
        elif i in list1 or  i in list2:
            print(i, "in list 1 or 2")
