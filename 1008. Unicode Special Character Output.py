'''
[1008. 유니코드 특수문자 출력하기]

- 모든 문자(기호, 특수문자 포함)는 메모리 내에서 고유한 개별 문자 코드로 관리된다. 유니코드는 문자 코드의 국제 표준 관리 체계다. 

- encoding : 문자 -> 코드로 부호화.
  ASCII, EBCDIC, UTF-8, UTF-16, UTF-32. 여러 표준 관리체계가 있다.
  decoding : 부호화된 코드 -> 문자나 기호로 표현.

'''

#유니코드 표 참고하여 값을 찾았으며, \u는 유니코드 문자를 불러온다는 의미.

#1.정답
print('1.\n\u250c\u252C\u2510\n\u251c\u253c\u2524\n\u2514\u2534\u2518')


#2.정답
#a,b,c string type.
a = '\u250c\u252C\u2510\n'
b = '\u251c\u253c\u2524\n'
c = '\u2514\u2534\u2518'
print('2.\n' + a + b + c)


#3.오답
#\n의 개행 기능이 실현되지 않고 문자열 있는 그대로 리스트에 저장된다.
#list 자료형이니 출력 형태도 list 구조로 된다.
a = ['\u250c\u252C\u2510\n']
b = ['\u251c\u253c\u2524\n']
c = ['\u2514\u2534\u2518']
print('3.')
print(a + b + c)


#4.부연설명
'''
- UTF-8은 웹 상에서 보편적으로 사용하는 encoding 체계. ex) 주민등록번호 관리에 쓰인다.
- python에서는 utf-8의 코드값과 문자를 변환할 수 있는 함수를 지원한다.
      ord() : 문자 -> utf-8코드값(interger)
      chr() : utf-8코드값 -> 문자

'''
print('\n4.')
print(ord('┍'))  #9485 출력. 'ㅂ'한자로 특수문자 찾음.
print(chr(9485))  #┍ 출력.


'''
< OUTPUT > 
1. 
┌┬┐
├┼┤
└┴┘
2.
┌┬┐
├┼┤
└┴┘
3.
['┌┬┐\n', '├┼┤\n', '└┴┘']

4.
9485
┍
'''