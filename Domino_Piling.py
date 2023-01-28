    l=input()    //take two int input from the user.
    i = int(l.index(" "))    //find the index of the first space=" "
    x=int(l[:i])               //set x to the number before the space
    y=int(l[i+1:])            //set y to the number after the space
    if (x * y)%2 == 0:
        print((x*y)//2)
    else:
        print(((x*y)-1)//2)
