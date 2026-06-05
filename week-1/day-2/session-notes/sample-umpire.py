'''

Write a function nanana_batman() that accepts an integer x
and prints the string "nanana batman!" where "na" is repeated x times.

How to solve via UMPIRE (Understand, Match, Plan, Implement, Review, Evaluate)

UNDERSTAND (U):
    * Input: an integer x
    * Output: a string "nanana batman!" where "na" is repeated x times

    * questions about the problem?

    * edge cases?
        - negative numbers, floating point numbers
        - string -> print("error! invalid input")
        - large numbers
        - 0 --> ("batman!")
        - non-numeric

MATCH (M):  * similar problems?

PLAN (P):
    1. validate the input
    2. initialize the result string
    3. use a for loop that runs x times
    4. add "na" x times to result
    5. check if result is empty, if yes add "batman!" else add " batman!"

IMPLEMENT (I):


REVIEW (R):
    

EVALUATE (E):
    
'''

## IMPLEMENT
def nanana_batman(x: int) -> str:
    result = ""

    if x < 0:
        return "error! invalid input"
    for i in range(x):
        result += "na"
    if result:
        return result + " batman!"
    else:
        return "batman!"
