# 입력 받기
N = int(input());
M = int(input());
numbers = list(map(int, input().split()));

# 입출력 예시
# 입력
# 6
# 9
# 2 7 4 1 5 3
# 출력
# 2

# 시간 초과 코드(O(n^2))
# count = 0;
# for i in range(0, N):
#   for j in range(i, N-1) :
#     if numbers[i] + numbers[j] == M :
#       count += 1;
# print(count);


# 파이썬 내장 정렬 함수(Timesort, O(nlogn))
numbers.sort() # 오름차순 정렬
left = 0
right = N - 1
count = 0

# 투 포인터 알고리즘(O(n))
while left < right:
    s = numbers[left] + numbers[right]

    if s == M:
        count += 1
        left += 1
        right -= 1
    elif s < M:
        left += 1
    else:
        right -= 1

print(count)