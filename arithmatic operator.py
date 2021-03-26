print("1.ADDITION");
print("2.SUBTRACTION");
print("3.MULTIPLICATION");
print("4.DIVISION");
print("5.EXIT");
choice=int(input("enter your choice:"));
if(choice>=1 and choice<=4):
     print("enter two numbers:");
num1=int(input());
num2=int(input());
if choice==1:
     res=num1+num2;
     print("Result =", res);
elif choice==2:
      res=num1-num2;
      print("result=",res);
elif choice==3: 
      res = num1 * num2;
      print("Result=", res);
elif choice==4:
      res=num1/num2;
      print("Result=", res);
elif choice== 5:
     exit();
    
else:
    print("Wrong input..!!"); 
