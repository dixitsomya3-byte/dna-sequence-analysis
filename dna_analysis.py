# DNA Sequence Analysis

# Sample DNA sequence
dna = "ATGCGATCGATCGATGCTAGCTAG"

# Calculate sequence length
length = len(dna)

# Count each nucleotide
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

# Calculate GC content
gc_content = ((g_count + c_count) / length) * 100

# Display results
print("DNA Sequence:", dna)
print("Sequence Length:", length)
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("GC Content:", round(gc_content, 2), "%")
