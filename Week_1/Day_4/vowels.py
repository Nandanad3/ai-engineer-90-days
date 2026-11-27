s=input("Enter a string:")
vowels=0
consonants=0
for i in range(0,len(s)):
    if s[i].lower() in "aeiou":
        vowels +=1
    else:
        consonants +=1
print(f"Number of vowels:{vowels}")
print(f"Number of consonants:{consonants}")