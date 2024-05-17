from package_reason import my_default_dict

def count_characters(sentence):
    char_count = {}
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def charCount(sen):
    dd = my_default_dict(int)
    for letter in sen:
        dd[letter] += 1
    return dd

# def charCount(sen):
#     dd = defaultdict(int)
#     for letter in sen:
#         dd[letter] += 1
#     return dd
# sen = "reasonn"
# print(charCount(sen))



# def counting_char(char):
#     counter = Counter(char)
#     return counter
# char = "reason"
# print(counting_char(char))