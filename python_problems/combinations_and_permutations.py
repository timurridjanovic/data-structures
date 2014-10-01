#combinations without repetition
#n!/(n-r)!(r!)

def combos(m, n, combo_list, result):
    if len(combo_list) == n:
        result.append(combo_list)
        return
    for i, e in enumerate(m):
        combos(m[i+1:], n, combo_list+[e], result)
    return result
    
    
#print combos([1, 2, 3, 4], 3, [], []) //4


#combinations with repetition
#(n+r-1)!/r!(n-1)!

def combos2(m, n, combo_list, result):
    if len(combo_list) == n:
        if sorted(combo_list) not in result:
            result.append(sorted(combo_list))
        return
    for e in m:
        combos2(m, n, combo_list+[e], result)
    return len(result)
    
    
#print combos2([1, 2, 3, 4], 3, [], []) //20


#permutations with repetition
#n^r

def perm(m, n, perm_list, result):
    if len(perm_list) == n:
        result.append(perm_list)
        return
    for e in m:
        perm(m, n, perm_list+[e], result)
    return len(result)
    
    
#print perm([1, 2, 3, 4], 3, [], []) //64


#permutations without repetition
#n!/(n-r)!

def perm2(m, n, perm_list, result):
    if len(perm_list) == n:
        result.append(perm_list)
        return
    for i, e in enumerate(m):
        perm2(m[:i] + m[i+1:], n, perm_list+[e], result)
    return len(result)
    
    
print perm2([1, 2, 3, 4], 3, [], []) #24



