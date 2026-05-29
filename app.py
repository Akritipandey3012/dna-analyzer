import streamlit as st

st.set_page_config(page_title="DNA Analyzer", page_icon="🧬")
st.title("🧬 DNA Analyzer Toolkit")
st.caption("Built with Python | Bioinformatics Learning Project")

dna = st.text_input("Enter DNA Sequence:").upper().strip()

if st.button("Analyze"):
    if not dna:
        st.warning("Please enter a sequence!")
    elif not all(b in "ATGC" for b in dna):
        st.error("Invalid! Only A, T, G, C allowed.")
    else:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("A", dna.count("A"))
        c2.metric("T", dna.count("T"))
        c3.metric("G", dna.count("G"))
        c4.metric("C", dna.count("C"))
        gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
        st.metric("GC Content", f"{gc:.1f}%")
        rna = dna.replace("T", "U")
        st.success(f"RNA: {rna}")
        if "AUG" in rna:
            st.info("✅ Start Codon (AUG) found!")
        else:
            st.warning("❌ No start codon found")
