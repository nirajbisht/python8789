if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr=[]
    lst=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(k+1):
                if (i+j+k!=n):
                    lst=[i,j,k]
                    arr.append(lst)
                else:
                    break
    print(arr)