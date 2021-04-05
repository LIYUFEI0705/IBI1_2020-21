seq='ATGCGACTACGATCGAGGGCC'
AAcode={'TTT':'F', 'TTC':'F', 'TTA':'L', 'TTG':'L', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'CCT':'P', 'CCA':'P', 'CCA':'P', 'CCG':'P', 'ATT':'I', 'ATC':'I', 'ATA':'J', 'ATG':'M', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V', 'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'TAT':'Y', 'TAC':'Y', 'TAA':'O', 'TAG':'U', 'TGT':'C', 'TGC':'C', 'TGA':'X', 'TGG':'W', 'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Z', 'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AAT':'N', 'AAC':'B', 'AAA':'K', 'AAG':'K', 'AGT':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
output=""
for i in range(1,len(seq),3):
    a=seq[i-1:i+2]
    b=AAcode[a]
    output=output+b
print(output)


