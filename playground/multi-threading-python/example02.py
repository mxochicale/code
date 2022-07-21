import random


def append_to_list(lst, num_items):
    """
    Appends num_items integers within the range [0-20000000) to the input lst
    """
    for n in random.sample(range(20000000), num_items):
        lst.append(n)

    return lst


def main():
    number_of_items = 10000000 #10  #  # #
    for i in range(2):
        #print(f'i: {i}')
        a_list = append_to_list([], number_of_items)
        #print(a_list)


if __name__ == "__main__":
    main()
