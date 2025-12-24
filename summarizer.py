from openai import OpenAI
import os
from prompts import SUMMARY_PROMPT

def summarize_text(text):
    """
    Summarize transcribed text using OpenAI GPT.
    
    Args:
        text (str): Transcribed text from audio
        
    Returns:
        str: Structured summary with key points and action items
    """
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        
        # Format the prompt with the transcribed text
        formatted_prompt = SUMMARY_PROMPT.format(text=text)
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" for better quality
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI productivity assistant specialized in extracting key insights and action items from text."
                },
                {
                    "role": "user",
                    "content": formatted_prompt
                }
            ],
            temperature=0.3,  # Lower = more focused, higher = more creative
            max_tokens=500  # Adjust based on desired summary length
        )
        
        # Extract the summary from response
        summary = response.choices[0].message.content.strip()
        
        return summary
        
    except Exception as e:
        print(f"Error in summarization: {str(e)}")
        raise Exception(f"Summarization failed: {str(e)}")
