#python program to find weather the word is palindrome or not
word = input("write any word").split()
if word == word[::-1]:
    print("Number is palindrome")
else:
    print("not palindrome")