#we have 10 stairs. We can climb those stairs going one step at a time, 
#two steps at a time, or three steps at a time, or any permutation of those
#possibilities. Calculate all possible ways of climbing those stairs.
#It's a permutation with repetition problem.

def ways_of_climbing(steps_list, num_stairs):
    result = []
    _climbing(steps_list, num_stairs, [], result)
    return result

def _climbing(steps_list, num_stairs, steps, result):
    if sum(steps) == num_stairs:
        result.append(steps)
        return
    if sum(steps) > num_stairs:
        return
    for step in steps_list:
        _climbing(steps_list, num_stairs, steps+[step], result)
    return result

print ways_of_climbing([1, 2, 3], 10)

