

# STRING REPLACEMENT SAY BOX

# EXAMPLE 1: GREETING USE CASE
name = "Daniel" # ← box input
greeting = "Hello %s nice to meet you" % name 
# Output: "Hello Daniel nice to meet you"
greeting = "Nice to meet you %s" % name 
# Output: "Nice to meet you Daniel"


# EXAMPLE 2: FAVORITE COLOR USE CASE
name = "blue" # ← box input
favorite_color_reaction = "%s is my favorite color too" % name
# Output: "blue is my favorite color too"
