def max(intervals):

    max_intervals = []

    intervals.sort(key=lambda x: x[0])

    previous_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start <= previous_end:
            max_intervals.append([start, end])
            previous_end = end
        else:
            previous_end = min(previous_end, end)

    return max_intervals

if __name__ == "__main__":

    arr = [[1, 5], [2, 3], [3, 6]]
    print(max(arr))

