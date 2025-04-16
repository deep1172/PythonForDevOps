
def prime():
    n = int(input("Enter the number till which you want prime ")) 
    primeNo =[]
    for i in range(2, n+1):
        is_prime =True
        for j in range(2, int(i**0.5) +1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primeNo.append(i)

    print("Prime numbers up to", n, "are:", primeNo)
    
prime()



