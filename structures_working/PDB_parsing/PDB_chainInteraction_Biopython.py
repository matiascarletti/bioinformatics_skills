from Bio import PDB
parser = PDB.PDBParser()
s = parser.get_structure("2H8L","2H8L.pdb")
first_model = s[0]
chain_A = first_model["A"]
chain_B = first_model["B"]
for res1 in chain_A:
    for res2 in chain_B:
        d = res1["CA"]-res2["CA"]
        if d <= 6.0:
            print res1.resname,res1.get_id()[1], res2.resname,\
                res2.get_id()[1], d