# mission 1: Build a histogram list for a list of numbers using a repetition operator.
lst = [3, 7, 2]
histo = []
for el in lst:
    histo.append(el * "*")
print(histo)


# mission 2: There are 2 lists of strings of the same length, build a result list
# that each value is a chain of elements in order from the first list with
# elements in reverse order from the second list, respectively using range function
# for indexes to iterate both lists.
lst1 = ["a", "b", "c"]
lst2 = ["x", "y", "z"]
lst_res = []
for i, j in zip(range(len(lst1)), range(len(lst2) - 1, -1, -1)):
    lst_res.append(lst1[i] + lst2[j])
print(lst_res)
