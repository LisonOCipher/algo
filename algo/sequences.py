
def remove_duplicates(sequences):

    list = set()
    return [ x for x in sequences if not (x in list or list.add(x))]


input_sequences = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequences)
print(result) 