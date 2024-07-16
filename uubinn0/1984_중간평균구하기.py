T = int(input())

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    
    num.remove(max(num))
    num.remove(min(num))
    
    print(f'#{test_case} {sum(num) / len(num):.0f}')