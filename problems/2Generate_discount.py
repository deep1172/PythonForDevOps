n =int (input("Enter the amount "))


if n>=100 and n<1000:
    print ("You will get 10% Discount and You bill is ", n*0.90)

elif n>=1000 and n<5000:
    print ("You will get 15% Discount and You bill is ", n*0.85)

elif n>=5000 and n<10000:
    print ("You will get 20% Discount and You bill is ", n*0.80)

elif n>=10000:
    print ("You will get 25% Discount and You bill is ", n*0.75)

else:
    print ("oops, No Discount is Available")
