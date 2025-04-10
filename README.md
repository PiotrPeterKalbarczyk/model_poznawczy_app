# Model poznawczy – aplikacja Streamlit + raport PDF

📌 *Poniżej znajduje się wersja angielska | English version below ⬇️*

To aplikacja wspierająca autorefleksję i pracę nad schematami myślowymi w nurcie poznawczo-behawioralnym. Umożliwia ona wypełnienie modelu poznawczego (sytuacja – emocje – myśli – reakcje – analiza poznawcza) oraz zapisanie odpowiedzi w formie pliku PDF. Aplikacja może być używana samodzielnie lub jako wsparcie terapii.

## ✍️ Funkcjonalności

- Interaktywny formularz w Streamlit
- Możliwość wyboru emocji, procentowego natężenia i kontekstu
- Zapis danych do pliku CSV
- Generowanie PDF na podstawie danych wejściowych (Jinja2 + HTML)

## 📋 Formularz zawiera:

- Obszar życia (praca, relacje, rodzina, itp.)
- Kto, kiedy, gdzie – kontekst sytuacji
- Opis sytuacji
- Myśli automatyczne
- Emocje (do 3, z kategorią i intensywnością)
- Reakcje behawioralne i impuls
- Dowody za i przeciw myśli automatycznej
- Myśl alternatywna

## 🛠️ Technologie

- Python  
- Streamlit  
- Pandas  
- Jinja2  
- HTML/CSS do raportu PDF  

## 📁 Pliki

- `app.py` – główna aplikacja Streamlit  
- `report_template.html` – szablon raportu PDF  
- `entries.csv` – automatycznie zapisany dziennik danych  

## 🚀 Możliwe rozszerzenia

- Dodanie bazy danych (np. SQLite, PostgreSQL)  
- Historia sesji użytkownika  
- Wersja mobilna lub dostęp z telefonu  
- Eksport wykresów emocji  

## 💭 Uwagi

Projekt powstał jako narzędzie osobiste do pracy własnej, ale może zostać rozwinięty do szerszego użytku.

---

# Cognitive Model App – Streamlit + PDF Generator

📌 *This is the English version.*

This is a self-reflection tool based on the cognitive model commonly used in cognitive-behavioral therapy. It allows the user to fill out structured information about an emotional event and automatically generate a PDF report. The app can be used independently or as a complement to therapy sessions.

## ✍️ Features

- Interactive Streamlit form  
- Emotion categories and intensity sliders  
- CSV data export  
- PDF report generation based on input (Jinja2 + HTML)

## 📋 The form includes:

- Life area (Work, Family, Partner, Community, etc.)
- Who / When / Where – contextual questions
- Event description
- Automatic thoughts
- Up to 3 emotions with category and intensity
- Behavioral response and impulse control
- Evidence supporting and contradicting the thought
- Alternative thought

## 🛠️ Technologies

- Python  
- Streamlit  
- Pandas  
- Jinja2  
- HTML/CSS (PDF design)

## 📁 Files

- `app.py` – main Streamlit application  
- `report_template.html` – PDF report template  
- `entries.csv` – local log of user entries  

## 🚀 Possible Improvements

- Add a database (e.g., SQLite or PostgreSQL)  
- User history dashboard  
- Mobile support  
- Emotion charts

## 💭 Notes

Originally created as a personal therapy support tool, with potential for future public use.