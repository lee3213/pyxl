


sum=0
for i in range(1,101):
    
    sum=sum+i
    print(i,sum)

sum=0
count_i=0
under_100=True
while under_100:
    count_i=count_i+1
    sum=sum+count_i
    if count_i > 100:
        under_100=False
    print(count_i,sum)

sum=0
count_i=0
under_100=True
while under_100:
    count_i=count_i+1
    sum=sum+count_i
    if count_i == 100:
        under_100=False
    print(count_i,sum)
