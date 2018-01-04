
def solution(A):
    # Check for corner case
    if A[0] == A[-1]:
        return 1

    # Build lookup table for adjacent values
    adjacent = {}
    previous = None
    for a in A:
        if previous:
            for first, second in [(a, previous), (previous, a)]:
                s = adjacent.get(first, set())
                s.add(second)
                adjacent[first] = s
        previous = a

    # Build reachability set
    reachability = {A[0]: 1}
    just_added = set([A[0]])
    while True:
        # round
        just_added_this_round = set()
        while just_added:
            element = just_added.pop()
            distance = reachability[element]
            for next_element in adjacent[element]:
                if next_element in reachability:
                    continue
                if next_element == A[-1]:
                    return distance + 1
                reachability[next_element] = distance + 1
                just_added_this_round.add(next_element)
        just_added = just_added_this_round


if __name__ == '__main__':
    print('Testing...')
    assert solution([1, 10, 6, 5, 10, 7, 5, 2]) == 4
    assert solution([1, 5, 3, 5, 9, 7, 5, 2, 4]) == 4
    assert solution([1, 1, 5, 3, 1]) == 1
    print('Ok!')

