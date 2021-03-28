from fuzzywuzzy import process

str2Match = "apple inc"
strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]


Ratios = lambda str1, options: process.extract(str1, options)
highest = lambda str1, options: process.extractOne(str1, options)


if __name__ == "__main__":
    print(Ratios(str2Match,strOptions))
    # You can also select the string with the highest matching percentage
    print(highest(str2Match,strOptions))