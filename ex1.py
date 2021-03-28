from fuzzywuzzy import fuzz


Str1 = "Apple Inc."
Str2 = "apple Inc"

ratio = lambda x, y: fuzz.ratio(Str1.lower(),Str2.lower())


if __name__ == "__main__":
    print(ratio(Str1, Str2))