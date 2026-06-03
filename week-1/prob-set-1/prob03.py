def prob03() -> None:
    # 1. Store the valid catchphrases
    # 2. Check if the character string has a valid catchphrase
    #   2.1. If so , simply return the catchphrase
    #   2.2. Otherwise, just return the sorry message
    
    # Time: O(n)
    # Space: O(1)

    def print_catchphrase(character: str) -> str:
        catchphrases = {
            "Pooh": "Oh bother!",
            "Tigger": "TTFN: Ta-ta for now!",
            "Eeyore": "Thanks for noticing me.",
            "Christopher Robin": "Silly old bear."
        }
    
        if character in catchphrases:
            return catchphrases[character]
        else:
            return f"Sorry! I don't know {character}'s catchphrase!"

    print_catchphrase("Pooh")
    print_catchphrase("Piglet")
    print_catchphrase("Oh bother!")
