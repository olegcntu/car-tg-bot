import simpful as sf
from simpful import Trapezoidal_MF, FuzzySet, LinguisticVariable

fs = sf.FuzzySystem()
x1 = sf.AutoTriangle(n_sets=2, terms=['no', 'yes'], universe_of_discourse=[0, 1])
fs.add_linguistic_variable(name='x1', LV=x1)

x2_L = FuzzySet(function=Trapezoidal_MF(a=-1.677, b=-0.406, c=0.406, d=1.677), term='L')
x2_A = FuzzySet(function=Trapezoidal_MF(a=0.625, b=2.292, c=2.708, d=4.375), term='A')
x2_H = FuzzySet(function=Trapezoidal_MF(a=3.125, b=4.792, c=5.21, d=6.875), term='H')

fs.add_linguistic_variable("x2", LinguisticVariable([x2_L, x2_A, x2_H], universe_of_discourse=[0, 5]))

x3_L = FuzzySet(function=Trapezoidal_MF(a=-1.677, b=-0.406, c=0.406, d=1.677), term='L')
x3_A = FuzzySet(function=Trapezoidal_MF(a=0.625, b=2.292, c=2.708, d=4.375), term='A')
x3_H = FuzzySet(function=Trapezoidal_MF(a=3.125, b=4.792, c=5.21, d=6.875), term='H')

fs.add_linguistic_variable("x3", LinguisticVariable([x3_L, x3_A, x3_H], universe_of_discourse=[0, 5]))

x4_L = FuzzySet(function=Trapezoidal_MF(a=-1.677, b=-0.406, c=0.406, d=1.677), term='L')
x4_A = FuzzySet(function=Trapezoidal_MF(a=0.625, b=2.292, c=2.708, d=4.375), term='A')
x4_H = FuzzySet(function=Trapezoidal_MF(a=3.125, b=4.792, c=5.21, d=6.875), term='H')

fs.add_linguistic_variable("x4", LinguisticVariable([x4_L, x4_A, x4_H], universe_of_discourse=[0, 5]))

x5 = sf.AutoTriangle(n_sets=2, terms=['no', 'yes'], universe_of_discourse=[0, 1])  # трикутна ф-я належності
fs.add_linguistic_variable(name='x5', LV=x5)
y = sf.AutoTriangle(n_sets=10, terms=['TS', 'TB', 'RL', 'RS', 'BM', 'BX', 'AMG', 'GLE', 'MA', 'LM'],
                    universe_of_discourse=[0, 10])
fs.add_linguistic_variable(name='y', LV=y)
fs.add_rules_from_file(path='C://Users//oleg//Desktop//rules.txt')


def get_car(y):
    car = ''
    if 0 <= y <= 1:
        car = 'TS'
    elif 1 < y <= 2:
        car = 'TB'
    elif 2 < y <= 3:
        car = 'RL'
    elif 3 < y <= 4:
        car = 'RS'
    elif 4 < y <= 5:
        car = 'BM'
    elif 5 < y <= 6:
        car = 'BX'
    elif 6 < y <= 7:
        car = 'AMG'
    elif 7 < y <= 8:
        car = 'GLE'
    elif 8 < y <= 9:
        car = 'MA'
    elif 9 < y <= 10:
        car = 'LM'
    return car
