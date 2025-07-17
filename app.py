import streamlit as st
import speech_recognition as sr
import threading
import time

# Initialize recognizer and shared state
recognizer = sr.Recognizer()
transcript = ""
is_listening = False
stop_signal = False

# Supported languages
languages = {
    "English (US)": "en-US",
    "Swahili (Kenya)": "sw-KE",
    "French (France)": "fr-FR",
    "German (Germany)": "de-DE",
    "Spanish (Spain)": "es-ES"
}

# Transcription function in a separate thread
def recognize_from_mic(lang_code):
    global transcript, is_listening, stop_signal

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.info("🎙 Listening... Speak now.")

        while is_listening and not stop_signal:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                text = recognizer.recognize_google(audio, language=lang_code)
                transcript += text + " "
                st.session_state['transcript'] = transcript
                time.sleep(0.1)
            except sr.WaitTimeoutError:
                st.warning("⏱️ No speech detected.")
            except sr.UnknownValueError:
                st.warning("🤷🏽 Could not understand that part.")
            except sr.RequestError as e:
                st.error(f"🚫 API error: {e}")
                break

# Streamlit UI
st.title("🎤 Live Speech Recognition App with Pause/Resume")
st.markdown("Transcribe speech using your microphone in real-time.")

# Language selection
selected_lang = st.selectbox("Choose your language:", list(languages.keys()))
lang_code = languages[selected_lang]

# Start, Pause, and Reset buttons
col1, col2, col3 = st.columns(3)
if col1.button("▶️ Start Listening"):
    if not is_listening:
        is_listening = True
        stop_signal = False
        threading.Thread(target=recognize_from_mic, args=(lang_code,), daemon=True).start()

if col2.button("⏸️ Pause Listening"):
    stop_signal = True
    is_listening = False
    st.success("✅ Paused.")

if col3.button("🔁 Reset"):
    transcript = ""
    st.session_state['transcript'] = ""
    stop_signal = True
    is_listening = False
    st.info("🧹 Reset complete.")

# Display transcript
st.subheader("📝 Transcript:")
st.write(st.session_state.get('transcript', ''))

# Save to file
if st.session_state.get('transcript', ''):
    with open("transcript.txt", "w", encoding='utf-8') as f:
        f.write(st.session_state['transcript'])

    st.download_button("💾 Download Transcript", data=st.session_state['transcript'], file_name="transcript.txt")
