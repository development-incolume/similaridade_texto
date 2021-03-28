from fuzzywuzzy import fuzz

Str1 = "The supreme court case of Nixon vs The United States"
Str2 = "Nixon v. United States"

Ratio = lambda Str1, Str2: fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = lambda Str1, Str2: fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = lambda Str1, Str2: fuzz.token_sort_ratio(Str1,Str2)
Token_Set_Ratio = lambda Str1, Str2: fuzz.token_set_ratio(Str1,Str2)

if __name__ == "__main__":
    print(Ratio)
    print(Partial_Ratio)
    print(Token_Sort_Ratio)
    print(Token_Set_Ratio)