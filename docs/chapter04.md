# 파이썬 자습서 - 4. 기타 제어 흐름 도구

자습서 페이지: https://docs.python.org/ko/3.12/tutorial/controlflow.html

## 목차

* [4.1. if 문](#41-if-문)
* [4.2. for 문](#42-for-문)
* [4.3. range() 함수](#43-range-함수)
* [4.4. break and continue Statements](#44-break-and-continue-statements)
* [4.5. else Clauses on Loops](#45-else-clauses-on-loops)
* [4.6. pass 문](#46-pass-문)
* [4.7. match Statements](#47-match-statements)
* [4.8. 함수 정의하기](#48-함수-정의하기)
* [4.9. 함수 정의 더 보기](#49-함수-정의-더-보기)
  * [4.9.1. 기본 인자 값](#491-기본-인자-값)
  * [4.9.2. 키워드 인자](#492-키워드-인자)
  * [4.9.3. 특수 매개 변수](#493-특수-매개-변수)
    * [4.9.3.1. 위치-키워드(Positional-or-Keyword) 인자](#4931-위치-키워드positional-or-keyword-인자)
    * [4.9.3.2. 위치 전용 매개 변수](#4932-위치-전용-매개-변수)
    * [4.9.3.3. 키워드 전용 인자](#4933-키워드-전용-인자)
    * [4.9.3.4. 함수 예제](#4934-함수-예제)
    * [4.9.3.5. 복습](#4935-복습)
  * [4.9.4. 임의의 인자 목록](#494-임의의-인자-목록)
  * [4.9.5. 인자 목록 언 패킹](#495-인자-목록-언-패킹)
  * [4.9.6. 람다 표현식](#496-람다-표현식)
  * [4.9.7. 도큐멘테이션 문자열](#497-도큐멘테이션-문자열)
  * [4.9.8. 함수 어노테이션](#498-함수-어노테이션)
* [4.10. 막간극: 코딩 스타일](#410-막간극-코딩-스타일)

## 4.1. if 문

```
>>> x = int(input("숫자를 입력하시오: "))
숫자를 입력하시오: 0
>>> if x < 0:
...     x = 0
...     print('nagative change to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
... 
Zero
```

`elif`는 들여쓰기가 깊어지는 것을 방지하기 위해 `else if`를 줄인 것이다.

## 4.2. for 문

파이썬의 `for`문은 시퀀스(리스트나 문자열)을 순회(iterate)하는 형태로만 반복수행된다.

```
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
  ...       print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

순회 도중 컬렉션을 수정하면(concurrent modification) 문제가 발생할 수 있으므로 카피본을 사용하도록 하자.

```
>>> for w in words.copy():                                                                                                                                                                                                          
...       print(w)
...       words.append(w)
... 
cat
window
defenestrate
>>> words
['cat', 'window', 'defenestrate', 'cat', 'window', 'defenestrate']
```

## 4.3. range() 함수

`for (int = 0; i < max; i++)` 같은 기능이 필요하면 `range()`를 사용해서 시퀀스를 생성할 수 있다.

```
>>> sum = 0
>>> for i in range(10):   # 0 ~ 9 까지를 가지는 시퀀스가 만들어짐
...       sum += i
... 
>>> print(sum)
45
```

`range` 인자를 여러개 지정하면, 시퀀스 시작값과 증분(step)을 설정할 수 있다.

```
>>> list(range(5, 10))          # (i = 5; i < 10; i++)
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))       # (i = 0; i < 10; i += 3)
[0, 3, 6, 9]
>>> list(range(-10, -100, -30)) # (i = -10; i > -100; i += -30)
[-10, -40, -70]
```

인덱스 번호가 필요하면 `range()`와 `len()`을 조합해서 사용한다.

```
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...       print(i, a[i])
... 
0 Mary
1 had
2 a
3 little
4 lamb
```

`enumerate()`로 같은 일을 할 수 있다.

```
>>> for (i, v) in enumerate(a):
...       print(i, v)
... 
0 Mary
1 had
2 a
3 little
4 lamb
```

### `range()`의 정체

`range()`의 값을 찍어보면 좀 이상하다.

```
>>> range(10)
range(0, 10)
```

`range()`는 리스트와 비슷하지만 실제 리스트는 아닌 무엇인가를 리턴하는데,
단순 루프를 위해서 실제 N개의 메모리 공간을 가지는 객체를 만들지 않기 때문에
메모리를 절약할 수 있다. 이런 객체를 이터러블(iterable)이라고 한다.

```
>>> sum(range(10))
45
```

### [참고] `sum()`과 `sum` 관련 주의 사항

만약 `sum()` 함수를 실행할때 오류가 발생한다면, `sum`이란 변수를 사용한 적이 있는지 생각해 보라

```
>>> sum = 10
>>> sum(range(10))
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    sum(range(10))
    ~~~^^^^^^^^^^^
TypeError: 'int' object is not callable
```

## 4.4. break and continue Statements

`for`, `while` 문 안에서 `break`와 `continue`를 사용할 수 있다.

```
>>> for n in range(2, 10):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(f"{n} equals {x} * {n//x}")
...                     break
... 
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
>>> for num in range(2, 10):
...     if num % 2 == 0:
...             print(f"Found an even number {num}")
...             continue
...     print(f"Found an odd number {num}")
... 
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

## 4.5. else Clauses on Loops

`for`와 `while` 루프에도 `else` 절을 사용할 수 있다.

`for`문에 `else`를 사용하면, `for`문이 정상적으로 종료되었을 때 `else`절이 실행된다.
`while`문에 `else`를 사용하면, `while`문이 조건식이 거짓이 되어 종료되었을 때 실행된다.

두 경우 모두 `break`문으로 루프를 빠져나가면 `else`절은 실행되지 않는다.

```
>>> for n in range(2, 10):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*', n//x)
...                     break
...     else:
...             # loop fell through without finding a factor
...             print(n, 'is a prime number')
... 
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

`else` 절이 `for`나 `while`에도 붙을 수 있으므로, 들여쓰기에 주의해야 할듯 하다.
루프에 붙는 `else`절은 `try` 예외 처리에 붙는 `else`와 비슷하다고 생각할 수 있다. 루프 블럭을 빠져나갈 때 실행된다. 

## 4.6. pass 문

`pass`문은 아무것도 하지 않는 문장이다. 문법적으로 문장이 필요하지만, 실행할 코드가 없을 때 사용한다.
보통은 빈 클래스를 만들거나 함수 정의할 때 플레이스 홀더로 사용된다.

```
>>> class MyEmptyClass:
...     pass
... 
>>> def initlog(*args):
...     pass    # TODO: remember to implement this!
... 
>>> 
```

## 4.7. match Statements

다른 언어에 있는 `switch`나 `case`문에 해당하는 `match`문이 있다.

```python
def http_error(status):
    match status:
      case 400:
        return 'Bad Request'
      case 401 | 403:
        return "You can't access this page"
      case 404:
        return 'Not Found'
      case 418:
        return "I'm a teapot"
      case _:
        return 'Something\'s wrong with the internet'
```

`match`문에서는 `_`가 `default` 역할을 한다. `case`에 `|`를 사용하면 여러 개의 조건을 나열할 수 있다.

```python
def where_is(point):
    match point:
      case (0, 0):
        print('Origin')
      case (0, y):
        print(f'Y={y}')
      case (x, 0):
        print(f'X={x}')
      case (x, y):
        print(f'X={x}, Y={y}')
      case _:
        raise ValueError('invalid point')

where_is( (0, 0) )
```

`case` 절에 `break` 같은 것은 필요 없다. 매칭되는 `case`절만 수행되고 끝나며, 매칭되는 절이 없으면 아무 것도 수행되지 않는다.

참고로 `(0, 0)` 같은 형식은 튜플(tuple)이라는 자료형이다.

위 예시에서 `(0, y)`같은 형식으로 `y`에 입력값을 바인딩 하는 방식으로 사용되는 것을 볼 수 있다.
`case (x, y)`는 2개 항으로된 튜플에 모두 매칭되고, 언패킹 할당(`(x, y) = point`) 처럼 동작한다.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
      case Point(x=0, y=0):
        print('Origin')
      case Point(x=0, y=y_value): 
        print(f'Y={y_value}')
      case Point(x=x_value, y=0):
        print(f'X={x_value}')
      case Point():
        print(f'X={point.x}, Y={point.y}')
      case _:
        raise ValueError('invalid point')
```

클래스를 사용하는 경우 생성자와 유사한 문법으로 `case`절을 작성할 수 있다.

클래스에 `__match_args__`를 사용하면 `case`절에서 `Point(x=0, y=0)` 대신 `Point(0, 0)`으로 사용할 수 있다.
이 경우 아래 `case` 절들은 모두 같은 의미가 된다.

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
      case Point(1, y_value):
        print(y_value)
      case Point(1, y=y_value):
        print(y_value)
      case Point(x=1, y=y_value):
        print(y_value)
      case Point(y=y_value, x=1):
        print(y_value)
```

`match`문에 의해서 할당되는 변수는 `x_value`, `y_value`같이 `=`의 오른 쪽 이름이란 점을 유의하자.
`case Point(x=x, y=y)` 처럼 할 수도 있으나 앞의 `x`는 `Point`의 속성명이고,
뒤의 `x`가 `match`문에 의해서 할당되는 지역 변수명이다.

중첩된 자료구조에 대한 패턴을 만들 수도 있다.

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_are(points):
    match points:
      case []:
        print('No points')
      case [Point(0, 0)]:
        print('The origin')
      case [Point(x_val, y_val)]:
        print(f'Single point {x_val}, {y_val}')
      case [Point(0, y1), Point(0, y2)]:
        print(f'Two on the Y axis at {y1}, {y2}')
      case _:
        print("Something else")
```

`case`절에 `if` 조건을 추가할 수도 있다.

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def is_diagonal(point):
    match point:
        case Point(x, y) if x == y:
            print(f'X=Y a {x}')
        case Point():
            print("Not on diagonal")
```

### `match` 관련 추가 사항

* 튜플과 리스트 패턴은 동일하게 취급되된다.
  ```
  >>> def match_zero2four(seq):
  ...     match seq:
  ...         case [0, 1, 2, 3, 4]:
  ...              print('ok')
  ...         case _:
  ...              print('nope')
  ...
  >>> match_zero2four( [0, 1, 2, 3, 4] )
  ok
  >>> match_zero2four( (0, 1, 2, 3, 4) )
  ok
  >>> match_zero2four( range(5) )
  ok
  ```
* 예외적으로 이터레이터나 문자열은 매칭되지 않는다.
  ```
  >>> def match_abcd( seq ):
  ...     match seq:
  ...         case [ 'a', 'b', 'c', 'd' ]:
  ...             print('ok')
  ...         case _:
  ...             print('nope')
  ... 
  >>> match_abcd( [ 'a', 'b', 'c', 'd' ] )
  ok
  >>> match_abcd( 'abcd' )
  nope
  ```
* `case` 패턴은 확장된 언패킹을 지원한다.
  `[x, y, *rest]` 는 최소 2개의 원소를 가진 시퀀스와 매칭하고,
  첫 2개를 각각 `x`, `y`에 나머지를 `rest`에 바인딩한다.
  `[x, y, *_]`는 마찬가지로 최소 2개의 원소를 가진 시퀀스와 매칭하고,
  `x`, `y`에 바인딩하고 나머지는 무시한다.
* 딕셔너리에 대한 매핑 패턴도 지원된다.
  `{'bandwidth': b, 'latency': l}`는 `bandwidth`와 `latency` 키를 가진 딕셔너리와 매칭되고,
  각각 `b`, `l`에 바인딩된다.
  `{'bandwidth': b, **rest}`는 `bandwidth` 키를 가진 딕셔너리와 매칭되고, 나머지는 `rest`에 바인딩된다.
  (하지만 원래 딕셔너리 매칭은 지정된 값만 찾고 나머지는 무시하므로 `**_`는 허용되지 않는다.)
  ```
  >>> def match_dict(dict):
  ...     match dict:
  ...         case { 'bandwidth': b, 'latency': l }:
  ...             print(f"found bandwidth {b} and latency {l}")
  ...         case { 'brand': b, **rest }:
  ...             print(f"brand {b} supports {rest}")
  ...         case { 'vendor': v }:
  ...             print(f"vendor {v} is here")
  ... 
  >>> match_dict( { 'bandwidth': 10, 'latency': 0.1, 'name': 'wireless' } )
  found bandwidth 10 and latency 0.1
  >>> match_dict( { 'brand': 'iptime', 'spec': '802.11ax' } )
  brand iptime supports {'spec': '802.11ax'}
  >>> match_dict( { 'vendor': 'IBM' } )
  vendor IBM is here
  >>> match_dict( { 'vendor': 'IBM', 'product': 'Personal Computer' } )
  vendor IBM is here
  ```

## 4.8. 함수 정의하기
## 4.9. 함수 정의 더 보기
## 4.9.1. 기본 인자 값
## 4.9.2. 키워드 인자
## 4.9.3. 특수 매개 변수
## 4.9.3.1. 위치-키워드(Positional-or-Keyword) 인자
## 4.9.3.2. 위치 전용 매개 변수
## 4.9.3.3. 키워드 전용 인자
## 4.9.3.4. 함수 예제
## 4.9.3.5. 복습
## 4.9.4. 임의의 인자 목록
## 4.9.5. 인자 목록 언 패킹
## 4.9.6. 람다 표현식
## 4.9.7. 도큐멘테이션 문자열
## 4.9.8. 함수 어노테이션
## 4.10. 막간극: 코딩 스타일
