file = open('sample_dna.txt', 'r')
dna = file.read()
print("DNA: ", dna)

rna = ""
conv_dna = ""
for i in dna:
    if i == "a" or i == "A":
        conv_dna += "A"
    elif i == "t" or i == "T":
        conv_dna += "T"
    elif i == "g" or i == "G":
        conv_dna += "G"
    elif i == "c" or i == "C":
        conv_dna += "C"
    else:
        continue
for i in conv_dna:
    if i == "T":
        rna += "U"
    else:
        rna += i
        
print("RNA: ", rna)

RNA_string = open('sample_rna.txt', 'a')
for i in rna:
    RNA_string.write(i)

print("New File Containing RNA Seq Created")
    
