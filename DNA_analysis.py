sample = ['GTA', 'GGG', 'CAC']

def read_dna(dna_file):
	dna_data = ""
	with open(dna_file) as f:
		for line in f:
			dna_data += line
	return dna_data
	
def dna_codons(dna):
	codons = []
	for i in range(0, len(dna), 3):
		if i + 3 < len(dna):
			codons.append(dna[i:i + 3])
	return codons

def match_dna(dna):
	matches = 0
	for codon in dna:
		if codon in sample:
			matches += 1
	return matches

def is_criminal(dna_sample):
	dna_data = read_dna(dna_sample)
	codons = dna_codons(dna_data)
	num_matches = match_dna(codons)
	if num_matches > 3 or num_matches == 3:
		print(str(num_matches) + " matches : " + dna_sample + " (TRUE)")
	else:
		print(str(num_matches) + " matches : " + dna_sample + " (FALSE)")
		
suspects_dna_data = ['suspect_1.txt', 'suspect_2.txt', 'suspect_3.txt']
for d in suspects_dna_data:
	is_criminal(d)

	

	
	
			
