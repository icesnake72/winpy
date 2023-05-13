'''
Helper Module of Output Debug String
'''

def make_out_string(**kwargs) -> str:
  str_out = ''
  for key, Value in kwargs:
    str_out += f'{key}={Value}\n'
  return str_out


def DebugOut(dbg_string:str) -> None:
  output = f'\n\
  >>>>>>>>>> Module : {__name__}, {__qualname__}\n \
  >>>>>>>>>> Debugging Message : {dbg_string}\n'  
  print(output)
  
  
def DebugValue(**kwargs) -> None:    
  str_out = lambda **kwargs : make_out_string(**kwargs)
  
  output = f'\n\
  >>>>>>>>>> Module : {__name__}, {__qualname__}\
  >>>>>>>>>> Debugging Message : { str_out(**kwargs) }\n'
  print(output)