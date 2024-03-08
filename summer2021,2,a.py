info_list = ["Shikha", "Muzam", "Haua", "01971700130"]

combined_string = ''.join(info_list)

total_characters = len(combined_string)
total_vowels = sum(combined_string.count(vowel) for vowel in 'aeiouAEIOU')

print("Total number of characters in the list:", total_characters)
print("Total number of vowels in the list:", total_vowels)
