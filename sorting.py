import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(sequence):
    sequence = sequence[:]
    idx = 0
    while idx < len(sequence):
        smallest = min(sequence[idx:])
        ix = sequence.index(smallest,idx)
        # (...,idx) mi urcuje odkud zacinam hledat aby to neztroskotalo na tom ze tam jsou dve stejna cisla a najde mi to to prvni
        sequence[idx], sequence[ix] = sequence[ix], sequence[idx]
        idx += 1

#    n = len(sequence)
#    for i in range(n):
#        min_idx = i
#        for idx in range(i + 1, n):
#            if sequence[idx] < sequence[min_idx]:
#                min_idx = idx
#        sequence[min_idx], sequence[i] = sequence[i], sequence[min_idx]

    return sequence


def bubble_sort(sequence):
    sequence = sequence[:]
    plt.ion()
    plt.show()
    n = len(sequence)
    for cycle in range(n - 1):
        for idx in range(n - 1 - cycle):
            index_highlight1 = idx
            index_highlight2 = idx + 1
            colors = ["steelblue"] * len(sequence)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(sequence)), sequence, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if sequence[idx] > sequence[idx + 1]:
                sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
    plt.ioff()
    plt.show()
    return sequence

def main():
    sequence = random_numbers(20)
    sort_sequence = selection_sort(sequence)
    sorted_sequence = bubble_sort(sequence)
    print(f"Selection sort: {sort_sequence}")
    print(f"Bubble sort: {sorted_sequence}")

if __name__ == "__main__":
    main()
