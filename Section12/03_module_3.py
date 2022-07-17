# 모듈에서 원하는 함수 및 변수를 읽어올 때
# from converter import kilometer_to_miles
# from converter import gram_to_pound
from converter import *

miles = kilometer_to_miles(150)
print('150km --> {}miles'.format(miles))

pound = gram_to_pound(2000)
print('2000gram --> {}pound'.format(pound))