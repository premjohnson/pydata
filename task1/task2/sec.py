
#palind
text = input("enter a string: ")
if text == text[::-1]:
    print("the input is a palin")
else:
    print("the input is not a palin")

#vowel in pro
text = input("rnter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("rumber of vowels:", count)

#leep year
year = int(input("enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("it is a leap year")
else:
    print("it is not a leap year")
