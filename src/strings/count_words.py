import re


def count_words(s):
    pattern = re.compile("\w+")
    words =re.findall(pattern, s)
    count =0
    for word in words:
        count+=1
        print(word)
    return count


test_string = "Geeksforg`eeks,    is best @# Computer Science Portal.!!!"

print(count_words(test_string))
