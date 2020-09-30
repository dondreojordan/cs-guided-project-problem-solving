def lambda_school(n):
    return [str(i) if i % 3 and i % 5 else "FizzBuzz" if not i % 15 else "Buzz" if not i % 5 else "Fizz" for i in range(1, n + 1) ]

n = 15
print(lambda_school(n))