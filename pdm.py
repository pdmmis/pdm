basic=int(input("your basic salary:"))
hra=float(input("enter your HRA (in percent):"))
hra=basic*hra/100
da=float(input("enter your DA (in percent):"))
da=basic*da/100
net=basic+hra+da
print("your gross salary is:",net)
