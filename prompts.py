"""
Prompt templates for AI Voice Note Summarizer.

This file contains carefully engineered prompts that guide the LLM
to produce structured, useful outputs.
"""

SUMMARY_PROMPT = """
You are an AI productivity assistant. Your task is to analyze the following voice note transcription and extract valuable insights.

**TRANSCRIPTION:**
{text}

**YOUR TASK:**
Please provide a structured summary with the following sections:

1. **📌 Key Points** (3-5 main ideas)
   - List the most important points discussed
   - Keep each point concise (1-2 sentences)

2. **✅ Action Items** (if any)
   - Extract any tasks, to-dos, or action items mentioned
   - Format each as: "Action: [Description]"
   - If no action items, write "No specific action items identified"

3. **🎯 Main Takeaway** (1-2 sentences)
   - Summarize the overall purpose or conclusion

**FORMATTING RULES:**
- Use clear bullet points
- Be concise but complete
- Focus on actionable and important information
- If the transcription is unclear or too short, provide what you can

**OUTPUT FORMAT:**
Use markdown formatting with headers and bullet points for easy reading.
"""

# Alternative prompt for meeting-specific summaries
MEETING_SUMMARY_PROMPT = """
Analyze this meeting transcription and provide:

**TRANSCRIPTION:**
{text}

**MEETING SUMMARY:**

**Attendees/Topics Discussed:**
- [List main topics or participants if mentioned]

**Key Decisions:**
- [List any decisions made]

**Action Items:**
- [Who] needs to [what] by [when, if mentioned]

**Next Steps:**
- [Any follow-up items]

**Notes:**
- [Additional relevant information]

If any section is not applicable, write "Not discussed in this recording."
"""

# Alternative prompt for idea/brainstorming sessions
IDEAS_SUMMARY_PROMPT = """
Analyze this brainstorming/idea session transcription:

**TRANSCRIPTION:**
{text}

**SUMMARY:**

**💡 Main Ideas:**
- [List creative ideas mentioned]

**🔥 Best Concepts:**
- [Highlight the most promising ideas]

**🤔 Questions/Concerns Raised:**
- [Any challenges or questions mentioned]

**⚡ Quick Wins:**
- [Easy-to-implement suggestions]

**🎯 Next Steps:**
- [How to move forward with these ideas]
"""