def check_armstrong(num):
    num_digit = len(str(num))
    d= num
    sum=0
    while d !=0:
        r = d % 10
        sum =sum + r**(num_digit)
        d = d // 10
    if  sum == num:
        return True
    else:
        return False

print(check_armstrong(153))