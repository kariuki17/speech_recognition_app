# Speech Recognition App

A Streamlit-based application that transcribes spoken words into text in real time. The app uses speech recognition APIs and Python libraries to capture audio, process it, and display the transcribed text on the interface.

## Features

* 🎤 **Real-Time Audio Capture**: Records audio directly from the user’s microphone.
* 📝 **Speech-to-Text**: Converts spoken language into written text.
* 🌍 **Language Selection**: Supports multiple languages for transcription.
* ⏯️ **Pause/Resume Recording**: Control recording without restarting the app.
* 💾 **Save Transcriptions**: Option to save text outputs as `.txt` or `.csv`.
* ⚠️ **Error Handling**: Handles silence, noise, and connectivity gracefully.

## Project Goals

This project demonstrates how speech recognition can be integrated into accessible web apps for transcription, note-taking, or accessibility purposes. It also shows how multiple APIs can be combined to improve accuracy and flexibility.

## Tech Stack

* **Python**
* **Streamlit** (for the web interface)
* **SpeechRecognition** (Python speech recognition library)
* **pyaudio / sounddevice** (for audio capture)
* **Google Speech-to-Text API / Other APIs** (for recognition)
* **pandas, numpy** (for text saving and formatting)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/speech-recognition-app.git
   cd speech-recognition-app
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the app.
2. Select a preferred language.
3. Click **Start Recording** and begin speaking.
4. View the real-time transcription on the interface.
5. Save results if needed.

## Future Improvements

* Enhanced noise reduction.
* Integration with cloud APIs for higher accuracy.
* Export options (Word, PDF).
* Mobile-first design for accessibility.

## Disclaimer

This project is for **educational and demonstration purposes only**. It is not a replacement for professional transcription services.
