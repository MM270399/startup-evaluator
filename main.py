import streamlit as st
import os
from openai import OpenAI

# Configura la chiave API di OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1",
)

# Configura la pagina
st.set_page_config(page_title="Valutatore Startup AI", layout="wide")

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

                # Chiamata all'API di OpenAI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Cambiato a gpt-3.5-turbo per maggiore accessibilità
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500
                )

                # Estrai la risposta
                valutazione = response.choices[0].message.content
                st.markdown("### Risultato della valutazione:")
                st.markdown(f"```text\n{valutazione}\n```")
            except Exception as e:
                st.error(f"Errore durante la valutazione: {str(e)}. Verifica la tua API key o la connessione.")
