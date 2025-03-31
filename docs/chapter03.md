# 파이썬 자습서 - 3. 파이썬의 간략한 소개

자습서 페이지: https://docs.python.org/ko/3.12/tutorial/introduction.html

## 목차

* [3.1. 파이썬을 계산기로 사용하기](#31-파이썬을-계산기로-사용하기)
  * [3.1.1. 숫자](#311-숫자)
  * [3.1.2. Text](#312-text)
  * [3.1.3. 리스트](#313-리스트)
* [3.2. 프로그래밍으로의 첫걸음](#32-프로그래밍으로의-첫걸음)

## 3.1. 파이썬을 계산기로 사용하기

### 3.1.1. 숫자

나눗셈은 항상 부동소수점으로 계산된다.

```
>>> (50 - 5*6)/4
5.0
>>> 8/5
1.6
```

정수형 나눗셈을 하고자 하면 `//`를 사용한다.

```
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
```

거듭제곱은 `**`를 사용한다.

```
>>> 2**16
65536
```

변수의 선언은 필요 없으며 `=`를 사용하여 값을 지정한다.
정의되지 않은 변수가 사용되면 오류가 발생한다.

```
>>> width=100
>>> height=20
>>> width * height
2000
>>> width * height * depth
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    width * height * depth
                     ^^^^^
NameError: name 'depth' is not defined
```

묵시적 형 변환으로 정수는 부동소수점으로 자동 변환된다.

```
>>> 4 * 3.75 - 1
14.0
```

대화형 모드에서는 바로 전에 출력된 값(expression)은 `_`에 저장된다.

```
>>> 4 * 3.75 - 1
14.0
>>> _ / 2
7.0
```

만약 `_`에 값을 저장하면 같은 이름의 지역변수가 생성되고 `_`는 더이상 이전 결과를 저장하지 않을 것이다.

```
>>> _ = 3
>>> 2 * _
6
>>> 2 * _
6
```

### 3.1.2. Text

문자열은 작은 따옴표(`'`) 또는 큰 따옴표(`"`)로 감싸서 표현한다.
특수 문자 이스케이프를 위해서 `\`를 사용할 수 있고 `\`로 시작하는 특수문자(escape sequence)를 사용할 수 있다.

다른 언어와 달리 따옴표(`'`)와 큰 따옴표(`"`)는 기능상 차이가 없다. 단지 escape(`\'` 또는 `\"`)를 피하기 위해 서로 바꿔쓸 수 있다.

```
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
```

입력하는 문자열과 출력하는 문자열은 다를 수 있다. ([UTF-8 character escape table](http://daniel-hug.github.io/characters/))

```
>>> "\uc774\ub300\uaddc"
'이대규'
```

문자열 내용에 `\`가 포함되어 있으면 이스케이프 문자로 해석된다.
표현식 출력시에는 `\`가 포함되어 있으면 이스케이프 문자를 추가해서 출력하게 된다.

```
>>> 'these are\ntwo lines'
'these are\ntwo lines'
>>> print('these are\ntwo lines')
these are
two lines
```

#### 날 문자열(raw string)

`\` 뒤의 문자가 특수 문자로 취급되지 않게 하려면, 따옴표 앞에 `r`을 붙여서 날 문자열(raw string)로 만들 수 있다.

```
>>> print("C:\some\name")
<python-input-4>:1: SyntaxWarning: invalid escape sequence '\s'
  print("C:\some\name")
C:\some
ame
>>> print("C:\\some\\name")
C:\some\name
>>> print(r"C:\some\name")
C:\some\name
```

날 문자열(raw string)에서는 제약 사항이 있는데, 마지막 문자가 `\`인 경우 홀수개면 안된다는 것이다.

```
>>> r"C:\this\will\not\work\"
  File "<python-input-12>", line 1
    r"C:\this\will\not\work\"
    ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> r"C:\this\will\work\\"      # 그렇다고 2개를 하면 원하는 결과가 아니게 된다.
'C:\\this\\will\\work\\\\'
>>> r"C:\this\will\work" "\\"   # 문자열을 그냥 이어쓰면 하나로 합쳐진다.
'C:\\this\\will\\work\\'
>>> "C:\\this\\will\\work\\"    # 직접 `\\`를 사용할 수도 있다.
'C:\\this\\will\\work\\'
```

문자열의 끝의 `\`는 이스케이프로 해석되어 문제가 되지만 중간에 나오면 아니다.

```
>>> print(r'I can\'t do that')
I can\'t do that
>>> print(r'I can't do that')       # 오히려 따옴표를 escape 못해서 문제가 됨
File "<python-input-29>", line 1
print(r'I can't do that')
^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('I can\'t do that')       # 따옴표를 쓰려면 raw string을 지양하자
I can't do that
```

#### 여러 줄 문자열

여러 줄 문자열은 `"""` 또는 `'''`로 감싸서 표현한다. \
앞쪽 `"""` 바로 뒤의 `\n`과 뒤쪽 `"""` 앞의 `\n`은 무시되지 않는 다는 점을 주목할것.
new line을 `\`를 사용해서 이스케이프 가능하다.

```
>>> print("""
... 우리는 민족 중흥의 사명을 띄고 이 땅에 태어났다고는 하지만 식민지를 겪은 우리 머리속의
... 민족이란 개념은 제국주의의 끝물에 나온 우드로 윌슨의 민족자결주의에서 기원을 찾을 수 있다.
... 민족자결주의는 영국, 프랑스 등 유럽 제국주의 열강들에게 식민지 독점을 포기하고 공평하게
... 시장에 내놓으라는 미국의 입장에 기인한 것이지 진짜 민족이 중요하기 때문은 아니었다고...
... """)

우리는 민족 중흥의 사명을 띄고 이 땅에 태어났다고는 하지만 식민지를 겪은 우리 머리속의
민족이란 개념은 제국주의의 끝물에 나온 우드로 윌슨의 민족자결주의에서 기원을 찾을 수 있다.
민족자결주의는 영국, 프랑스 등 유럽 제국주의 열강들에게 식민지 독점을 포기하고 공평하게
시장에 내놓으라는 미국의 입장에 기인한 것이지 진짜 민족이 중요하기 때문은 아니었다고...

>>> print("""\
... Usage: thingy [OPTIONS]
...     -h              Display this usage message
...     -H hostname     Hostname to connect to\
... """)
Usage: thingy [OPTIONS]
    -h              Display this usage message
    -H hostname     Hostname to connect to
>>> 
```

#### 문자열 연산

문자열은 `+`로 연결할 수 있다. `*`는 문자열을 반복한다.

```
>>> 3 * '몰래' + " 다가가"
'몰래몰래몰래 다가가'
```

문자열 리터럴이 연속해서 나타나면 자동으로 하나로 합쳐진다.

```
>>> print("우리는 민족 중흥의 사명을 띄고 이 땅에 태어났다고는 하지만 식민지를 겪은 우리 머리속의"
... "민족이란 개념은 제국주의의 끝물에 나온 우드로 윌슨의 민족자결주의에서 기원을 찾을 수 있다."
... "민족자결주의는 영국, 프랑스 등 유럽 제국주의 열강들에게 식민지 독점을 포기하고 공평하게"
... "시장에 내놓으라는 미국의 입장에 기인한 것이지 진짜 민족이 중요하기 때문은 아니었다고...")
우리는 민족 중흥의 사명을 띄고 이 땅에 태어났다고는 하지만 식민지를 겪은 우리 머리속의민족이란 개념은 제국주의의 끝물에 나온 우드로 윌슨의 민족자결주의에서 기원을 찾을 수 있다.민족자결주의는 영국, 프랑스 등 유럽 제국주의 열강들 에게 식민지 독점을 포기하고 공평하게시장에 내놓으라는 미국의 입장에 기인한 것이지 진짜 민족이 중요하기 때문은 아니었다고...
```

문자열 리터럴이 아닌 변수나 표현식에는 해당되지 않는다.

```
>>> prefix = 'Py'
>>> prefix 'thon'
  File "<python-input-39>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
```

이럴때는 명시적으로 `+`를 사용해야 한다.

```
>>> prefix = 'Py'
>>> prefix + 'thon'
'Python'
```

#### 서브스크립트

문자열은 배열처럼 인덱스를 사용하여 서브스크립트 가능하다. '문자'형 자료형은 따로 없고 한글자 짜리 문자열이다.

```
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
```

인덱스가 음수인 경우 끝에서 부터 센다. `-0` == `0` 이므로 음수 인덱스는 `-1` 부터 시작한다.

```
>>> word[-1]
'n'
>>> word[-6]
'P'
```

#### 슬라이스

슬라이스 인덱스는 부분 문자열을 쉽게 추출 가능하다. `string_var[start:end]` 형식으로 사용한다.
(`start` is inclusive, `end` is exclusive)

```
>>> word[0:2]     # index >= 0 && index < 2
'Py'
>>> word[2:5]     # index >= 2 && index < 5
'tho'
```

슬라이스 인덱스에서 일부를 생략하면 알아서 잘 채운다.

```
>>> word[:2]      # (index >= 0) && index < 2
'Py'
>>> word[4:]      # index >= 4 && (index < len(word))
'on'
>>> word[-2:]     # index >= -2 && (index < len(word))
'on'
>>> word[:]       # 이건 되긴 하는데 별 의미는 없어 보인다.
'Python'
```

`start`번째 문자는 포함되고, `end`번째 문자는 포함되지 않는다.
그래서 `s[:i] + s[i:] == s` 가 항상 성립한다.

```
>>> for n in range(len(word)):
...     if word[:n] + word[n:] == word:
...         print("same")                                                                                                                                                                                                           
...         
same
same
same
same
same
same
```

인덱스는 글자들 사이를 나타내는 것으로 생각하면 이해하기 쉽다.

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

범위를 벗어나는 인덱스는 오류를 내지만, 슬라이스 인덱스의 경우 오류를 발생시키지는 않는다.

```
>>> word[6]
Traceback (most recent call last):
File "<python-input-5>", line 1, in <module>
word[6]
~~~~^^^
IndexError: string index out of range
>>> word[-7]
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    word[-7]
    ~~~~^^^^
IndexError: string index out of range
>>> word[:100]
'Python'
>>> word[100:]
''
>>> word[:100] + word[100:] == word
True
```

#### 문자열은 변경 불가

파이썬의 문자열은 불변 객체로 문자열 인덱스에 대입할 수 없다.

```
>>> word[0] = 'p'
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    word[0] = 'p'
    ~~~~^^^
TypeError: 'str' object does not support item assignment
```

변경을 해야 한다면 문자열을 새로 만들어야 한다.

```
>>> 'p' + word[1:]
'python'
```

#### 문자열 함수 및 고급 기능

```
>>> base64chars = '/0123456789=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
>>> len(base64chars)
64
```

* 문자열은 유니코드 문자 대상의 불변 시퀀스 타입으로 [시퀀스 타입 공통의 연산들](https://docs.python.org/ko/3.12/library/stdtypes.html#common-sequence-operations)을 지원한다.
* [문자열(str class) 고유의 메소드](https://docs.python.org/ko/3.12/library/stdtypes.html#string-methods)들도 많다.
* [포맷 문자열 리터럴(formatted string literals) 또는 f-string](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings)
* `str.format()`, `Formatter` 사용법 - [포맷 문자열 문법](https://docs.python.org/ko/3.12/library/string.html#formatstrings)
* C의 [`printf()` 스타일 문자열 포매팅](https://docs.python.org/ko/3.12/library/stdtypes.html#old-string-formatting)

### 3.1.3. 리스트

리스트는 컴파운드(compound) 자료형 중의 하나이다. 각 원소들은 서로 다른 자료형을 가질 수 있다.
문자열(또는 다른 시퀀스)처럼 인덱스와 슬라이스를 사용할 수 있다.

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[0:3]
[1, 4, 9]
```

`+` 연산으로 이어 붙일 수 있다.

```
>>> squares[:1] + squares[1:] == squares
True
```

문자열과 달리 리스트는 가변, 즉 내용을 변경할 수 있다.

```
>>> cubes = [1, 8, 27, 65, 125]
>>> 4 ** 3
64
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes
[1, 8, 27, 64, 125, 216, 216, 343]
```

단순 할당(assignment)는 리스트 객체를 복사하지 않는다.

```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> rgba.append("Alpha")
>>> rgb
['Red', 'Green', 'Blue', 'Alpha']
>>> id(rgb) == id(rgba)
True
```

전체 슬라이스를 사용하면 새로운 리스트 객체를 생성할 수 있다.

```
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb[:]
>>> id(rgb) == id(rgba)
False
>>> rgba.append("Alpha")
>>> rgb, rgba
(['Red', 'Green', 'Blue'], ['Red', 'Green', 'Blue', 'Alpha'])
```

슬라이스에 대입을 할 수 있는데, 일부를 잘라내거나 대체해서 리스트 크기가 변경될 수 있다.

```
>>> nums = ['I', 'II', 'III', 'IV', 5, 6, 'VII', 'VIII', 'IX', 'X']
>>> nums[4:6] = ["V", "VI"]
>>> nums
['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
>>> nums[5:] = []
>>> nums
['I', 'II', 'III', 'IV', 'V']
```

`len()`은 리스트에도 적용 가능하다.

```
>>> len(nums)
5
```

중첩된 리스트를 만들 수 있다.

```
>>> import numpy
>>> matrix1 = numpy.array([ [1, 2, 3], [4, 5, 6] ])
>>> matrix2 = numpy.array([ [2, 3, 4], [5, 6, 7] ])
>>> matrix1 * matrix2
array([[ 2,  6, 12],
       [20, 30, 42]])
```

## 3.2. 프로그래밍으로의 첫걸음

```python
#!/usr/bin/env python3
# fibonacci.py - print Fibonacci series

import sys

a, b = 0, 1
n = int(sys.argv[1]) if len(sys.argv) > 1 else 10

while a < n:
    print(a, end=', ')
    a, b = b, a + b
```

```
(.venv) PS> py .\src\chapter03\fibonacci.py
0 1 1 2 3 5 8 
(.venv) PS> py .\src\chapter03\fibonacci.py 100
0 1 1 2 3 5 8 13 21 34 55 89 
(.venv) PS> py .\src\chapter03\fibonacci.py 1000
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
```

* 다중 대입: `a, b = 0, 1`
* `while` 루프
* `print()` 함수`
  * 다양한 타입의 값을 출력할 수 있으며, 인자를 여러개 주면 공백으로 구분하여 출력한다.
    ```
    >>> i = 256*256
    >>> print('The value of i is', i)
    The value of i is 65536
    ```
  * 키워드 인자 `end`를 사용하여 출력 후 줄바꿈을 하지 않도록 설정할 수 있다.
