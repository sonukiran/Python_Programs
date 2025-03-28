#program to reverse each string in a sentence
def reveresestring(sentence):
    return ''.join(word[::-1] for word in sentence.split())

sentence = "Hello world"
print(reveresestring(sentence))  # Output: olleH dlrow