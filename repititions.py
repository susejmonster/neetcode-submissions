def solution(n):
    mx = 0 
    l = 0
    for r in range(len(n)):
        cnt = r - l
        if n[l]!=n[r] or cnt<0:
            l = r
            cnt=0
        if n[l]==n[r]:
            cnt+=1
        
        if cnt>mx:
            mx = cnt    
    return mx
def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = input_data[0]
    #arr = [int(x) for x in input_data[1:]]
    print(solution(n))

if __name__ == '__main__':
    main()