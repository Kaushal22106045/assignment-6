#checking the palindrome
chk_str = input("Enter a word/phrase: ")
chk_str = chk_str.replace(" ","")
for i in range (len(chk_str)//2):
    if (chk_str[i] != chk_str[-i-1]):
        print("The given word/phrase is not a palindrome")
        break
else :
    print ("Entered word/phrse is a palindrome")
