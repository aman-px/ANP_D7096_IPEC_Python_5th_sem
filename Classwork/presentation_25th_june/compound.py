P = float(input("Principal: "))
r = float(input("Rate (%): ")) / 100
t = float(input("Time (years): "))
n = int(input("Compounds per year: "))

A = P * (1 + r/n) ** (n*t)
CI = A - P

print("Amount =", round(A, 2))
print("Compound Interest =", round(CI, 2))