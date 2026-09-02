def edit_distance(a, b):
    pass
def edit_distance(a, b):
    m, n = len(a), len(b)
    
    
    dp = list(range(n + 1))
    
    for i in range(1, m + 1):
        prev_diag = dp[0]
        
        dp[0] = i
        
        for j in range(1, n + 1):
            temp = dp[j]
            
            if a[i - 1] == b[j - 1]:
                
                dp[j] = prev_diag
            else:
                dp[j] = 1 + min(
                    dp[j - 1],  
                    dp[j],      
                    prev_diag   
                )
            
            prev_diag = temp
            
    return dp[n]