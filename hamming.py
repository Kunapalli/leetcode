def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """

    t = x ^ y
    count = 0
    d = { 0:0, 1:1, 2:1, 3: 2, 4:1, 5:2, 6:2, 7:3, 8:1, 9:2, 10:2, 11:2, 12:2, 13:3, 14:3, 15:4, 16:1}
    while t != 0:
        x = t & 0x0000000f
        count += d[x]
        t = t >> 4
    return count

print(hammingDistance(15, 16))
