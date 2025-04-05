import pandas as pd
import streamlit as st
import datetime
import os
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Model Poznawczy</h1>
    </div>
    """,
    unsafe_allow_html=True
)

pytanie_1 = st.selectbox(
    "Obszar:",
    ("Praca","Przyjazn","Rodzina","Partner", "Społeczność"),
    index = None,
    placeholder = "Wybierz obszar sytuacji:"
)
pytanie_2a = st.text_input("Kto?", placeholder = "Kogo dotyczyla sytuacja:")
pytanie_2b = st.date_input("Kiedy?",datetime.date.today())
pytanie_2c = st.text_input("Gdzie?")
pytanie_2d = st.text_area(
    label = "Opis",
    height = 200,)


pytanie_3 = st.text_area(
    label = "Myśli automatyczne",
    height = 100,)

emocje = {
    "Złość": ["Wkurzenie", "Zawstydzenie", "Zazdrość", "Frustracja", "Irytacja", "Zranienie", "Rozdrażnienie", "Rozgoryczenie", "Zawiść"],
    "Strach": ["Niepokój", "Zmartwienie", "Panika", "Zestresowanie", "Przerażenie", "Zaskoczenie", "Niepewność", "Podejrzliwość"],
    "Smutek": ["Przygnębienie", "Samotność", "Żal", "Rozczarowanie", "Poczucie winy", "Bezsilność", "Apatia", "Żałoba"],
    "Wstyd": ["Zażenowanie", "Niska samoocena", "Upokorzenie", "Żenada", "Skrępowanie"],
    "Miłość": ["Czułość", "Zauroczenie", "Pożądanie", "Troska", "Intymność", "Uwielbienie", "Ciepło", "Tęsknota"],
    "Radość": ["Zadowolenie", "Wdzięczność", "Podekscytowanie", "Spełnienie", "Zainspirowanie", "Optymizm", "Spokój", "Szczęście"]
}

emocje_list = []

for i in range(2):
    emocja = []
    col1, col2, col3 = st.columns(3)
    with col1:
        kat = st.selectbox(f"Kategoria {i+1} :", list(emocje.keys()), key=f"kat_{i}")
        emocja.append(kat)
    with col2:
        emo = st.selectbox(f"Emocja {i+1} :", emocje[kat], key=f"emo_{i}")
        emocja.append(emo)
    with col3:
        perc = st.slider(f"% danej emocji {i+1} :", 0,100,50,5, key=f"perc_{i}")
        emocja.append(perc)
    emocje_list.append(emocja)


on = st.toggle("Dodac emocje?")

if on:
    emocja = []
    col1, col2, col3 = st.columns(3)
    with col1:
        kat = st.selectbox("Kategoria 3:", list(emocje.keys()), key="kat_3")
        emocja.append(kat)
    with col2:
        emo = st.selectbox("Emocja 3:", emocje[kat], key="emo_3")
        emocja.append(emo)
    with col3:
        perc = st.slider("% danej emocji 3:", 0, 100, 50, 5, key="perc_3")
        emocja.append(perc)
    emocje_list.append(emocja)



pytanie_5 = st.text_area(
    label = "Reakcje behawioralne",
    height = 100,)


# Inicjalizacja stanu (ważne przy pierwszym uruchomieniu)
if "pytanie_6a" not in st.session_state:
    st.session_state.pytanie_6a = False
if "pytanie_6b" not in st.session_state:
    st.session_state.pytanie_6b = False

# Funkcje do zmiany stanu
def select_6a():
    st.session_state.pytanie_6a = True
    st.session_state.pytanie_6b = False

def select_6b():
    st.session_state.pytanie_6a = False
    st.session_state.pytanie_6b = True

# Kolumny z checkboxami
col1, col2 = st.columns(2)

with col1:
    st.checkbox("Zadziałałem wg impulsu", key="pytanie_6a", on_change=select_6a)

with col2:
    st.checkbox("Nie zadziałałem wg impulsu", key="pytanie_6b", on_change=select_6b)

# Zapis końcowego wyboru
if st.session_state.pytanie_6a:
    impuls_wybrany = True
elif st.session_state.pytanie_6b:
    impuls_wybrany = False
else:
    impuls_wybrany = "Brak odpowiedzi"


pytanie_7 = st.text_area(
    label = "dowody za mysla automatyczna ",
    height = 200,)
    
pytanie_8 = st.text_area(
    label = "dowody przeciw mysli automatycznej ",
    height = 200,)
    
pytanie_9 = st.text_area(
    label = "mysl alternatywna",
    height = 200,)

data = {
    "obszar": pytanie_1,
    "kto": pytanie_2a.strip().capitalize(),
    "kiedy": str(pytanie_2b),
    "gdzie": pytanie_2c.strip().title(),
    "opis": pytanie_2d,
    "mysl_automatyczna": pytanie_3,
    "emocja_1": emocje_list[0],
    "emocja_2": emocje_list[1],
    "reakcje": pytanie_5,
    "impuls": impuls_wybrany,
    "dowody_za": pytanie_7,
    "dowody_przeciw": pytanie_8,
    "mysl_alternatywna": pytanie_9
}
if len(emocje_list)>2:
    data["emocja_3"] = emocje_list[2]

if st.button("Zapisz"):  
    df=pd.DataFrame([data])
    df.to_csv("entries.csv", mode="a", header=not os.path.exists("entries.csv"), index=False, encoding='cp1250')

if st.button("PDF"):
    from generate_pdf import generate_pdf
    pdf_path=generate_pdf(data)
    


