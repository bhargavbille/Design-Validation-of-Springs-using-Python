import sys
from sys import exit
print("\t\t\t     'Design of Springs'\nSelect the type of Sping you need to Design,")
dmm = input("1. Helical Spring\n2. Conical Springs\n3. Torsional Springs\n.......... : ")
if dmm == "1":
    import helical_spring
elif dmm == "2":
    import conical_spring
elif dmm == "3":
    import torsional_springs
else:
    if input("Sorry wrong Option\nIf you want to try again press 's' or else press any key : ") == 's':
        import design_of_springs
    else:
        sys.exit("\t\tThank You")
print("\t\tThank You")
