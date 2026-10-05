def solution(n, arr):
    expsum = 0
    for i in range(1, n + 1):
        expsum += i
    actsum = 0

    for j in range(len(arr)):
        actsum += arr[j]
        
    return expsum - actsum

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:]]
    print(solution(n, arr))

if __name__ == '__main__':
    main()