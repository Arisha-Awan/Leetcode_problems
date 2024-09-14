# Count the Number of Consistent Strings
def countConsistentStrings(allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """
    allowed = sorted(allowed)

    def sort_str(x: str):
        return "".join(sorted(set(x)))

    def check_consistent(word):
        for char in word:
            if char not in allowed:
                return False
        return True

    count = 0
    for word in words:
        x = sort_str(word)
        consistent = check_consistent(x)
        if consistent:
            count += 1
    return count


# apraoch using boolean array
def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    # Create a boolean list to mark which characters are allowed
    is_allowed = [False] * 26

    # Mark all characters in 'allowed' as True in the is_allowed list
    for char in allowed:
        is_allowed[ord(char) - ord("a")] = True

    consistent_count = 0

    # Iterate through each word in the words list
    for word in words:
        is_consistent = True

        # Check each character of the current word
        for char in word:
            # If any character is not allowed, mark as inconsistent and break
            if not is_allowed[ord(char) - ord("a")]:
                is_consistent = False
                break

        # If the word is consistent, increment the count
        if is_consistent:
            consistent_count += 1

    return consistent_count


if __name__ == "__main__":
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    count = countConsistentStrings(allowed, words)
    print(f"consisitent strings {count}")
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    count = countConsistentStrings(allowed, words)
    print(f"consisitent strings {count}")
