def ft_recursive_util(start, stop):
    if (start <= stop):
        print("Day", start)
        start = start + 1
        ft_recursive_util(start, stop)


def ft_count_harvest_recursive():
    stop = int(input("Days until harvest: "))
    start = 1
    ft_recursive_util(start, stop)
    print("Harvest time!")
