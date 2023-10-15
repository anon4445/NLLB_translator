import streamlit as st
import ctranslate2
import transformers
from translator import translate
st.title("On Device Translator")
user_input = st.text_area("Enter text to be translated in English here.") 
languages = {
    "English": "eng_Latn",
    "Japanese": "jpn_Jpan",
    "Hindi": "hin_Deva",
    "French": "fra_Latn",
    "Spanish": "spa_Latn",
    "Chinese": "zho_Hans",
    "Italian": "ita_Latn",
    "German": "deu_Latn",
    "Russian": "rus_Cyrl"
}
selected_language = st.selectbox("Select Target Language", list(languages.keys()))
if st.button("Translate"):
    translated_text = translate(user_input, tgt_lang=languages[selected_language])
    st.write(f"Translated text: {translated_text}")

