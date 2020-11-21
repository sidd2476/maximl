
def longestsub(strr): 
      
    n = len(strr) 
      
    res = 0 
      
    for i in range(n): 
        for j in range(i, n): 
            if (different(strr, i, j)): 
                res = max(res, j - i + 1) 
                  
    return res 
  
def different(strr, i, j): 
    visited = [0] * (26) 
  
    for k in range(i, j + 1): 
        if (visited[ord(strr[k]) - 
                   ord('a')] == True): 
            return False
              
        visited[ord(strr[k]) -
                ord('a')] = True
  
    return True


      
strr = input()
      
len = longestsub(strr) 
print(len)
