
import gradio as gr
import requests

BOT_URL = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your Rasa server's endpoint

with gr.Blocks(css=".gradio-container {background-color: #F0F8FF} .feedback {background-color: 	#00ff00}") as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(elem_classes="feedback")
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        payload = {"sender": "user", "message": message}
        response = requests.post(BOT_URL, json=payload).json()
        try:
            bot_message = response[0]["text"]
            chat_history.append((message, bot_message))
            return "", chat_history
        except Exception as e:
            chat_history.append((message, "Sorry! I could not process your query now."))
            return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()

