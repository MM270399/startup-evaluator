import streamlit as st

st.set_page_config(page_title="Quanto della tua vita sprechi?", page_icon="⏳")

st.title("⏳ Quanto della tua vita sprechi?")
st.write("Inserisci quante ore al giorno dedichi a ciascuna attività e quanti giorni a settimana lavori. L'app calcolerà quanti anni della tua vita hai speso in quelle attività.")

# Input utente
età = st.slider("🎂 La tua età attuale (anni)", 10, 100, 30)
dormire = st.slider("😴 Ore al giorno dedicate a dormire", 0.0, 24.0, 8.0, 0.5)
lavorare = st.slider("💼 Ore al giorno lavorando/studiando (nei giorni lavorativi)", 0.0, 24.0, 8.0, 0.5)
giorni_lavoro = st.slider("📅 Giorni di lavoro a settimana", 0, 7, 5, 1)
mangiare = st.slider("🍽️ Ore al giorno mangiando", 0.0, 24.0, 1.5, 0.5)
social = st.slider("📱 Ore al giorno su social / TV", 0.0, 24.0, 2.0, 0.5)
trasporti = st.slider("🚗 Ore al giorno in trasporti / attese", 0.0, 24.0, 1.0, 0.5)

# Funzione di calcolo per attività giornaliere (tutti i giorni)
def anni_spesi_giornalieri(ore_giorno, anni_vissuti):
    return round((ore_giorno * anni_vissuti) / 24, 1)

# Funzione di calcolo per lavoro (solo giorni lavorativi)
def anni_spesi_lavoro(ore_giorno, anni_vissuti, giorni_settimana):
    # Totale ore all'anno lavorative = ore_giorno * giorni_settimana * settimane
    # Settimane in un anno ≈ 52.18
    settimane = 52.18
    ore_annue_lavoro = ore_giorno * giorni_settimana * settimane
    ore_totali_vita = anni_vissuti * 365.25 * 24
    return round(ore_annue_lavoro * anni_vissuti / ore_totali_vita * anni_vissuti, 1)

# Calcoli
anni_dormire = anni_spesi_giornalieri(dormire, età)
anni_lavorare = anni_spesi_lavoro(lavorare, età, giorni_lavoro)
anni_mangiare = anni_spesi_giornalieri(mangiare, età)
anni_social = anni_spesi_giornalieri(social, età)
anni_trasporti = anni_spesi_giornalieri(trasporti, età)

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
st.write(f"💼 Lavorando: **{anni_lavorare}** anni")
st.write(f"🍽️ Mangiando: **{anni_mangiare}** anni")
st.write(f"📱 Su social/TV: **{anni_social}** anni")
st.write(f"🚗 In trasporti/attese: **{anni_trasporti}** anni")

st.markdown("---")
st.write(f"🧮 **Anni totali spesi in queste attività**: **{anni_totali_spesi}** anni")

if anni_totali_spesi >= età:
    st.error("😱 Hai speso più anni di quanti ne hai vissuti! Controlla i dati.")
else:
    percentuale = round((anni_totali_spesi / età) * 100, 1)
    st.success(f"📉 Hai speso circa **{percentuale}%** della tua vita in queste attività.")

st.markdown("---")
st.markdown("🔗 Creato con ❤️ da Massimiliano")
