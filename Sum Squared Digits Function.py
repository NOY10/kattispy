num = int(input())
arr = []

for i in range(num):
    lis = list(map(int,input().split()))
    sum = 0

    se = lis[2]
    fi = lis[1]

    while(se > 0):
        ans = se % fi
        sum = sum + pow(ans,2)
        se = se // fi
    arr.append(sum)

for i in range(num):
    print(f'{i+1} {arr[i]}')

