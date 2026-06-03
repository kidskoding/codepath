def prob05() -> None:
    # 1. Create another integer variable called sum
    # 2. Loop through your items list
        # 2.1. Update the sum variable to the current sum plus the current item in the list
    # 3. Return the final sum value

    # Time: O(n)
    # Space: O(1)

    def sum_honey(hunny_jars: list[int]) -> int:
        sum = 0
        for jar in hunny_jars:
            sum += jar

        return sum

    sum_honey([2, 3, 4, 5])