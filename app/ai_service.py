from google import genai
from dotenv import load_dotenv
import os
from pydantic import BaseModel

class Email(BaseModel):
    ai_summary: str
    ticket_category: str 
    priority: str
    ai_sentiment_score: int

load_dotenv()

def analyze_email(email_title, email_message):
    client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

    prompt = f"Here is the title and body of an email that a customer sent to our support mailbox to generate a support ticket. Email title: {email_title}, Email body: {email_message}. Please provide a summary of the email, ticket category (question, request, issue), priority (low, medium, high), and AI sentiment score (1-10). Please provide it in JSON format with key values as ai_summary, ticket_category, priority, ai_sentiment_score."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Email.model_json_schema()
        }
    )

    response = Email.model_validate_json(response.text)
    return response