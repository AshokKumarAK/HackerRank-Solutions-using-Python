year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("12.09."+str(year))
else:
    print("13.09."+str(year))