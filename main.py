import streamlit as st

st.set_page_config(page_title="⏳ Calcolatore di Vita Spesa")

st.title("⏳ Quanto della tua vita hai già 'speso'?")

eta = st.slider("Quanti anni hai?", 10, 100, 30)
aspettativa = st.slider("Aspettativa di vita (in anni)", 50, 120, 85)

st.markdown("### Ore al giorno dedicate a:")
dormire = st.slider("😴 Dormire", 0.0, 12.0, 8.0)
lavorare = st.slider("💼 Lavorare/studiare", 0.0, 12.0, 8.0)
mangiare = st.slider("🍽️ Mangiare", 0.0, 4.0, 1.5)
social = st.slider("📱 Social media / TV", 0.0, 8.0, 2.0)
trasporti = st.slider("🚗 Trasporti / attese", 0.0, 6.0, 1.0)

# Calcoli
anni_tot = aspettativa
anni_trascorsi = eta
anni_restanti = anni_tot - eta

def ore_giornaliere_in_anni(ore_giorno):
    return round(ore_giorno * 365.25 * anni_tot / 24, 1)

st.markdown("---")

st.subheader("📊 Risultati:")

st.write(f"**Hai già vissuto:** {anni_trascorsi} anni")
st.write(f"**Ti restano (statisticamente):** {anni_restanti} anni")

st.markdown("### Tempo totale speso in vita:")
st.write(f"😴 Dormendo: {ore_giornaliere_in_anni(dormire)} anni")
st.write(f"💼 Lavorando/studiando: {ore_giornaliere_in_anni(lavorare)} anni")
st.write(f"🍽️ Mangiando: {ore_giornaliere_in_anni(mangiare)} anni")
st.write(f"📱 Sui social / TV: {ore_giornaliere_in_anni(social)} anni")
st.write(f"🚗 In trasporti / attese: {ore_giornari_in_anni(trasporti)} anni")

anni_spesi = sum([
    ore_giornaliere_in_anni(dormire),
    ore_giornari_in_anni(lavorare),
    ore_giornari_in_anni(mangiare),
    ore_giornari_in_anni(social),
    ore_giornari_in_anni(trasporti)
])

anni_liberi = round(anni_tot - anni_spesi, 1)

st.markdown("### ⏱️ Tempo VERAMENTE LIBERO nella vita:")
st.success(f"🧘 {anni_liberi} anni")

st.caption("⚠️ Basato su dati medi. L'obiettivo non è deprimere... ma svegliare.")

