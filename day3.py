# day 3

# Find indices of all numbers. Scan around the numbers to find if there's a symbol there. 
with open("day3.txt", "r") as f:
    schematic = f.readlines()
symbols = ['+', '-', '*', '/', '$', '#', '%', '@', '=', '!', '^', '&', '(', ')', '[', ']', '{', '}', '<', '>', '?', '|', '~', '`', '_', '"', "'", ':', ';', ',']
schematic = [line.strip() for line in schematic]
schematic = ''.join(schematic)

linelength = 140


def find_numbers(schematic):
    indices = []
    i = 0
    numstart = 0
    numend = 0
    while i < len(schematic):
        if schematic[i].isdigit():
            numstart = i
            while schematic[i].isdigit() and i < len(schematic):
                # print('# at: ', i)
                i += 1
            numend = i
            indices.append([numstart, numend])
        i += 1
    return indices

def scan_around(coordinate, schematic):
    # print('coordinate: ', coordinate)
    if coordinate[0] >= 140:
        for i in range(coordinate[1]-coordinate[0]+2):
            try :
                if schematic[coordinate[0]-1-140+i] in symbols:
                    return True
            except IndexError as e:
                pass
    if coordinate[1] <= 140*139:
        for i in range(coordinate[1]-coordinate[0]+2):
            try :
                if schematic[coordinate[0]-1+140+i] in symbols:
                    return True
            except IndexError as e:
                pass
    try:
        if schematic[coordinate[0]-1] in symbols:
            return True
    except IndexError as e:
        pass
    try:
        if schematic[coordinate[1]] in symbols:
            print('triggered on ', schematic[coordinate[0]:coordinate[1]])
            return True
    except IndexError as e:
        pass
    return False

# total_part_count = 0
# # print('starting')
# coords = find_numbers(schematic)
# # print('found coords')
# for coord in coords:
#     if scan_around(coord, schematic):
#         # print('found part: ', schematic[coord[0]:coord[1]])
#         total_part_count += int(schematic[coord[0]:coord[1]])
#     else:
#         # print('neglected part: ', schematic[coord[0]:coord[1]])
#         pass

# print(total_part_count)

# part 2

gear = '*'

def scan_around_for_gears(coordinate, schematic): # returns the index of the gear
     # print('coordinate: ', coordinate)
    if coordinate[0] >= 140:
        for i in range(coordinate[1]-coordinate[0]+2):
            try :
                if schematic[coordinate[0]-1-140+i] in gear:
                    return coordinate[0]-1-140+i
            except IndexError as e:
                pass
    if coordinate[1] <= 140*139:
        for i in range(coordinate[1]-coordinate[0]+2):
            try :
                if schematic[coordinate[0]-1+140+i] in gear:
                    return coordinate[0]-1+140+i
            except IndexError as e:
                pass
    try:
        if schematic[coordinate[0]-1] in gear:
            return coordinate[0]-1
    except IndexError as e:
        pass
    try:
        if schematic[coordinate[1]] in gear:
            # print('triggered on ', schematic[coordinate[0]:coordinate[1]])
            return coordinate[1]
    except IndexError as e:
        pass
    return False

dict_of_gears = {}
total_gear_power = 0
number_indices = find_numbers(schematic)
for number_index in number_indices:
    gear_index = scan_around_for_gears(number_index, schematic)
    try: 
        if dict_of_gears[gear_index] != False:
            # print('adjacent gear found')
            total_gear_power += int(schematic[number_index[0]:number_index[1]])*int(schematic[dict_of_gears[gear_index][0]:dict_of_gears[gear_index][1]])
    except KeyError as e:
        pass
    if gear_index != False:
        dict_of_gears[gear_index] = number_index

print(total_gear_power)






