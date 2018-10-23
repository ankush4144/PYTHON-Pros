print("result calculator")
print("enter the marks for the three subject exams")
s1=int(input())
s2=int(input())
s3=int(input())
s=(s1+s2+s3)/3
tot=0
tot=tot+s
print("enter the three activities marks out of 50")
a1=int(input())
a2=int(input())
a3=int(input())
a=((a1+a2+a3)/150)*100
a=(30*a)/100
tot=tot+a
print("enter the sportsactivity marks out of 100")
sp=int(input())
sp=(20*sp)/100
tot=tot+sp
print("final result for the student comes out to be :",tot,"\%")
