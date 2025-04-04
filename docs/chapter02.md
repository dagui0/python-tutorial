# 파이썬 자습서 - 2. 파이썬 인터프리터 사용하기

자습서 페이지: https://docs.python.org/ko/3.12/tutorial/interpreter.html

## 목차

* [2.1. 인터프리터 실행하기](#21-인터프리터-실행하기)
  * [Linux](#linux)
  * [Windows](#windows)
  * [2.1.1. 인자 전달](#211-인자-전달)
  * [2.1.2. 대화형 모드](#212-대화형-모드)
* [2.2. 인터프리터와 환경](#22-인터프리터와-환경)
  * [2.2.1. 소스 코드 인코딩](#221-소스-코드-인코딩)

## 2.1. 인터프리터 실행하기

파이썬 쉘 실행

```shell
python
python3
python3.12
```

명령 바로 실행

```shell
python -c 'print("Hello, World!")'
```

`venv`라는 모듈 실행

```shell
python -m venv
```

### Linux

Linux에는 python이 필수로 깔리지만 `python` 명령이 없거나 `python2`일 수도 있다.
예전에는 `python2`로 지정된 경우가 많았지만, 지금은 아예 비워두거나, `python3`으로 지정된 경우가 많다.

* Debian/Ubuntu: `apt install python-is-python3`
* RedHat/CentOS: `alternatives --set python /usr/bin/python3`

### Windows

Python이 설치되면 `%SystemRoot%`(보통은 `C:\WINDOWS`)에 `py.exe`가 설치되며 `python`명령을 찾아서 실행시켜주는 역할을 한다.

```
C:\>dir %SystemRoot%\py.exe
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: E88C-3F80

 C:\WINDOWS 디렉터리

2025-02-04  오후 04:37           772,840 py.exe
               1개 파일             772,840 바이트
               0개 디렉터리  210,170,204,160 바이트 남음

C:\>py --list
 -V:3.13 *        Python 3.13 (64-bit)
 -V:2.7           Python 2.7

C:\>py -3
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

C:\>py -2
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

### 2.1.1. 인자 전달

`pydoc`모듈(도움말)에 `venv` 인자를 전달하여 실행

```shell
python -m pydoc venv
```

모듈이나 스크립트들은 `sys.argv`에서 인자들을 읽어올 수 있다. ([hello.py](src/chapter02/hello.py))

```python
#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
  target = sys.argv[1]
else:
  target = "여러분"
print(target + " 안녕!")
```

```
$ python hello.py 야이노무자스가
야이노무자스가 안녕!
```

`sys.argv[0]`은 스크립트의 이름을 포함하고, `sys.argv[1]`이후는 차례대로 전달된 인자를 저장하고 있다.
예를 들어, 위의 예시에서 `python hello.py 야 이노무 자스가`의 경우:

* `sys.argv[0]` : hello.py
* `sys.argv[1]` : 야
* `sys.argv[2]` : 이노무
* `sys.argv[3]` : 자스가

```
$ python hello.py 야 이노무 자스가
야 안녕!
```

원래 인자가 `-`로 시작하면 파이썬의 옵션으로 해석되지만,
스크립트가 지정된 경우(`-m`, `-c` 포함) 이후의 모든 인자들은
옵션이 아니라 파이썬 모듈이나 스크립트에 `sys.argv`로 전달된다.

```
$ python hello.py -m venv
-m 안녕!
```

### 2.1.2. 대화형 모드

스크립트를 지정하지 않고 `python` 명령을 실행하면 대화형 모드로 진입한다.
스크립트 파일명이 `-`인 경우 터미널(`stdin`)에서 읽어들이라는 의미로 이해한다. 이 또한 대화형 모드로 진입한다.

* `>>>`: 기본 프롬프트
* `...`: 문장이 끝나지 않았음을 나타내는 프롬프트

```
$ python - 이노무자스가
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> if len(sys.argv) > 1:
...     target = sys.argv[1]
... else:
...     target = "여러분"
... 
>>> print(target + " 안녕!")
이노무자스가 안녕!
>>> exit()
```

파이썬 쉘(대화형 모드)를 종료하려면 `exit()` 또는 `Ctrl+D` 를 입력하면 된다.
`Ctrl-D`는 유닉스에서 파일을 끝(stdin의 EOF)을 의미하는 특수 문자이고, Windows에서는 `Ctrl-Z`+`Enter`에 해당된다.

## 2.2. 인터프리터와 환경

### 2.2.1. 소스 코드 인코딩

Python 3은 기본적으로 UTF-8 인코딩을 사용한다.
인코딩을 다르게 지정하려면 소스 코드의 첫 줄에 인코딩을 지정해줄 수 있다. ([hello-euc.py](../src/chapter02/hello-euc.py))

```python
#!/usr/bin/env python3
# -*- coding: euckr -*-
print("여러분 안녕")
```
