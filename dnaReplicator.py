__author__ = 'Eli Sobylak'

#Returns complementary DNA sequence for a given input
#adenine = "A"
#thymine = "T"
#cytosine = "C"
#guanine = "G"


input = raw_input("Enter a DNA sequence (ex.ATCG): ")

def main():
    print input.replace("A","%temp%").replace("T","A").replace("%temp%", "T").replace("C","%temp%").replace("G","C").replace("%temp%", "G")

main()
