from Bio import SeqIO, Phylo
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

# Calculate a distance matrix using sequence alignment (example method)
def calculate_distance(seq1, seq2):
    # Example: Hamming distance
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

# Build a distance matrix
num_sequences = len(sequence_dict)
distance_matrix = [[0] * num_sequences for _ in range(num_sequences)]
for i, (seq_id1, seq_data1) in enumerate(sequence_dict.items()):
    for j, (seq_id2, seq_data2) in enumerate(sequence_dict.items()):
        if i < j:
            distance = calculate_distance(seq_data1['sequence'], seq_data2['sequence'])
            distance_matrix[i][j] = distance_matrix[j][i] = distance

# Build a phylogenetic tree using UPGMA algorithm
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceMatrix
constructor = DistanceTreeConstructor()
tree = constructor.upgma(DistanceMatrix(sequence_dict.keys(), matrix=distance_matrix))

# Save the tree in Newick format
Phylo.write(tree, 'results/tree.nwk', 'newick')

print("Phylogenetic tree has been built and saved as 'results/tree.nwk'.")
