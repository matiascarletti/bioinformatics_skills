#%%
import os
os.getcwd()
os.chdir('/home/matias/bioinformatics_skills/sequences_working/analysis')
os.getcwd()
os.listdir()

#%% [markdown] 
## help(NCBIWWW.qblast)
# qblast(program, database, sequence, url_base='https://blast.ncbi.nlm.nih.gov/Blast.cgi', auto_format=None, composition_ba
# sed_statistics=None, db_genetic_code=None, endpoints=None, entrez_query='(none)', expect=10.0, filter=None, gapcosts=None
# , genetic_code=None, hitlist_size=50, i_thresh=None, layout=None, lcase_mask=None, matrix_name=None, nucl_penalty=None, n
# ucl_reward=None, other_advanced=None, perc_ident=None, phi_pattern=None, query_file=None, query_believe_defline=None, que
# ry_from=None, query_to=None, searchsp_eff=None, service=None, threshold=None, ungapped_alignment=None, word_size=None, sh
# ort_query=None, alignments=500, alignment_view=None, descriptions=500, entrez_links_new_window=None, expect_low=None, exp
# ect_high=None, format_entrez_query=None, format_object=None, format_ty
## Some useful parameters:
#      - program        blastn, blastp, blastx, tblastn, or tblastx (lower case)
#      - database       Which database to search against (e.g. "nr").
#      - sequence       The sequence to search.
#      - ncbi_gi        TRUE/FALSE whether to give 'gi' identifier.
#      - descriptions   Number of descriptions to show.  Def 500.
#      - alignments     Number of alignments to show.  Def 500.
#      - expect         An expect value cutoff.  Def 10.0.
#      - matrix_name    Specify an alt. matrix (PAM30, PAM70, BLOSUM80, BLOSUM45).
#      - filter         "none" turns off filtering.  Default no filtering
#      - format_type    "HTML", "Text", "ASN.1", or "XML".  Def. "XML".
#      - entrez_query   Entrez query to limit Blast search
#      - hitlist_size   Number of hits to return. Default 50
#      - megablast      TRUE/FALSE whether to use MEga BLAST algorithm (blastn only)
#      - short_query    TRUE/FALSE whether to adjust the search parameters for a
#                       short query sequence. Note that this will override
#                       manually set parameters like word size and e value. Turns
#                       off when sequence length is > 30 residues. Default: None.
#      - service        plain, psi, phi, rpsblast, megablast (lower case)

#%%
from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast('blastp', 'nr', 'MSVIKSDMKIKLRMEGTVNGHKFVIEGEGEGKPYEGTQTMNLKVKEGAPLPFAYDILTTAFQYGNRVFTKYPKDIPDYFKQSFPEGYSWERSMTFEDGGICTATSDITLEGDCFFYKIRFDGVNFPPNGPVMQKKTLKWEPSTEKMYVRDGVLMGDVNMALLLEGGGHYRCDFKTTYKAKKGVQLPDYHFVDHRIEILSHDKDYNNVKLYEHAVARSSLLP')

# %%
from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.04

for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
         if hsp.expect < E_VALUE_THRESH:
             print("****Alignment****")
             print("sequence:", alignment.title)
             print("length:", alignment.length)
             print("e value:", hsp.expect)
             print(hsp.query[0:75] + "...")
             print(hsp.match[0:75] + "...")
             print(hsp.sbjct[0:75] + "...")

# %% [markdown] 
# nowork
# from Bio.Blast import NCBIXML
# blast_records = NCBIXML.parse(result_handle)
# blast_record = next(blast_records)

# E_VALUE_THRESH = 0.04

# for alignment in blast_record.alignments:
#      for hsp in alignment.hsps:
#          if hsp.expect < E_VALUE_THRESH:
#              print("****Alignment****")
#              print("sequence:", alignment.title)
#              print("length:", alignment.length)
#              print("e value:", hsp.expect)
#              print(hsp.query[0:75] + "...")
#              print(hsp.match[0:75] + "...")
#              print(hsp.sbjct[0:75] + "...")
