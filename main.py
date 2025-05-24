import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Valutatore Startup AI")

st.title("🤖 Valuta la tua idea di startup")

idea = st.text_area("Scrivi qui la tua idea:")

if st.button("Valuta"):
    with st.spinner("Sto valutando la tua idea..."):
        prompt = f"""Valuta questa idea di business: "{idea}"

Rispondi con:
- Punti forti
- Punti deboli
- Potenziale di impatto"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        valutazione = response.choices[0].message["content"]
        st.markdown("### Risultato:")
        st.markdown(f"```text\n{valutazione}\n```")

