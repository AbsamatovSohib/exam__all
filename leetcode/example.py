def lengthOfLastWord(s):
    s = s.strip()
    m = s.split(" ")
    return len(m[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))
