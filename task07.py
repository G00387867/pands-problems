# Adam
# A program that reads in a text
#  file and outputs the number of e's it contains
# The program takes the filename from 
# an argument on the command line.
# I found information on this website:
# https://www.sanfoundry.com/python-program-read-file-counts-number/

#fname = input("Enter file name: ")
#l = input("Enter letter to be searched: ")
#e = 0

#with open(fname, "r") as f:
    #for line in f:
        #words = line.split()
        #for i in words:
            #for letter in i:
                #if(letter == l):
                    #e = e+1

#print("Occurences of the letter: ")
#print(e)

# Requirement for this assignmnet is to only print
#  The occurence of letter E

fname = input("Enter file name: ")
e = 0

with open(fname, "r") as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter == "e"):
                    e = e+1
print(e)

  
                


  


