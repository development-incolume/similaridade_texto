from fuzzywuzzy import fuzz


Str1 = "Los Angeles Lakers"
Str2 = "Lakers"
Ratio = lambda Str1, Str2: fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = lambda Str1, Str2: fuzz.partial_ratio(Str1.lower(),Str2.lower())

if __name__ == "__main__":
    print(Ratio)
    print(Partial_Ratio)