#Given an array that contains N integers.number of repetitions of each integer in array is represented by ri.Task is to print the integers in the decreasing order of their occurance in the array.


from collections import Counter
def group_Sol(N,a):
    ini_list = a
    result = [item for items, c in Counter(ini_list).most_common()
                                          for item in [items] * c]
    a = result
    import collections
    dup = [item for item, count in collections.Counter(a).items() if count > 1]
    dup.sort(reverse = True)
    new = dup
    dup1=set(a)
    for i in dup1:
        if i in dup:
            pass
        else:
            new.append(i)
    joined_string = ' '.join([str(v) for v in new])
    return(joined_string)
    
N= int(input())
a= list(map(int,input().split()))

out_ =group_sol(N,a)
print(*out_)
