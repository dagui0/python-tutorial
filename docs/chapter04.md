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

### `match` 문

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
def print_point_desc(point):
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

print_point_desc( (0, 0) )
```

`case` 절에 `break` 같은 것은 필요 없다. 매칭되는 `case`절만 수행되고 끝나며, 매칭되는 절이 없으면 아무 것도 수행되지 않는다.

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
## 4.5. else Clauses on Loops
## 4.6. pass 문
## 4.7. match Statements
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
