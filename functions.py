
def cleaner(in_list : list[str],filter_list : list[str]):
    """
    in_list : Input list to be cleaned
    filter_list : List of items to be filtered out
    """

    n = []
    value = []

    for i in filter_list:
        n = in_list.split(i)

    for i in n:
        if i == '':
            n.remove(i)

    for i in n:
        if ' ' in i or ',' in i:
            i = i.split('</div>')
            i.pop(1)
            i.pop(1)
            value += i

    return value

def filter(in_list : list[str]):
    """
    in_list : List to be filtered
    """

    sorted = []
    list = []
    end = []
    result = []
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in in_list:
        if len(i) == 1:
            continue
        else:
            sorted.append(i)
        
    for i in sorted:
        list += i

        for i in list:
            if i == ',':
                list.remove(i)
        x = ''.join(list)
        end.append(x)

        list = []

    for i in end:
        if any(s in i for s in letters) == False:
            i = int(i)
            result.append(i)
        else:
            result.append(i)
              
    return result

