import openai, os
import tkinter as tk
from tkinter import font



class ChatGPTWrapper:
  def __init__(self, api_key:str) -> None:
    openai.api_key = api_key
    self.history = []
  
    
  def getResponse(self, user_msg:str) -> any:
    input_with_history = '\n'.join(self.history + [user_msg])
        
    # OpenAI에 요청하여 응답 생성
    messages = [ 
                  {
                    'role':'user',
                    'content':user_msg
                  }
                ]
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',        
        messages= messages,
        # prompt=input_with_history,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,        
    )
    
    # 응답에서 모델의 답변 추출
    model_reply = response.choices[0].message.content
    print(model_reply)
    
    self.history.append(user_msg)
    self.history.append(model_reply)    
    
    return model_reply
    
  
    

class WinPosition():
  def __init__(self, x, y, width, height) -> None:
    self.__x = x
    self.__y = y
    self.__width = width
    self.__height = height
    
  @property
  def x(self) -> int:
    return self.__x
  
  @property
  def y(self) -> int:
    return self.__y
  
  @property
  def width(self) -> int:
    return self.__width
  
  @property
  def height(self) -> int:
    return self.__height   
    

class MainWindow():
  def __init__(self, title:str, pos:WinPosition) -> None:
    ''' 메인 윈도우를 생성하고 위치를 지정한다 '''
    self.gpt:ChatGPTWrapper = None
    self.__mainWin = tk.Tk()
    self.__mainWin.title(title)
    self.__init_position(pos)
    self.__init_menu()
    self.__init_widgets()
    self.__mainWin.bind('<Configure>', self.__OnResize)
    
  @property
  def mainWindow(self) -> any:
    return self.__mainWin
    
  def setOpenAI(self, gpt:ChatGPTWrapper):
    self.gpt = gpt
    
  def __init_menu(self):
    menubar = tk.Menu(self.__mainWin)
    menu_1=tk.Menu(menubar, tearoff=0)
    menu_1.add_command(label='New')
    menu_1.add_command(label='Open')
    menu_1.add_command(label='Save')
    menu_1.add_command(label='Close')
    menubar.add_cascade(label='File', menu=menu_1)
    
    menu_2=tk.Menu(menubar, tearoff=0)
    menu_2.add_command(label='Copy')
    menu_2.add_command(label='Paste')
    menu_2.add_command(label='Clear')
    menubar.add_cascade(label='Edit', menu=menu_2)
    
    self.__mainWin.config(menu=menubar)
    
  
  def __init_widgets(self) -> None:
    main_font = font.Font(self.__mainWin, family='AppleGothic', size=14)
    self.edit_input = tk.Entry(self.__mainWin, width=self.__mainWin.winfo_width(), font=main_font)
    self.edit_input.pack(side='bottom')    
    self.edit_input.bind("<Return>", self.__OnEditInputEnter)    
        
    self.text_Out = tk.Text(self.__mainWin, width=self.__mainWin.winfo_width(), height=self.__mainWin.winfo_height()-self.edit_input.winfo_height(), font=main_font) #, state='disabled'
    self.text_Out.pack(side='top')
    self.text_Out.bind("<KeyPress>", self.__OnTextKeyPressed)    
    
    self.edit_input.focus()    
      
  
  def __init_position(self, pos:WinPosition) -> None:    
    screen_width = self.__mainWin.winfo_screenwidth()
    screen_height = self.__mainWin.winfo_screenheight()
    x_pos = (screen_width // 2) - (pos.width // 2)
    y_pos = (screen_height // 2) - (pos.height // 2)
    self.__mainWin.geometry(f"{pos.width}x{pos.height}+{x_pos}+{y_pos}")
    self.__mainWin.minsize(width=400, height=400)
    
  
  def __OnEditInputEnter(self, event):    
    user_message = self.edit_input.get()
    message = f'USER : {user_message}\n'
    self.text_Out.insert(tk.END, message)
    self.edit_input.delete(0, tk.END)
    
    if self.gpt!=None:
      ret_msg = self.gpt.getResponse(user_message)
      message = f'GPT : {ret_msg}\n'
      self.text_Out.insert(tk.END, message)
      self.text_Out.see(tk.END)
    
    
  def __OnResize(self, event):
    pass
    # y_pos = event.height - self.edit_input.winfo_height()
    # self.edit_input.place(x=0, y=y_pos, width=event.width)
    
  
  def __OnTextKeyPressed(self, event):
    return 'break'
    
  
if __name__=='__main__':
  key = os.getenv("OPENAI_API_KEY")
  gpt = ChatGPTWrapper(key)
  
  win_width = 800
  win_height = 600
  wp = WinPosition(0, 0, win_width, win_height)
  app = MainWindow('Tkinter Window', wp)
  app.setOpenAI(gpt)
  
  app.mainWindow.mainloop()


# main_font = font.Font(self.mainWin, family='AppleGothic', size=14)
# edit_input = tk.Entry(self.mainWin, width=win_width, font=main_font)
# edit_input.pack()
# edit_input.focus()

# edit_input.bind("<Return>", OnEditInputEnter)




#
# Example of an OpenAI ChatCompletion request with stream=True
# https://platform.openai.com/docs/guides/chat

# record the time before the request is sent
# start_time = time.time()

# send a ChatCompletion request to count to 100
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {'role': 'user', 'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
#     ],
#     temperature=0,
#     stream=True  # again, we set stream=True
# )

# # create variables to collect the stream of chunks
# collected_chunks = []
# collected_messages = []
# # iterate through the stream of events
# for chunk in response:
#     chunk_time = time.time() - start_time  # calculate the time delay of the chunk
#     collected_chunks.append(chunk)  # save the event response
#     chunk_message = chunk['choices'][0]['delta']  # extract the message
#     collected_messages.append(chunk_message)  # save the message
#     print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

# # print the time delay and text received
# print(f"Full response received {chunk_time:.2f} seconds after request")
# full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
# print(f"Full conversation received: {full_reply_content}")
#