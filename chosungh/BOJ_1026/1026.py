import sys
input = sys.stdin.readline

num = int(input())
sum = 0

arr_A = list(map(int, input().split()))[:num]
arr_B = list(map(int, input().split()))[:num]

cp_arr_B = arr_B.copy()
cp_arr_A = arr_A.copy()

for i in range(num):
    cp_arr_B[i] = [cp_arr_B[i], i]

cp_arr_B.sort(reverse=True)
cp_arr_A.sort()

for i in range(num):
    sum += cp_arr_A[i] * cp_arr_B[i][0]
    cp_arr_A[i] = [cp_arr_A[i], cp_arr_B[i][1]]

for i in range(num):
    val = cp_arr_A[i][0]
    arr_A[cp_arr_A[i][1]] = val

print(sum)