import streamlit as st
import whisper
from pydub import AudioSegment
from pathlib import Path



with st.sidebar: 
    st.image("https://cf.ltkcdn.net/baby/images/std-xs/183290-340x433-proud-baby.jpg")
    st.title("For Lina")
    choice = st.radio("Navigation", ["Upload","Transcribe", "Download"])
    st.info("This project application will transcribe files")


if choice == "Upload":
    st.title("Upload Your file")
    wav_file = st.file_uploader("Upload Your file")
    if wav_file:
      file_var = AudioSegment.from_wav(wav_file)
      save_path = Path() / wav_file.name
      file_var.export(save_path, format='wav')
      model_type = ["medium", "large","large-v2"]
      chosen_target = st.selectbox('Choose the Target Column', model_type)
      if st.button('Transcribe'): 
        model = whisper.load_model(model_type[0])
        result = model.transcribe('/content/test.wav')
        st.download_button('Download', result.replace(".", ".\n"), file_name="transcribed.txt")
        st.audio(wav_file)
        st.text(result['text'].replace(".", ".\n"))
