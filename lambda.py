'''
lambda : 람다 함수는 이름이 없는 아주 작은 기능을 갖는 함수이다.
람다 함수는 많은 파라미터들을 이용할 수 있지만 한 문장만 쓸수 있다
'''

# 아래는 람다의 형식이다.
# 이름이 없는 이 함수는 a 라는 파라미터를 받아 10과 더한 결과값을 반환한다.
# 여기서 x는 람다함수를 수행한 결과값일 수 있는데, 그보다는 람다 함수 자체라고 보는것이 더 맞다.
x = lambda a : a + 10

# 따라서 아래와 같이 사용할 수 있다.
print(x(5))

# 여러개의 문자열을 받아 리스트로 반환하는 람다 함수
append = lambda *args : [ i for i in args ]
li = append('10', '20', '30')
print(li)


# 복잡한 작업을 수행하는 람다 함수
# 람다함수는 한 표현에 담아야 하기 때문에 복잡한 작업을 수행할 수는 없다
# 이럴경우에는 함수를 호출하여 복잡한 작업을 수행할 수 있도록 한다
def getSum(a:int) -> int:
  tot = 0
  for i in range(a+1):
    tot += i
  
  return tot

totaler = lambda a: getSum(a)
print(totaler(100))


# 람다의 힘은 다른 함수 내에서 익명 함수로 사용할 때 더 잘 나타납니다.
# 함수 한개로 비슷한 작업을 수행하는 여러개의 함수를 만들수 있습니다.
def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
print(doubler(10))

hundreder = myfunc(100)
print(hundreder(10))




def callbackFunction(data:str):
  print(data, end='')


# callback function
def readFromFile(fileName:str, callback):
  with open(fileName, 'r') as f:
    while True:
      ret = f.read(4)
      if ret=='': break        
      callback(ret)
      
    
readFromFile('MyClass.cs', callback=callbackFunction)
print()


def multipleVar(*args, **kwargs):
  print(args)
  print(kwargs)

multipleVar('a', 'b', 'c', integer=[1,2,3], flo=[0.1,0.2,0.3], mystr='string')