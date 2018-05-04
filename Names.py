names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

def remove(x):
    final_list = []
    for name in x:
        if name not in final_list:
            final_list.append(name)
    
    print(final_list)

remove(names)

