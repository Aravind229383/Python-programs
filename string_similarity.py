
str1 = input("Enter String 1 \n").lower()
str2 = input("Enter String 2 \n").lower()

if len(str2) < len(str1):
     short = len(str2)
     long = len(str1)
else:
     short = len(str1)
     long = len(str2)

match_count = 0
for i in range(short):
    if str1[i] == str2[i]:
        match_count += 1

print("Similarity between two said strings:")
print(match_count/long)
