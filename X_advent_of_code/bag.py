from items_in_bag import items


def cut_to_list(items_string:str):
    #function to convert items string to items list
    items_list = items_string.split('\n')
    return items_list

def find_match_in_row(items_list:list[str]):
    #function to find matches of items in rows of items list
    #function returns list of matches
    match_list = []
    for row in items_list:
        half_lenght = int(len(row)/ 2)
        found = False
        for symbol in row[0:half_lenght]:
            if not found == True:
                for second_symbol in row[half_lenght : len(row)+1]:
                    if symbol == second_symbol:
                        match_list.append(symbol)
                        found = True
                        break
    return match_list

def count_priority(match_list:list[str]):
    #count priority of items in list and return priority sum
    #velké - 38 (65-90), malé - 96 (97 -122)
    priority_list = []
    for match_item in match_list:
        raw_priority = ord(match_item)
        if (raw_priority >= 65 and raw_priority <= 90):
            new_priority = raw_priority - 38
            priority_list.append(new_priority)
        elif (raw_priority >= 97 and raw_priority <= 122):
            new_priority = raw_priority - 96
            priority_list.append(new_priority)
    priority = sum(priority_list)

    return priority

print(count_priority(find_match_in_row(cut_to_list(items))))

        



