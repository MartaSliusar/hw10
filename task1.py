import string
def paliandrom(s):
    punctuation = string.punctuation
    result = ''

    for i in s:
        if i not in punctuation:
            result += i

    result = result.lower()
    result = result.replace(' ', '')

    reverse = result[::-1]
    return result == reverse

s = 'A man, a plan, a canal: Panama'
print(paliandrom(s))
