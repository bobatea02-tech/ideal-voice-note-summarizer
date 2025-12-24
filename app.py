import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text
import os

# Page configuration
st.set_page_config(
    page_title="AI Voice Note Summarizer",
    page_icon="🎙️",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        height: 3em;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🎙️ AI Voice Note Summarizer")
st.markdown("Convert your voice notes into structured summaries with action items")

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key. Get one at https://platform.openai.com/api-keys"
    )
    
    st.markdown("---")
    st.markdown("### 📋 Instructions")
    st.markdown("""
    1. Enter your OpenAI API key
    2. Upload an audio file (WAV, MP3, M4A)
    3. Click 'Process Voice Note'
    4. Get your summary!
    """)

# Main content area
st.markdown("---")

# File uploader
audio_file = st.file_uploader(
    "Upload your voice note",
    type=["wav", "mp3", "m4a", "ogg"],
    help="Supported formats: WAV, MP3, M4A, OGG"
)

# Display audio player if file uploaded
if audio_file:
    st.audio(audio_file, format=f'audio/{audio_file.type.split("/")[1]}')
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        process_button = st.button("🚀 Process Voice Note", use_container_width=True)
    
    if process_button:
        # Check if API key is provided
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API key in the sidebar!")
        else:
            # Set API key as environment variable
            os.environ['OPENAI_API_KEY'] = api_key
            
            try:
                # Step 1: Transcription
                with st.spinner("🎧 Transcribing audio... This may take a moment."):
                    transcribed_text = transcribe_audio(audio_file)
                
                if transcribed_text:
                    st.success("✅ Transcription complete!")
                    
                    # Display transcription
                    with st.expander("📝 View Full Transcription", expanded=False):
                        st.text_area(
                            "Transcribed Text",
                            transcribed_text,
                            height=200,
                            disabled=True
                        )
                    
                    # Step 2: Summarization
                    with st.spinner("🤖 Generating summary and action items..."):
                        summary = summarize_text(transcribed_text)
                    
                    if summary:
                        st.success("✅ Summary generated!")
                        
                        # Display summary
                        st.markdown("---")
                        st.subheader("📊 Summary & Action Items")
                        st.markdown(summary)
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Summary",
                            data=f"TRANSCRIPTION:\n\n{transcribed_text}\n\n{'='*50}\n\nSUMMARY:\n\n{summary}",
                            file_name="voice_note_summary.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("❌ Failed to generate summary. Please try again.")
                else:
                    st.error("❌ Failed to transcribe audio. Please check your file and try again.")
                    
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Make sure your OpenAI API key is valid and you have sufficient credits.")

else:
    # Show instructions when no file is uploaded
    st.info("👆 Upload an audio file to get started!")
    
    # Example use cases
    st.markdown("---")
    st.markdown("### 💡 Use Cases")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📅 Meeting Notes**")
        st.markdown("Convert meeting recordings into structured notes")
    
    with col2:
        st.markdown("**💭 Ideas**")
        st.markdown("Capture and organize brainstorming sessions")
    
    with col3:
        st.markdown("**✅ Tasks**")
        st.markdown("Extract action items from voice memos")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with Streamlit + Whisper + GPT | "
    "<a href='https://github.com' target='_blank'>View on GitHub</a></p>",
    unsafe_allow_html=True
)