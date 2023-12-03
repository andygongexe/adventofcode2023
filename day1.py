# # Take an input file and for each line, take the first and last number. first is 10s, last is 1s; stick them together. 
# # Sum every single one of these numbers for our answer. 

# with open("day1.txt", "r") as f:
#     lines = f.readlines()

# # print(lines)
# total = 0
# # linelist = lines.split("\n")
# # print("lines: ", len( lines))
# for line in lines:
#     first = 100
#     last = 100
#     for i in range(len(line)):
#         # print(i)
#         if line[i].isdigit() and first == 100:
#             # print('first found')
#             first = int(line[i])
#         if line[-i-1].isdigit() and last == 100:
#             # print('last found')
#             last = int(line[-i-1])
#         if first != 100 and last != 100:
#             # print(f"{index}: {first*10+ last}")
#             break
#     # print(first*10 + last)
#     total += first*10 + last
            
# # print(total)
    
# part 2:
# Now we have some letters in there that should behave like numbers.
# Same code as last time, except we have a dictionary of letters to numbers.
# We also need to make sure that we're checking for the existence of letter-numbers in addition to just digits.
with open("day1.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

# lines = ['1ffffffffff6nine']

letterindex = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def finder(indexing, string):
    # If string[indexing] is a digit, return it.
    if string[indexing].isdigit():
        return int(string[indexing])
    # otherwise, check if it's a letter-number
    else:
        try:
            safestring = string + ('ABCDE')
            # print(safestring)
            # for each letter case
            for i in [3,4,5]:
                if indexing < 0:
                    candidate = safestring[indexing-6:indexing+i-6]
                else:
                    candidate = safestring[indexing:indexing+i]
                # print(f'candidate: {candidate}')
                try:
                    if type(letterindex[candidate]) == int:
                        print(f'found {letterindex[candidate]}')
                        return letterindex[candidate]
                except KeyError as e:
                    pass
            return 100

        except IndexError as e:
            return 100
        except KeyError as e:
            return 100

# print(lines)
total = 0
# linelist = lines.split("\n")
# print("lines: ", len( lines))
# print('test: ', finder(0, 'bone'))
# print('test2: ', finder(1, 'bone'))
# print(type(finder(1, 'b2one')))
for line in lines:
    first = 100
    last = 100
    for i in range(len(line)):
        # print(f'index: {i}')
        if first == 100:
            first = finder(i, line)
            if first != 100:
                print(f'first: {first}')
        if last == 100:
            last = finder(-i-1, line)
        if first != 100 and last != 100:
            print('line: ', line)
            print(first*10 + last)

            break
    
    total += first*10 + last
            
print(total)