'''
Tcl/Tk의 Wrapper 모듈임
파이썬에서 윈도우 프로그램을 아주 쉽게 개발할 수 있도록 많은 함수들 및 클래스를 제공한다.
'''
import tkinter as tk

if __name__=='__main__':
  
  count = 0
  def countUP():
    global count
    count +=1
    label.config(text=str(count))
    
  def changeState(button:tk.Button):
    bs = button.cget('state')
    if bs==tk.DISABLED:
      button.configure(state=tk.NORMAL)
    elif bs==tk.NORMAL:
      button.configure(state=tk.ACTIVE)
    else:
      button.configure(state=tk.DISABLED)

  
  # tkinter 모듈의 Tk()클래스로 메인 윈도우를 생성한다
  mainWin = tk.Tk()
  
  # 메인 윈도우의 타이틀을 설정한다.
  mainWin.title('메인 윈도우')
  
  width = 800
  height = 600
  mainWin.geometry(f'{width}x{height}')   # 윈도우의 초기 너비와 높이를 결정한다
  mainWin.minsize(300, 300) # Resize가 가능한 윈도우의 최소 너비와 높이를 결정한다
  mainWin.resizable(False, False) # 넓이, 높이 조정 가능 여부
  
  label=tk.Label(mainWin, 
                 text="tkinter로 생성된 윈도우입니다.", # 라벨에 표시될 텍스트
                 bitmap='info',  # 비트맵을 지정할 수도 있음
                 compound='left', # 문자열과 이미지가 같이 표시될 경우 비트맵의 위치
                 width=300,  # 너비
                 height=30,  # 높이
                 relief='solid',  # Border Style
                 bd=1,          # Border Line 두께
                 fg='#000000',  # 텍스트 컬러
                 bg='#CCCCCC')  # 백그라운드 컬러
                 
  label.pack()
  
  
  button = tk.Button(mainWin, 
                     text='Count Up',
                     overrelief="solid", 
                     width=15, 
                     command=countUP, 
                     repeatdelay=1000, 
                     repeatinterval=100)
  button.pack()
  
  button2 = tk.Button(mainWin, 
                      text='상태변경',
                      overrelief="solid", 
                      width=15, 
                      command=lambda : changeState(button), 
                      repeatdelay=1000, 
                      repeatinterval=100)
  button2.pack()
  
  # 프로세스가 종료될때까지 메인 이벤트 루프를 반복한다
  mainWin.mainloop()
  
  
