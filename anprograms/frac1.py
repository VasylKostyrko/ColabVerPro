x = 16
y = 3

# AREA(Int)
# CP(I):
# ECP
r = x
q = 0
while y <= r:
    # CP(1):
    # ECP
    r -= y
    q += 1
# CP(E):
# ECP

print("q =", q, ", r =", r)
