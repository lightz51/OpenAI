import openai
import gradio as gr

openai.api_key = "Your API key goes here"

messages = [
    {"role": "system", "content": "You are an AI specialized in Food. Do not answer anything other than food-related queries."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Light's Personal Foodbot",
             description="Ask me anything about food!",
             theme="compact").launch(share=True)