gnames = []
gseqs = []

from sys import argv

with open(str(argv[1])+"_folder/CPhits.txt", 'r') as cp_seqs, open(str(argv[1]), 'r') as genome:
	cpnames = [line.strip() for line in cp_seqs]
	for line in genome:
		if line.startswith('>'):
			gnames.append(line.strip())
		else:
			gseqs.append(line.strip())

with open(str(argv[1])+"_folder/" + str(argv[1]) + "CP.fasta", 'w') as new:
	for i in range(len(gnames)):
		if gnames[i] in cpnames:
			new.write(gnames[i]+'\n'+gseqs[i]+'\n')
		else:
			pass

#print cpnames[:10]
#print gnames[:10]
#print gseqs[:10]

cp_seqs.close()
genome.close()
new.close()
