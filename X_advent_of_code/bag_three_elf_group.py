from items_in_bag import items

items = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def cut_to_list(items_string:str):
    #function to convert items string to items list
    items_list = items_string.split('\n')
    return items_list

def cut_to_group_list(items_list:list[str]):
    #function to make list of lists of 3 strings of equipment
    #chyba
    count_of_groups = int(len(items_list)/3)
    list_of_groups = []
    row_for_three = []
    elf_number = 0
    for row in items_list:
        row_for_three.append(row)
        elf_number += 1
        if elf_number == 3:        
            list_of_groups.append(row_for_three)
            elf_number = 0
            row_for_three = []
    return list_of_groups

def find_match(list_of_groups:list[list[str]]):
    #function is finding match in every group and return this matches
    matches = []
    for group in list_of_groups:
        match_founded = False
        working_group = group.copy()
        for bag in group:
            if match_founded == True:
                break
            for symbol in bag:
                if symbol in working_group[1] and symbol in working_group[2]:
                    matches.append(symbol)
                    match_founded = True
                    break
    return matches


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

 



        



