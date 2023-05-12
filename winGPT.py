import openai
import os
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# OpenAI API 키 설정
# openai.api_key = 'YOUR_API_KEY'
openai.api_key = os.getenv("OPENAI_API_KEY")

# 대화 내용 추적을 위한 변수
conversation_history = []

def generate_response(input_text):
  # 이전 대화 내용과 현재 입력을 함께 전달
  # input_with_history = '\n'.join(conversation_history + [input_text])
  myMessages = []
  myMessages.append(
                {
                  'role':'user',
                  'content':input_text
                }
              )

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=myMessages
  )

  # 응답에서 모델의 답변 추출
  model_reply = completion.choices[0].message.content.strip()

  # 대화 내용에 현재 입력과 모델의 답변 추가
  conversation_history.append(input_text)
  conversation_history.append(model_reply)

  # 모델의 답변 반환
  return model_reply


def send_message():
  user_input = input_entry.get("1.0", tk.END).strip()
  if user_input:
    # 사용자 입력을 모델에 전달하여 응답 생성
    model_response = generate_response(user_input)

    # 모델 응답을 채팅 창에 표시
    chat_text.insert(tk.END, "사용자: " + user_input + "\n")
    chat_text.insert(tk.END, "ChatGPT: " + model_response + "\n")
    chat_text.insert(tk.END, "\n")

    # 사용자 입력 창 초기화
    input_entry.delete("1.0", tk.END)
    
def clear_chat():
  # 채팅 창 초기화
  chat_text.delete("1.0", tk.END)
  # 대화 내용 초기화
  global conversation_history
  conversation_history = []

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("ChatBot")
window.geometry("400x500")

# 스크롤 가능한 텍스트 창 생성
chat_text = scrolledtext.ScrolledText(window, height=20, width=40)
chat_text.pack(pady=10)

# 사용자 입력 창 생성
input_entry = tk.Text(window, height=3, width=30)
input_entry.pack()

# 전송 버튼 생성
send_button = tk.Button(window, text="전송", command=send_message)
send_button.pack(pady=10)

# 대화 초기화 버튼 생성
clear_button = tk.Button(window, text="대화 초기화", command=clear_chat)
clear_button.pack(pady=5)

# 윈도우 실행
window.mainloop()

# openai.api_key = os.getenv("OPENAI_API_KEY")

# myMessages = []
# myMessages.append(
#                 {
#                   'role':'user',
#                   'content':'5월에 가기 좋은 여행지 3곳만 알려줘'
#                 }
#               )
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=myMessages
# )

# print('...')

# print(completion.choices[0].message.content)