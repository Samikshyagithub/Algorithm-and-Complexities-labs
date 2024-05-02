import random
import time
import matplotlib.pyplot as plt
from insertionsort import insertion_sort
from selectionsort import selection_sort
from copy import deepcopy


def generate_random_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]


def generate_graph():
    breakpoints = [i*100 for i in range(1, 21)]
    random_numbers = generate_random_array(breakpoints[-1])

    random_numbers_list = [random_numbers[0:i] for i in breakpoints]

    # Initialize lists to store time taken for each sorting algorithm
    time_taken_insertion_sort = []
    time_taken_selection_sort = []

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Insertion Sort
        start_time = time.time()
        insertion_sort(data_set)
        insertion_sort_endtime = time.time() - start_time
        time_taken_insertion_sort.append(insertion_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Selection Sort
        start_time = time.time()
        selection_sort(data_set.copy())
        selection_sort_endtime = time.time()-start_time
        time_taken_selection_sort.append(selection_sort_endtime)

    print(f" The time taken by Insertion Sort:\t {insertion_sort_endtime}\n")
    print(f"The time taken by Selection Sort:\t{selection_sort_endtime}\n")

 # Plotting the graph
    plt.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
    plt.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')

    plt.xlabel('Size of the Array')
    plt.ylabel('Time Taken in seconds')
    plt.title('Comparison of Insertion and Selection Sort')
    plt.legend()
    plt.grid(True)
    plt.show()


generate_graph()
