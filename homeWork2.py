# mission 1: Write a program that receive a string and prints how many times each
# character appeared in it
s = "dabaxyddab"
count_dict = {}
for char in s:
    if char not in count_dict:
        count_dict[char] = 1
    else:
        count_dict[char] += 1

# a: Print in a sorted according to lexicographic keys
for key in sorted(count_dict):
    print(key + "- " + str(count_dict[key]))

# b: Build an inverted dictionary, the quantities will now
# be the keys and all the characters that have the
# same quantity sat in the same list
reverseDict = {}
for key in count_dict:
    if count_dict[key] not in reverseDict:
        reverseDict[count_dict[key]] = [key]
    else:
        reverseDict[count_dict[key]].append(key)
print(reverseDict)


# mission 2: There are 3 lists
lst1 = [11,  7, 5,  8, 5,  37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

# a: Find only such lists that have at least one recurring value
general_dict = {}
general_dict["lst1"] = lst1
general_dict["lst2"] = lst2
general_dict["lst3"] = lst3
rest_lst = []
for lst in general_dict:
    lst_set = set(general_dict[lst])
    contains_duplicates = len(general_dict[lst]) != len(lst_set)
    if contains_duplicates:
        print(lst, "includes some values more than once")
    else:
        rest_lst.extend(general_dict[lst])

# b: Find common values from all the rest lists from "a"
# if one list remains - all its values are common, if no list remains - the answer will be empty
seen = set()
dupes = []
for x in rest_lst:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)
if len(dupes) == 0 and len(seen) > 1:
    dupes = seen
print(dupes)


# mission 3: Write a program that defines a list of
# numbers and sort_order=asc/desc variables and prints all
# the distinct digits from all the numbers in given list in sorted order
lst = [31, 99, 3, 1943]
lst_str = ""
for el in lst:
    lst_str += str(el)
# order_lst.append(lst_str)
order_lst = sorted(set(sorted(lst_str)))
print(order_lst)
order_lst.reverse()
print(order_lst)
