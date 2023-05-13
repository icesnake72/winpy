'''
python을 이용한 메모장 프로그램

<<<<< 마우스 버튼 이벤트 >>>>>
<Button-1>	마우스 왼쪽 버튼을 누를 때
<Button-2>	마우스 휠 버튼을 누를 때
<Button-3>	마우스 오른쪽 버튼을 누를 때
<Button-4>	스크롤 업
<Button-5>	스크롤 다운
<MouseWheel>	마우스 휠 이동

<<<<< 마우스 모션 이벤트 >>>>>
<Motion>	마우스가 움직일 때
<B1-Motion>	마우스 왼쪽 버튼을 누르면서 움직일 때
<B2-Motion>	마우스 휠 버튼을 누르면서 움직일 때
<B3-Motion>	마우스 오른쪽 버튼을 누르면서 움직일 때

<<<<< 마우스 버튼 Release 이벤트 >>>>>
<ButtonRelease-1>	마우스 왼쪽 버튼을 뗄 때
<ButtonRelease-2>	마우스 휠 버튼을 뗄 때
<ButtonRelease-3>	마우스 오른쪽 버튼을 뗄 때

<<<<< 마우스 버튼 더블클릭 이벤트 >>>>>
<Double-Button-1>	마우스 왼쪽 버튼을 더블 클릭할 때
<Double-Button-2>	마우스 휠 버튼을 더블 클릭할 때
<Double-Button-3>	마우스 오른쪽 버튼을 더블 클릭할 때

<<<<< 키 이벤트 >>>>>
<Key>	 특정 키가 입력되었을 때
<Return>	Enter 키가 입력되었을 때
<Cancel>	Break 키가 입력되었을 때
<Pause>	Pause 키가 입력되었을 때
<BackSpace>	백스페이스 키가 입력되었을 때
<Caps_Lock>	캡스 락 키가 입력되었을 때
<Escape>	이스케이프 키가 입력되었을 때
<Home>	Home 키가 입력되었을 때
<End>	End 키가 입력되었을 때
<Print>	Print 키가 입력되었을 때
<Insert>	Insert 키가 입력되었을 때
<Delete>	Delete 키가 입력되었을 때
<Prior>	Page UP 키가 입력되었을 때
<Up>	윗쪽 방향키가 입력되었을 때
<Down>	아랫쪽 방향키가 입력되었을 때
<Right>	오른쪽 방향키가 입력되었을 때
<Left>	왼쪽 방향키가 입력되었을 때

<<<<< 위젯 이벤트 >>>>>
<Enter>	위젯 안으로 마우스 포인터가 들어왓을 때
<Leave>	위젯 밖으로 마우스 포인터가 나갔을 때
<FocusIn>	위젯 안으로 Tab 키를 이용하여 들어왔을 때
<FocusOut>	위젯 밖으로 Tab 키를 이용하여 나갔을 때
<Configure>	위젯의 모양이 수정되었을 때
'''

from pyWinWrapper import MainWindow
from pyWinWrapper import tk
from tkinter import scrolledtext, font, messagebox, filedialog
import tkinter.ttk
from debugout import DebugOut

class PyWinMemo(MainWindow):
  def __init__(self, title: str = None, geometry: str = None, resizable:dict=None, minSize:dict=None) -> None:
    super().__init__(title, geometry, resizable, minSize)
    self.currentFile = ''
    self.mainWin.protocol('WM_DELETE_WINDOW', self.OnClose)
    self.initRecentList()
    
  def initRecentList(self):
    with open('pymemo.txt', 'rt') as f:
      while True:
        filepath = f.readline()
        filepath = filepath.strip()
        if filepath=='':break
        self.listbox.insert(tk.END, filepath)
    
  def initLayout(self) -> None:
    '''
    메모장 프로그램의 레이아웃을 결정한다
    왼쪽에 비쥬얼 소스코드와 같이 현재 폴더의 사용가능한 파일들을 나열하는 리스트 박스를 위치시킨다.
    오른쪽에는 메모장을 위치시킨다
    아래쪽에는 스테이터스바를 위치시킨다.
    '''    
    self.topPanel = tk.PanedWindow(self.mainWin,
                                   relief='flat',
                                   width=self.mainWin.winfo_width(),
                                   height=30)
    self.topPanel.grid(row=0, column=0)
    
    self.leftPanel = tk.PanedWindow(self.mainWin, 
                                    relief='flat', 
                                    # bg='#FF00FF', 
                                    # bd=5,
                                    width=250,
                                    height=100
                                    )
    # self.leftPanel.pack(side='left', fill='y')
    self.leftPanel.grid(row=1, column=0)
    
    self.rightPanel = tk.PanedWindow(self.mainWin, 
                                     relief='flat', 
                                    #  bg='#0000FF', 
                                    #  bd=5,
                                     width=300,
                                     height=100
                                    )
    # self.leftPanel.pack(side='left', fill='y')
    self.rightPanel.grid(row=1, column=1)
    self.mainWin.bind("<Configure>", self.__OnResize)
    super().initLayout()
  
  def __OnResize(self, event:tk.Event):
    width = self.MainWindow.winfo_width()
    height = self.MainWindow.winfo_height()
    # self.topPanel.configure(width=width, height=20)
    self.leftPanel.configure(height=height)
    self.rightPanel.configure(width=(width-self.leftPanel.winfo_width()), height=height)
    
  def initLeftSideWidget(self):
    '''
    레이아웃 왼쪽 영역 leftPanel(PanedWindow)의 위젯들을 생성하고 배치시킨다
    순서와 배치 옵션(여기서는 pack()을 사용함)이 중요하다
    '''
    
    # 최상단에 위치할 라벨(Label) 위젯을 생성
    self.labelRecent = tk.Label(self.leftPanel, 
                                relief='solid', 
                                bd=1, 
                                text="최근 사용된 파일들", 
                                font=self.font)
    self.labelRecent.pack(side='top', fill='x')
    
    # 리스트 박스 위젯과 함께 사용될 스크롤바 위젯을 만들고 배치한다.
    self.listScrollbar=tk.Scrollbar(self.leftPanel, bd=1, relief='solid')
    self.listScrollbar.pack(side='right', fill='y')
    
    # 리스트 박스를 생성하고 스크롤바 위젯과 연동시킨다.
    self.listbox = tk.Listbox(self.leftPanel, 
                              selectmode='single', 
                              yscrollcommand=self.listScrollbar.set, 
                              font=self.font)
    # for i in range(100):
    #   self.listbox.insert(i, str(i)*100)
    self.listbox.yview()
    self.listbox.pack(side='left', fill='both', expand=True)  # 리스트 박스를 스크롤바를 제외한 영역에 가득차게 배치시킨다
    self.listScrollbar['command'] = self.listbox.yview  # 스크롤바와 연동 마무리
    self.listbox.bind('<Double-Button-1>', self.OnDoubleClickList)
    
  def OnDoubleClickList(self, event):
    sels = self.listbox.curselection()
    filepath = self.listbox.get(sels[0])
    # self.currentFile = filepath    
    self.CheckModified()
    self.openFile(filepath)
    pass
  
  def initTopPanelWidget(self):    
    fontList = font.families(self.mainWin)
    self.fontCombo = tkinter.ttk.Combobox(self.topPanel,
                                          height=30,
                                          values=fontList
                                          )
    self.fontCombo.current(0)
    self.fontCombo.pack(side='left', fill='y') #.grid(row=0, column=0)
    self.fontCombo.bind('<<ComboboxSelected>>', self.OnFontChange)
    
    self.fontSizeCombo = tkinter.ttk.Combobox(self.topPanel,
                                              width=3,
                                              height=30)
    # self.fontSizeCombo.current(0)
    self.fontSizeCombo.pack(side='left', fill='y') #.grid(row=0, column=0)
    self.fontSizeCombo.bind('<<ComboboxSelected>>', self.OnFontSizeChange)
    
  
  def OnFontSizeChange(self, event):
    self.textFont.configure(size=self.fontSizeCombo.get())
    self.textBox.configure(font=self.textFont)
  
  def getFontSizes(self, font_family):
    sizes = []
    for size in range(1, 100):
        font_name = font.Font(family=font_family, size=size).actual()['family']
        if font_name != font_family:
            break
        sizes.append(size)
    return sizes
  
  def OnFontChange(self, event):    
    li = self.getFontSizes(self.fontCombo.get())
    # print(li)
    self.fontSizeCombo.configure(values=li)
    
    self.textFont.configure(family=self.fontCombo.get())
    self.textBox.configure(font=self.textFont)
    pass
  
  def initRightSideWidget(self):
    '''
    레이아웃 오른쪽 영역 rightPanel(PanedWindow)의 위젯들을 생성하고 배치시킨다
    순서와 배치 옵션(여기서는 pack()을 사용함)이 중요하다
    '''
    
    # 텍스트 박스 전용 폰트 생성
    self.textFont = font.Font(self.mainWin, family='AppleGothic', size=16)
    
    # 텍스트 박스 위젯과 함께 사용될 스크롤바 위젯을 만들고 배치한다.    
    self.textHScrollbar=tk.Scrollbar(self.rightPanel, 
                                    #  bd=1, 
                                     relief='flat', 
                                     orient=tk.HORIZONTAL)
    self.textHScrollbar.pack(side='bottom', fill='x')       
    
    self.textBox = scrolledtext.ScrolledText(self.rightPanel, 
                           font=self.textFont, 
                           tabs='20',
                           wrap='none',
                          #  xscrollcommand=self.textHScrollbar,
                          #  yscrollcommand=self.textVScrollbar
                           )
    self.textBox.pack(side='top', fill='both', expand=True)
    
    # # 텍스트 박스 위젯과 함께 사용될 상하 스크롤바 위젯을 만들고 배치한다.
    # self.textVScrollbar=tk.Scrollbar(self.textBox, bd=1, relief='solid')
    # self.textVScrollbar.pack(side='right', fill='y')
    # self.textBox.config(yscrollcommand=self.textVScrollbar.set)
    # self.textVScrollbar.config(command=self.textBox.yview)   
    
    self.textBox.config(xscrollcommand=self.textHScrollbar.set)   
    self.textHScrollbar.config(command=self.textBox.xview)    
  
  def initMenu(self):
    '''메뉴를 생성하고 하위 메뉴들을 추가한다'''
    
    # 메뉴바 생성
    menubar = tk.Menu(self.mainWin)
    
    # 파일
    menu_1=tk.Menu(menubar)
    menu_1.add_command(label='새파일', command=self.OnFileNew, accelerator='Control+N') # 새파일
    menu_1.add_separator()
    menu_1.add_command(label='열기', command=self.OnFileOpen) # 열기
    menu_1.add_command(label='저장', command=self.OnFileSave) # 저장
    menu_1.add_command(label='다른 이름으로 저장', command=self.OnFileSaveas) # 저장
    menu_1.add_separator()
    menu_1.add_command(label='종료', command=self.OnClose, accelerator='Command+W')  # 프로그램 종료
    menubar.add_cascade(label='파일', menu=menu_1)  # 메뉴바에 파일이라는 타이틀로 menu_1 묶음 추가
    
    # 편집
    menu_2=tk.Menu(menubar, tearoff=0)
    menu_2.add_command(label='복사', command=self.OnCopyText)
    menu_2.add_command(label='잘라내기', command=self.OnCutText)
    menu_2.add_command(label='붙여넣기', command=self.OnPasteText)    
    menubar.add_cascade(label='편집', menu=menu_2)  
    
    
    cmd = self.mainWin.bind('<Control-Key-n>', lambda event: self.OnNew())
    cmd = self.mainWin.bind('<Command-Key-w>', lambda event: self.OnClose())
        
    self.mainWin.config(menu=menubar)    
    
  def OnNew(self):
    print('test')
    
  
  def initWidget(self) -> None: 
    self.font = font.Font(self.mainWin, family='AppleGothic', size=12)
    
    self.initTopPanelWidget()
    self.initLeftSideWidget()
    self.initRightSideWidget()
    self.initMenu()
    
    super().initWidget() 
    
  def CheckModified(self):
    if self.textBox.edit_modified():
      result = messagebox.askquestion("확인", "변경사항을 저장하시겠습니까?")
      if result == 'yes':
          self.OnFileSave()
      
    self.textBox.delete('1.0', tk.END)
    self.textBox.edit_modified(False)
          
  def addToList(self, filepath:str):
    if filepath in self.listbox.get(0, tk.END):
      return
    
    self.listbox.insert(0, filepath)
    
    
  def saveRecents(self):
    with open('pymemo.txt', 'wt') as f:
      for filepath in self.listbox.get(0, tk.END):
        f.write(f'{filepath}\n')
        
  
    
  def OnFileNew(self):
    self.CheckModified()
    
  def openFile(self, filepath):
    self.textBox.delete('1.0', tk.END)
    with open(filepath, 'rt') as f:      
      try:   
        content = f.read()
        content = content.rstrip('\n')
        self.textBox.insert(tk.END, content)          
      except:
        messagebox.showerror('에러', '파일을 읽을 수 없습니다')
        return
      
      # line = self.textBox.index(tk.END)
      # print(line)
      
      self.textBox.edit_modified(False)  
      self.addToList(filepath)
      self.currentFile = filepath
        
  def OnFileOpen(self):
    self.CheckModified()
    filetypes = (("텍스트 파일", "*.txt"), ("파이썬 파일", "*.py"), ("모든 파일", "*.*"))
    filepath = filedialog.askopenfilename(filetypes=filetypes)
    if filepath:
        self.openFile(filepath)
          
  def saveFile(self, filepath:str):
    if filepath=='':
      print('saveFile() 메소드에서 filepath 값이 없습니다.')
      return False
      
    txt = self.textBox.get('1.0', tk.END)    
    if len(txt) <= 0:
      messagebox.showerror('에러', '파일에 저장할 내용이 없습니다')
      return False
    
    try:
      with open(filepath, 'wt') as f:
        f.write(self.textBox.get('1.0', tk.END))
        self.textBox.edit_modified(False)
    except:
      return False
    
    return True
  
      
  def OnFileSave(self):
    if self.currentFile=='':
      return self.OnFileSaveas()
    
    self.saveFile(self.currentFile)
  
  def OnFileSaveas(self):
    filetypes = (("텍스트 파일", "*.txt"), ("모든 파일", "*.*"))
    filepath = filedialog.asksaveasfilename(filetypes=filetypes)
    if filepath:                
        if self.saveFile(filepath):
          self.currentFile = filepath
          self.addToList(self.currentFile)
        else:
          messagebox.showerror('에러', '파일에 저장할 수 없습니다.')
          
          
  def OnCopyText(self):
        selected_text = self.textBox.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.mainWin.clipboard_clear()
        self.mainWin.clipboard_append(selected_text)

  def OnCutText(self):
      if self.textBox.tag_ranges(tk.SEL):
          selected_text = self.textBox.get(tk.SEL_FIRST, tk.SEL_LAST)
          self.textBox.delete(tk.SEL_FIRST, tk.SEL_LAST)
          self.mainWin.clipboard_clear()
          self.mainWin.clipboard_append(selected_text)

  def OnPasteText(self):
      clipboard_text = self.mainWin.clipboard_get()
      self.textBox.insert(tk.INSERT, clipboard_text)
      
  def OnClose(self):
    self.saveRecents()
    self.mainWin.destroy()
    
  
if __name__=='__main__':
  pyMemo = PyWinMemo(title='PyWin 메모장', 
                     geometry='800x600+100+100',
                     resizable={'width':True, 'height':True},
                     minSize={'width':300, 'height':300})
  
  pyMemo.MainWindow.mainloop()
  
  


