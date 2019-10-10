#6 kyu
#Delete occurrences of an element if it occurs more than n times.

#Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

#EXAMPLE
#  delete_nth ([1,1,1,1],2) # return [1,1]

#  delete_nth ([20,37,20,21],1) # return [20,37,21]

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
    
#OR

def delete_nth(lst, N):
  itemCounts = {}
  result = []
  for num in lst:
    count = itemCounts.get(num, 0) 
    if count < N:
      result.append(num)
      itemCounts[num] = count + 1
  print(itemCounts)
  return result


#EXAMPLE

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
