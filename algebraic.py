# //before optimization
((a + b) * c) + (d * (e + 0)) - (f * 1)

# //after optmization
((a + b) * c) + (d * e) - f

# Remove addition of zero:
# The expression "(e + 0)" simplifies to just "e".
# So, the expression becomes:
# ((a + b) * c) + (d * e) - (f * 1)
# Remove multiplication by one:
# The expression "(f * 1)" simplifies to just "f".
# So, the expression becomes:
# ((a + b) * c) + (d * e) - f
# Replace multiplication by zero with zero:
# There's no multiplication by zero in our expression, so no change here.
# Remove multiplication or addition with zero operands:
# There are no multiplication or addition operations involving zero operands in our expression, so no change here.