__author__ = 'Eli Sobylak'
import re
dict_A = ("""
                    A
                   A A
                  A   A
                 A     A
                AAAAAAAAA
               A         A
              A           A
          """)

def main():
    word = raw_input(str(("Please Enter a phrase to be Lettered: ")))
    split = word.split()
    testlet = 'a'
    #if re.search(r'[A-Z]',split) in split is True:
       # print "Entery must be all in lower-case!"
    if split[0] == testlet:
         print(dict_A)
    print(split[0])


main()
