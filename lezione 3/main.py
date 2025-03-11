
# In Python, a "literal" is a data value specified directly in the code

print(15_000_000_000_000) # syntax that helps us writing big numbers
print(0b01001010110101) # for binary numbers
print(0o041324567) # for octal
print(0xFFF012) # for hex
print(15e9) # 15*10 to the power of 9

var = 1
type(var) #returns the value of the argument passed

# string methods

title = "Il Signore degli Anelli"
print(title)
title = "Il Signore degli Anelli".upper() # all uppercase
print(title)
title = "Il Signore degli Anelli".lower() # all low
print(title)
title = "Il Signore degli Anelli".capitalize() # make the first character have upper case and the rest lower case
print(title)
title = "Il Signore degli Anelli".title()
print(title)
title = "      Il Signore degli Anelli        ".title()
print(title)
title = "Il Signore degli Anelli".replace("Signore", "Padrone", 1) #In this case only the first occurrence gets substituted
print(title)
is_alpha = "      Il Signore degli Anelli        ".isalpha() # returns false if there is non alphabetical values, included whitespaces
print(is_alpha)
print(111)
is_digit = "      Il Signore degli Anelli        ".isdigit() # returns false if there is non numerical values, included whitespaces
print(is_digit)
count = "      Il Signore degli Anelli        ".count("Anelli") # returns how many occurrences of the substrings are in the string
print(count)
# WE NEVER HAVE INPLACE METHODS FOR STRINGS IN PYTHON

# function => Independent from an object
# method => Dependent from an object