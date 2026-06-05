"""

Write a function nanana_batman() that accepts an integer x
and prints the string "nanana batman!" where "na" is repeated x times.
Do not use the * operator.

UNDERSTAND:
    * Input: integer x
    * Output: string "nanana batman!" where "na" is repeated x times

    * questions about the problem?

    * edge cases?
    - x < 0 (negative numbers), null, None, invalid data type (string) --> print("error: invalid input")
    - x = 0     (should print "batman!")
    - large numbers


MATCH:    * similar problems?

PLAN
1. validate input
2. initialize result as empty string
3. init a for loop that runs x times and adds "na" to result in each iteration
4. check if x is 0, if so return "batman!"
5. add " batman!" to result and return result

IMPLEMENT:
- see below

REVIEW:
- will do next class

EVALUATE:
    * runtime and complexity? (will do next class)


"""


## IMPLEMENT
def nanana_batman(x):
    result = ""

    if x < 0:
        return("error!")

    for _ in range(x):
        result += "na"
    if result:
        return(result+ " batman!")
    else:
        return("batman!")


## TESTS
print(nanana_batman(-10))