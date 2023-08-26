from Bio import Phylo

# Load the phylogenetic tree from the Newick file
tree = Phylo.read('results/tree.nwk', 'newick')

# Customize the tree visualization (optional)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", do_show=False)
Phylo.draw_ascii(tree)

# Save the tree visualization as an image
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False, do_show=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", show_confidence=False)

# Save the tree visualization as an image
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", do_show=False)
Phylo.draw_ascii(tree)

# Save the tree visualization as an image
Phylo.draw(tree, branch_labels=lambda c: f"{c.branch_length:.2f}", do_show=False)
Phylo.draw_ascii(tree)
print("Tree visualization has been created and saved as 'results/tree.png'.")
