dna = input("Enter a DNA sequence: ")
dna = dna.upper()
if dna == "":
    print("Please enter a DNA sequence")
    exit()

for letter in dna:
    if letter not in "ATGC":
        print("Invalid DNA sequence")
        exit()

print("Valid DNA sequence")

complement = ""
for letter in dna:
    if letter == "A":
        complement += "T"
    elif letter == "T":
        complement += "A"
    elif letter == "G":
        complement += "C"
    elif letter == "C":
        complement += "G"

reverse_complement = complement[::-1]   

print("Original DNA:", dna)
print("Complement DNA:", complement)
print("Reverse Complement DNA:", reverse_complement)


