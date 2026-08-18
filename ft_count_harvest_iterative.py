def ft_count_harvest_iterative():
    stop = int(input("Days until harvest: "))
    for start in range(stop):
        print("Day", start + 1)
    print("Harvest time!")
