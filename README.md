# 🎙️ AI Voice Note Summarizer

Convert voice notes into structured summaries with action items using AI.

## 🚀 Features

- ✅ Speech-to-text transcription using OpenAI Whisper
- ✅ AI-powered summarization with GPT
- ✅ Action item extraction
- ✅ Clean Streamlit interface
- ✅ Download summaries as text files
- ✅ Supports multiple audio formats (WAV, MP3, M4A, OGG)

## 📁 Project Structure

```
ai_voice_note_summarizer/
│
├── app.py                # Streamlit UI
├── transcriber.py        # Speech → Text logic (Whisper)
├── summarizer.py         # LLM summarization logic
├── prompts.py            # Prompt engineering templates
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🛠️ Setup Instructions

### Step 1: Install Python (3.8 or higher)

Check if Python is installed:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install FFmpeg (Required for Whisper)

**Windows:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract and add to PATH
3. Or use Chocolatey: `choco install ffmpeg`

**Mac:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### Step 3: Clone/Download Project

```bash
# Create project folder
mkdir ai_voice_note_summarizer
cd ai_voice_note_summarizer

# Copy all the code files here
```

### Step 4: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

**Note:** First installation may take 5-10 minutes as it downloads Whisper model and PyTorch.

### Step 5: Get OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)

**Cost:** ~$0.002 per minute of audio (very cheap!)

### Step 6: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage

1. **Enter API Key:** Paste your OpenAI API key in the sidebar
2. **Upload Audio:** Choose a voice note file (WAV, MP3, M4A, OGG)
3. **Process:** Click "Process Voice Note"
4. **View Results:** See transcription and summary
5. **Download:** Save the summary as a text file

## 🧠 How It Works

```
Voice Note (Audio)
       ↓
[Whisper Model] → Transcription (Text)
       ↓
[GPT Model] → Summary + Action Items
       ↓
[Display in Streamlit UI]
```

### Technical Flow:

1. **Audio Upload:** Streamlit receives audio file
2. **Temp Storage:** File saved temporarily for processing
3. **Whisper Transcription:** Audio → Text conversion
4. **Prompt Engineering:** Text formatted with instructions
5. **LLM Processing:** GPT analyzes and structures output
6. **Display Results:** Summary shown in UI

## 🎯 Example Output

**Input:** 2-minute voice note about project meeting

**Output:**
```
📌 Key Points
• Discussed Q4 product launch timeline
• Budget approved at $50K
• Marketing campaign starts next month

✅ Action Items
• Action: John to finalize design mockups by Friday
• Action: Sarah to schedule client demo for next week
• Action: Team to review competitor analysis

🎯 Main Takeaway
Project is on track for Q4 launch with approved budget and clear next steps.
```

## ⚙️ Customization

### Change Whisper Model (in `transcriber.py`)

```python
# Faster but less accurate
model = whisper.load_model("tiny")

# Better accuracy (default)
model = whisper.load_model("base")

# Best accuracy (slower)
model = whisper.load_model("large")
```

### Change GPT Model (in `summarizer.py`)

```python
# Cheaper, faster
model="gpt-3.5-turbo"

# Better quality
model="gpt-4"

# Latest model
model="gpt-4-turbo-preview"
```

### Modify Prompts (in `prompts.py`)

Edit `SUMMARY_PROMPT` to change output format or focus areas.

## 🐛 Troubleshooting

### Error: "FFmpeg not found"
- Install FFmpeg (see Step 2)
- Restart terminal after installation

### Error: "Invalid API key"
- Check if key starts with `sk-`
- Verify key at [platform.openai.com](https://platform.openai.com/api-keys)
- Check if you have API credits

### Slow Transcription
- Use smaller Whisper model (`tiny` or `base`)
- First run downloads model (~150MB), subsequent runs are faster

### Out of Memory
- Close other applications
- Use smaller Whisper model
- Process shorter audio files

## 💡 Improvement Ideas

- [ ] Add support for multiple languages
- [ ] Speaker diarization (who said what)
- [ ] Timestamp extraction
- [ ] Export to PDF
- [ ] Batch processing multiple files
- [ ] Custom summary templates

## 📊 Project for Resume/Portfolio

**Technical Skills Demonstrated:**
- Python programming
- AI/ML integration (Whisper, GPT)
- API consumption (OpenAI)
- Web development (Streamlit)
- Prompt engineering
- File handling & data pipeline design

**Interview Talking Points:**
- "Built end-to-end AI pipeline with 3 core components"
- "Implemented speech recognition using Transformer models"
- "Engineered prompts for structured output extraction"
- "Designed modular architecture for maintainability"

## 📝 License

MIT License - feel free to use for personal or commercial projects.

## 🤝 Contributing

Suggestions and improvements welcome! Open an issue or submit a pull request.

---

**Built with:** Python • Streamlit • OpenAI Whisper • GPT-3.5

**Made by:** Parthi Gadher | [GitHub](https://github.com/bobatea02-tech)

