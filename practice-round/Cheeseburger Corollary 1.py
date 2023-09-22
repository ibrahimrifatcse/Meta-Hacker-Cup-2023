T = int(input())

for i in range(1, T+1):
    S, D, K = map(int, input().split())
     
    Total_Buns = S*2 + D*2
    Total_Meat = S*1 + D*2
     
    if Total_Buns >= K+1 and Total_Meat >= K:
        print(f'Case #{i}: YES')
    else:
        print(f'Case #{i}: NO')
    
    
