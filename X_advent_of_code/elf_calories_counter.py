from calories import calories
#importing string with data

def richest_elf(calories):
#creating new list with sum of calories for every elf
    calories_list = calories.split('\n\n')
    new_list = []
    for elf in calories_list:
        elf = elf.strip()
        one_elf_food = elf.split('\n')
        elf_calories_count = int(0)
        for food in one_elf_food:
            elf_calories_count += int(food)
        new_list.append(elf_calories_count)
    #grnerating three richest elfs
    richest_elfs = []
    for _ in range(3):
        top_position = new_list.index(max(new_list))
        richest_elfs.append(new_list[top_position])
        new_list[top_position] = 0
    richest_elfs = sum(richest_elfs)
    return richest_elfs

print(richest_elf(calories))