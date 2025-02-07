# AREA(Int)
# CP(I):
#   x >= 0
#   y > 0
# ECP
r = x
q = 0
while y <= r:
    # CP(1):
    #   x == q * y + r
    # ECP
    r -= y
    q += 1
# CP(E):
#   x == q * y + r
#   r < y
# ECP
