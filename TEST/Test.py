k_l = input()

k,l = k_l.split(" ")
k = int(k)
l = int(l)

if (k<1):
    k = 1
elif (k>1000):
    k = 1000
if (l<0):
    l = 0
elif (l>1000000):
    l = 1000000
arr = list()

for i in range(0,l):
    m_n = input()
    m,n = m_n.split(" ")
    m = int(m)
    n = int(n)
    if (m < 1):
        m = 1
    elif (m > k):
        k = k
    if (n < 1):
        n = 0
    elif (l > k):
        l = k
    arr.append((m,n))

arrNum = set()

for i in arr():
    arrNum.add(i[0])
    arrNum.add(i[1])

arrNum = list(arrNum)

arrDic = dict()



