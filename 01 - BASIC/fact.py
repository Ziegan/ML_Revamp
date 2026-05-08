n = int(input("enetr the given no"))
fact = 1

for i in range(1, n+1):
      fact *= i
      print("progress:", fact, i)
print(fact)

