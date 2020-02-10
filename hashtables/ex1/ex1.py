#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        print(f'insert: {weights[i]}, {i}')
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        print(f'checking for: {limit - weights[i]}')
        value = hash_table_retrieve(ht, limit - weights[i])

        if value is not None:
            print(f'{value}, {i}')
            return (value, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# get_indices_of_item_weights([4, 4], 2, 8)
# get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7)