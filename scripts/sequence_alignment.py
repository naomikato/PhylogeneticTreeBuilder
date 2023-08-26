from Bio import SeqIO, Align
import pandas as pd

# Load sequence data from FASTA file
sequences = SeqIO.parse('data/sequences.fasta', 'fasta')

# Load metadata from CSV file
metadata = pd.read_csv('data/metadata.csv')

# Create a dictionary to store sequences and their corresponding metadata
sequence_dict = {}
for record in sequences:
    sequence_id = record.id
    sequence = str(record.seq)
    metadata_row = metadata[metadata['Sequence_ID'] == sequence_id].iloc[0]
    species = metadata_row['Species']
    location = metadata_row['Location']
    sequence_dict[sequence_id] = {'sequence': sequence, 'species': species, 'location': location}

# Create a list of sequence records
sequence_records = [SeqIO.SeqRecord(Seq(seq_data['sequence']), id=seq_id) for seq_id, seq_data in sequence_dict.items()]

# Perform sequence alignment using ClustalW
alignment = Align.MultipleSeqAlignment(sequence_records)

# Save the alignment in FASTA format
SeqIO.write(alignment, 'results/aligned_sequences.fasta', 'fasta')

print("Sequence alignment has been performed and saved as 'results/aligned_sequences.fasta'.")
