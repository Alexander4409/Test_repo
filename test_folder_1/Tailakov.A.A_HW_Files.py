# Task 1
# with open(file='file1.txt', mode='r', encoding='utf-8') as file1, \
#         open(file='file2.txt', mode='r', encoding='utf-8') as file2:
#     line1 = file1.readlines()
#     line2 = file2.readlines()
#
# for i, (line1, line2) in enumerate(zip(line1, line2)):
#     if line1 != line2:
#         print(f"string {i+1}: {line1.strip()} (from first file) does not match {line2.strip()} (from second file)")


# Task 2
# with open(file='file1.txt', mode='r', encoding='utf-8') as file1, \
#         open(file='file2.txt', mode='w', encoding='utf-8') as file2:
#     content = file1.read()
#
#     count_chars = len(content)
#     count_lines = content.count('\n') + 1
#     count_vowels = sum([1 for char in content if char in 'aeiouyAEIOUY'])
#     count_consonant = sum([1 for char in content if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'])
#     count_digit = sum([1 for char in content if char in '0123456789'])
#
#     file2.write(f'Symbols: {str(count_chars)}; \nStrings: {count_lines}; \nVowels: {count_vowels}; \nConsonants:'
#                 f' {count_consonant}; \nЦифр: {count_digit}')


# Task 3
# with open("file.txt", "r") as file:
#     lines = file.readlines()
#
# with open("file2.txt", "w") as file2:
#     file2.writelines(lines[:-1])


# Task 4
# with open(file='file1.txt', mode='r', encoding='utf-8') as file:
#     min_length = 0
#     min_string = ''
#
#     for line in file:
#         length = len(line.strip())
#         if length < min_length:
#             min_length = length
#             min_string = line.strip()
#
# print(f'The longest string is: {min_line}, its length: {min_length}')


# Task 5
# with open(file='file1.txt', mode='r', encoding='utf-8') as file:
#     content = file.read()
#     count_words = content.count(input('Enter the words: '))
#     print(count_words)


# Task 6
# with open(file='file1.txt', mode='r+', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
#
#     search_word = input('Enter the word which you want to find: ')
#     if search_word in content:
#         replace_word = input('Enter the new word: ')
#         content = content.replace(search_word, replace_word)
#         print(f'Replacement successful!. \nNew date: {content}')
#     else:
#         print('The word not found!')
#
#     file.seek(0)
#     file.write(content)
#     file.truncate()
