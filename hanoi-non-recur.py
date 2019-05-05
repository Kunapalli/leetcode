
def move(n, src, dest, tmp):
    stack = []
    count = 0
    while n > 0:
        stack.append((n, src, dest, tmp))
        (dest, tmp) = (tmp, dest)
        n -= 1
    
    while stack:
        (n, src, dest, tmp) = stack.pop()
        count += 1
        print("moving from {} to {} with temp as {}".format(src, dest, tmp))
        while n > 1:
            stack.append((n-1,tmp,dest,src))
            (dest, src) = (src, dest)
            n -= 1

    print("total moves = {}".format(count))
    
move(5,1,2,3)

