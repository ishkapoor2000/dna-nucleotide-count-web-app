import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd

image = Image.open('<You can add any relevant picture here!>')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app created by Ish Kapoor counts the nucleotides of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # To remove/skip the sequence name
sequence = ''.join(sequence)  # Concatenates the remaining string

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence  # Displays the concatenated text

st.header('OUTPUT (DNA Nucleotide Count)')

# Print Dictionary
st.subheader('1. Print Dictionary')


def DNA_nucleotide_count(seq):

    d = dict([('A', seq.count('A')), ('T', seq.count('T')),
              ('G', seq.count('G')), ('C', seq.count('C'))])

    return d


X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())
X  # Displays nucleotide count for given input sequence
X_label
X_values

# Print text
st.subheader('2. Print text')
st.write(('There are {} adenine(A)').format(X['A']))
st.write(('There are {} thymine(T)').format(X['T']))
st.write(('There are {} guanine(G)').format(X['G']))
st.write(('There are {} cytosine(C)').format(X['C']))

# Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

# Display Bar Chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(x='nucleotide', y='count')
p = p.properties(width=alt.Step(80))
st.write(p)
