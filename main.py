import streamlit as st

st.set_page_config(page_title="Quanto della tua vita sprechi?", page_icon="⏳")

st.title("⏳ Quanto della tua vita sprechi?")
st.write("Inserisci quante ore al giorno dedichi a ciascuna attività. L'app calcolerà quanti anni della tua vita vengono spesi in quelle attività.")

# Input utente
età = st.slider("🎂 La tua età attuale", 10, 100, 30)
dormire = st.slider("😴 Ore al giorno dedicate a dormire", 0.0, 24.0, 8.0, 0.5)
lavorare = st.slider("💼 Ore al giorno lavorando/studiando", 0.0, 24.0, 8.0, 0.5)
mangiare = st.slider("🍽️ Ore al giorno mangiando", 0.0, 24.0, 1.5, 0.5)
social = st.slider("📱 Ore al giorno su social / TV", 0.0, 24.0, 2.0, 0.5)
trasporti = st.slider("🚗 Ore al giorno in trasporti / attese", 0.0, 24.0, 1.0, 0.5)

# Funzione di calcolo
def ore_giornaliere_in_anni(ore):
    giorni_in_anno = 365.25
    return round((ore * giorni_in_anno) / 24, 1)

# Output
st.subheader("📊 Risultati:")

st.write(f"😴 Dormendo: {ore_giornaliere_in_anni(dormire)} anni")
st.write(f"💼 Lavorando/studiando: {ore_giornaliere_in_anni(lavorare)} anni")
st.write(f"🍽️ Mangiando: {ore_giornaliere_in_anni(mangiare)} anni")
st.write(f"📱 Sui social / TV: {ore_giornaliere_in_anni(social)} anni")
st.write(f"🚗 In trasporti / attese: {ore_giornaliere_in_anni(trasporti)} anni")

anni_spesi = sum([
    ore_giornaliere_in_anni(dormire),
    ore_giornaliere_in_anni(lavorare),
    ore_giornaliere_in_anni(mangiare),
    ore_giornaliere_in_anni(social),
    ore_giornaliere_in_anni(trasporti)
])

st.markdown("---")
st.write(f"🧮 **Anni totali spesi in queste attività**: **{anni_spesi} anni**")

if anni_spesi >= età:
    st.error("😱 Hai speso più anni di quanti ne hai vissuti! Ricontrolla i numeri.")
else:
    percentuale = round((anni_spesi / età) * 100, 1)
    st.success(f"📉 Hai speso circa **{percentuale}%** della tua vita in queste attività.")

st.markdown("---")
st.markdown("🔗 Creato con ❤️ da Massimiliano")
