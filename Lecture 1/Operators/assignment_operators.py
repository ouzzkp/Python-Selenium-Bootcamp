# Operators used in assignment. It is the “=” operator that we use the most.

# = Transfers the right-hand value or an operation performed on the right-hand side to the left-hand side. c = a + b, the result is transferred to variable c.
# += adds the right-hand value over the left-hand side and the new result is found in the left-hand value. The result of a += b, a + b is reflected in the variable a.
# -= Subtracts the left-hand value from the right-hand value and the new result is found in the left-hand value. The result of a += b, a – b is reflected in the variable a.
# *= Multiplies both sides, the result is transferred to the variable on the left. The result a *= b, a * b is reflected in the variable a.
# /= Divides the left-hand value by the right-hand side, the result is reflected in the left-hand value. a /= b, a / b result is reflected in variable a.
# %= Performs modding, the result is reflected on the left. The result of a %= b, a % b is reflected in variable a.
# **= Performs an override, the result is reflected on the left. The result a **= b, a ** b is reflected in the variable a.
# //= Performs rounding, the result is reflected to the left. The result of a //= b, a // b is reflected in the variable a.

a,b = 10,20

print(a) # 10

a += b

print(a) # 30

