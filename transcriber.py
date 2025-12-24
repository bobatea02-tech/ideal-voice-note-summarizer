import streamlit as st
import whisper
import tempfile
import os

# Load Whisper model (cached after first load)
@st.cache_resource
def load_whisper_model():
    """
    Load Whisper model. Uses @st.cache_resource to load only once.
    
    Model sizes:
    - tiny: fastest, least accurate
    - base: good balance (recommended)
    - small: better accuracy
    - medium: high accuracy, slower
    - large: best accuracy, slowest
    """
    print("Loading Whisper model...")
    return whisper.load_model("base")

def transcribe_audio(audio_file):
    """
    Transcribe audio file to text using Whisper.
    
    Args:
        audio_file: Streamlit UploadedFile object
        
    Returns:
        str: Transcribed text
    """
    try:
        # Load model
        model = load_whisper_model()
        
        # Create temporary file to save uploaded audio
        # Whisper needs a file path, not a file object
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.name.split('.')[-1]}") as tmp_file:
            # Write uploaded file content to temp file
            tmp_file.write(audio_file.read())
            tmp_file_path = tmp_file.name
        
        try:
            # Transcribe audio
            result = model.transcribe(
                tmp_file_path,
                language="en",  # Set to None for auto-detection
                task="transcribe",  # or "translate" to translate to English
                fp16=False  # Set to True if you have GPU
            )
            
            # Extract text from result
            transcribed_text = result["text"].strip()
            
            return transcribed_text
            
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)
                
    except Exception as e:
        print(f"Error in transcription: {str(e)}")
        raise Exception(f"Transcription failed: {str(e)}")