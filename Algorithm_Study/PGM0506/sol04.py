
def solution(stones, k):
    answer = 0
    left = 0 
    right = 200000000
    while left <= right :
        mid = (left+right)//2
        cnt = 0 
        for stone in stones :
            if stone <= mid :
                cnt += 1
            else :
                cnt = 0
            if cnt >= k :
                break
        if cnt >= k :
            right = mid - 1
        else :
            left = mid + 1
    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))