def is_palindrome(word):
    if word.lower()==word[::-1].lower():
        return 1
    else:
        return 0

    


def main():
    word=input("Enter a word: ")
    result=is_palindrome(word)
    if result == 1:
        print("Your word is a palindrome.")
    else:
        print("Your word is not a palindrome.")

if __name__ == "__main__":
    main()