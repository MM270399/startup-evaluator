import streamlit as st
from transformers import pipeline

# Configura la pagina
st.set_page_config(page_title="Valutatore Startup AI", layout="wide")

# Inizializza il modello di Hugging Face
generator = pipeline("text-generation", model="gpt2")

# Titolo
st.title("🤖 Valuta la tua idea di startup")

# Descrizione
st.write("Inserisci la descrizione della tua idea di business e ottieni una valutazione dettagliata.")

# Input dell'idea
idea = st.text_area("Scrivi qui la tua idea di startup:", height=200)

# Pulsante per valutare
if st.button("Valuta"):
    if not idea:
        st.error("Per favore, inserisci un'idea di startup.")
    else:
        with st.spinner("Sto valutando la tua idea..."):
            try:
                # Prompt per l'AI
                prompt = f"""Valuta questa idea di business: "{idea}"

Rispondi in italiano con:
- **Punti forti**
- **Punti deboli**
- **Potenziale di impatto**"""

                # Genera la risposta
                response = generator(prompt, max_length=500, num_return_sequences=1, truncation=True)
                valutazione = response[0]["generated_text"]
                st.markdown("### Risultato della valutazione:")
                st.markdown(f"```text\n{valutazione}\n```")
            except Exception as e:
                st.error(f"Errore durante la valutazione: {str(e)}.")
