import gradio as gr
from transformers import pipeline

chat = pipeline("conversational", model="microsoft/DialoGPT-medium")

def respond(user_input):
    from transformers import Conversation
    conversation = Conversation(user_input)
    chat(conversation)
    return str(conversation.generated_responses[-1])

iface = gr.Interface(fn=respond, 
                     inputs="text", 
                     outputs="text", 
                     title="KingofDanger Chatbot",
                     description="Ask anything 👑 powered by Hugging Face")

iface.launch()