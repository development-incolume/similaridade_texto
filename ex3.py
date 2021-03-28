from fuzzywuzzy import fuzz

Str1 = "united states v. nixon"
Str2 = "Nixon v. United States"


Ratio = lambda Str1, Str2: fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = lambda Str1, Str2: fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = lambda Str1, Str2: fuzz.token_sort_ratio(Str1,Str2)
if __name__ == '__main__':
    print(Ratio(Str1, Str2))
    print(Partial_Ratio(Str1, Str2))
    print(Token_Sort_Ratio(Str1, Str2))