def is_palindrome(text):
    txt_lower = []
    for i in text:
        if i not in [' ', ',', '.', '!', '?', '-']:
            txt_lower.append(i.lower())
    pure_text = ''.join(txt_lower)
    print('pure text', pure_text)
    print('reversed text', pure_text[::-1])
    return pure_text == pure_text[::-1]
    # for j in range(pure_text):

txt = input()


print(is_palindrome(txt))