def count_inversion(sequence):
    # we need the sequence to be mutable for this to work
    if type(sequence) is not list:
        sequence = list(sequence)

    # divide and conquer: count inversions in sequence[first:last]
    # important invariant: afterwards sequence[first:last] will be sorted
    def count(first, last):
        # recursion ends when there are too few elements
        if last - first < 2:
            return 0
        # divide in two halves and count inversions separately
        mid = (first + last) // 2
        inversions = count(first, mid)
        inversions += count(mid, last)
        # then add cross-half inversions while merging the two halves
        i, j = first, mid
        ordered = []
        while i < mid and j < last:
            if sequence[i] < sequence[j]:
                ordered.append(sequence[i])
                i += 1
            else:
                ordered.append(sequence[j])
                j += 1
                # count all remaining elements in first half as inversions
                inversions += mid - i
        ordered.extend(sequence[i:mid])
        ordered.extend(sequence[j:last])
        sequence[first:last] = ordered
        return inversions

    # and now, just count them all...
    return count(0, len(sequence))


print(count_inversion([5, 8, 4]))
