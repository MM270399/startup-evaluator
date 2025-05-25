import streamlit as st

st.set_page_config(page_title="Quanto della tua vita sprechi?", page_icon="⏳")

st.title("⏳ Quanto della tua vita sprechi?")
st.write("Inserisci quante ore al giorno dedichi a ciascuna attività. L'app calcolerà quanti anni della tua vita hai speso in quelle attività.")

# Input utente
età = st.slider("🎂 La tua età attuale (anni)", 10, 100, 30)
dormire = st.slider("😴 Ore al giorno dedicate a dormire", 0.0, 24.0, 8.0, 0.5)
lavorare = st.slider("💼 Ore al giorno lavorando/studiando", 0.0, 24.0, 8.0, 0.5)
mangiare = st.slider("🍽️ Ore al giorno mangiando", 0.0, 24.0, 1.5, 0.5)
social = st.slider("📱 Ore al giorno su social / TV", 0.0, 24.0, 2.0, 0.5)
trasporti = st.slider("🚗 Ore al giorno in trasporti / attese", 0.0, 24.0, 1.0, 0.5)

# Funzione di calcolo corretta: 
# anni spesi in un'attività = (ore al giorno) * (anni vissuti) / 24
def anni_spesi(ore_giorno, anni_vissuti):
    return round((ore_giorno * anni_vissuti) / 24, 1)

# Calcoli per ciascuna attività
anni_dormire = anni_spesi(dormire, età)
anni_lavorare = anni_spesi(lavorare, età)
anni_mangiare = anni_spesi(mangiare, età)
anni_social = anni_spesi(social, età)
anni_trasporti = anni_spesi(trasporti, età)

# Somma totale
anni_totali_spesi = sum([
    anni_dormire,
    anni_lavorare,
    anni_mangiare,
    anni_social,
    anni_trasporti
])

# Output
st.subheader("📊 Risultati:")
st.write(f"😴 Dormendo: **{anni_dormire}** anni")
st.write(f"💼 Lavorando/studiando: **{anni_lavorare}** anni")
st.write(f"🍽️ Mangiando: **{anni_mangiare}** anni")
st.write(f"📱 Sui social / TV: **{anni_social}** anni")
st.write(f"🚗 In trasporti / attese: **{anni_trasporti}** anni")

st.markdown("---")
st.write(f"🧮 **Anni totali spesi in queste attività**: **{anni_totali_spesi}** anni")

if anni_totali_spesi >= età:
    st.error("😱 Hai speso più anni di quanti ne hai vissuti! Controlla i dati.")
else:
    percentuale = round((anni_totali_spesi / età) * 100, 1)
    st.success(f"📉 Hai speso circa **{percentuale}%** della tua vita in queste attività.")

st.markdown("---")
st.markdown("🔗 Creato con ❤️ da Massimiliano")
