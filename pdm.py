b=int(input("your basic salary:"))
hra=float(input("enter your HRA (in percent):"))
hra=b*hra/100
da=float(input("enter your DA (in percent):"))
da=b*da/100
net=b+hra+da
print("your gross salary is:",net)
