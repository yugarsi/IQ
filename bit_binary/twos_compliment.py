# These are Python's bitwise operators.

# Preamble: Twos-Complement Numbers
# All of these operators share something in common -- they are "bitwise" operators. That is, they operate on numbers (normally), but instead of treating that number as if it were a single value, they treat it as if it were a string of bits, written in twos-complement binary. A two's complement binary is same as the classical binary representation for positve integers but is slightly different for negative numbers. Negative numbers are represented by performing the two's complement operation on their absolute value. So a brief summary of twos-complement binary is in order:

# Two's Complement binary for Positive Integers:

# 0 is written as "0"
# 1 is written as "1"
# 2 is written as "10"
# 3 is "11"
# 4 is "100"
# 5 is "101"
# .
# .
# 1029 is "10000000101" == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1
# Two's Complement binary for Negative Integers:

# Negative numbers are written with a leading one instead of a leading zero.
#  So if you are using only 8 bits for your twos-complement numbers,
#   then you treat patterns from "00000000" to "01111111" as the whole numbers from 0 to 127, 
#   and reserve "1xxxxxxx" for writing negative numbers. A negative number, -x, is written using 
#   the bit pattern for (x-1) with all of the bits complemented (switched from 1 to 0 or 0 to 1). 
#   So -1 is complement(1 - 1) = complement(0) = "11111111", and -10 is 
#   complement(10 - 1) = complement(9) = complement("00001001") = "11110110". 
#   This means that negative numbers go all the way down to -128 ("10000000").

# Of course, Python doesn't use 8-bit numbers. 
# It USED to use however many bits were native to your machine, 
# but since that was non-portable, it has recently switched to using an INFINITE number of bits.
#  Thus the number -5 is treated by bitwise operators as if it were written "...1111111111111111111011".

# Whew! With that preamble out of the way (and hey, you probably knew this already), 
# the operators are easy to explain: