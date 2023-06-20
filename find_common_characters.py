if not words:
        return []

    result = []
    first_word = words[0]

    # Iterate over each character in the first word
    for char in first_word:
        char_present = True

        # Check if the character is present in all other words
        for word in words[1:]:
            if char not in word:
                char_present = False
                break

        # If the character is present in all words, add it to the result
        if char_present:
            result.append(char)

    return result
