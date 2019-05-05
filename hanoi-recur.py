
def move(n, src, dest, tmp, count):
    if n > 0:
        move(n-1, src, tmp, dest, count)
        count[0] += 1
        print("moving from {} to {} with temp as {}".format(src, dest, tmp))
        move(n-1, tmp, dest, src, count)
    

count = [0]
move(5, 1, 2, 3, count)
print("total moves = {}".format(count[0]))

