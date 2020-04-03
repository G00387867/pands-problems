# program asks a user to input a string and outputs 
# every second letter in reverse order


sentence = str(input("please Enter a Sentence: "))

reverseSentence = sentence[ : :-1] # reverse the sentence

print(reverseSentence[ : :2]) # prints every second letter
