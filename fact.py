def firstFact(num):

    num = (int(num))
    fact = num
    fa = num
    nums = []

    while num > 1:
        num -=1
        nums.append(num)

    for x in nums:
        fact = x * fact
    print("the factorial of %s is: " % fa)
    print(fact)

w = input ("This will tell you the factorial of a number\nEnter a number won't you ")
firstFact(w)
