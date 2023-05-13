'''
파이썬 윈도우 Wrapper
'''

import tkinter as tk

class MainWindow():
  '''
  이 클래스는 tkinter를 이용하여 기본 윈도우를 생성하기 위한 클래스이다.
  title, geometry, resizable 파라미터들의 설정값으로 윈도우를 초기화할 수 있다.
  생성자에서 메인 윈도우를 초기화한뒤, 레이아웃을 설정하고, 위젯들을 초기화하도록 규칙을 만들었다. 
  '''
  def __init__(self, 
               title:str=None, 
               geometry:str=None, 
               resizable:dict=None, 
               minSize:dict=None) -> None:
    self.__winInit(title, geometry, resizable, minSize)
    self.initLayout()   
    self.initWidget()
    
  def __winInit(self, 
                title:str=None, 
                geometry:str=None, 
                resizable:dict=None,
                minSize:dict=None):
    '''메인 윈도우를 생성하고 전달되는 파라미터값들을 이용하여 초기화를 시킨다'''
    self.mainWin = tk.Tk()
    if title!=None:
      self.mainWin.title(title)
      
    if geometry!=None:
      self.mainWin.geometry(geometry)
      
    try:
      if len(resizable) == 2:
        print(resizable['width'], resizable['height'])
        self.mainWin.resizable(resizable['width'], resizable['height'])
    except:
      print('resizable(dict)의 \'width\' 키의 값(Value)은 넓이 조정 가능 여부를 결정하는 bool 값이어야 하고\n \
             \'height\' 키의 값(Value)은 높이 조정 가능 여부를 결정하는 bool 값이어야 합니다.')
      
    try:
      if len(minSize) == 2:
        self.mainWin.minsize(minSize['width'], minSize['height'])
    except:
      print('minSize(dict)의 \'width\' 키의 값(Value)은 메인 윈도우의 최소 넓이를 결정하는 값(int)이어야 하고\n \
             \'height\' 키의 값(Value)은 최소 높이를 결정하는 값(int)이어야 합니다.')
  
  @property
  def MainWindow(self) -> tk.Tk:
    return self.mainWin
  
  def initLayout(self) -> None: ...
  def initWidget(self) -> None: ...