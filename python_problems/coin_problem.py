#We have 5 cent coins, 10 cent coins and 25 cent coins. We want all 
#possible combinations of coins that will make a dollar. This means 
#that it is a combination with repetition problem.

def coin_combination(coin_list, amount):
    result = []
    _coin_combination(coin_list, amount, [], result)
    return result


def _coin_combination(coin_list, amount, combination, result):
    if sum(combination) == amount:
        if sorted(combination) not in result:
            result.append(sorted(combination))
        return
    if sum(combination) > amount:
        return
    for coin in coin_list:
        _coin_combination(coin_list, amount, combination + [coin], result)
    return result


print coin_combination([5, 10, 25], 100)



