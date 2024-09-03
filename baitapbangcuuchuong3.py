while True:
    n=int(input("nhập từ 2 đến 10 [2,10]:"))
    if n>=2 and n<=10:
        break
    else:
        print("nhập sai, nhập lại")
i=1
while i<=10:
    print("{0}*{1}={2}".format(i,n,i*n))
    i=i+1