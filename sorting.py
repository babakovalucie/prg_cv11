import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(sequence):
    sequence = sequence[:]
    idx = 0
    while idx < len(sequence):
        smallest = min(sequence[idx:])
        ix = sequence.index(smallest,idx)
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
    cycle = 0
    n = len(sequence)
    for cycle in range(n - 1):
        for idx in range(n - 1 - cycle):
            if sequence[idx] > sequence[idx + 1]:
                sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
    return sequence

def main():
    sequence = random_numbers(20)
    sort_sequence = selection_sort(sequence)
    sorted_sequence = bubble_sort(sequence)
    print(f"Selection sort: {sort_sequence}")
    print(f"Bubble sort: {sorted_sequence}")

if __name__ == "__main__":
    main()
