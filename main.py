in_number=int(input("please enter your number:   ")) 
if in_number<=0:print(in_number)
elif in_number==1:print(in_number)
else:
    for i in range(2,in_number+1):
            flag=0
            for j in range(2,i):
                if i%j==0:
                    flag=1
            if flag==0:
                print(i)
        
