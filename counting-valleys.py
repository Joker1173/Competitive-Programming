def countingValleys(steps, path):
    valleys=0
    tmp=0
    for i in range(steps):
        if path[i] =="D":
            tmp-=1
        else:
            tmp+=1
        if tmp==-1 and path[i+1]=="U":
            valleys+=1
    return valleys
