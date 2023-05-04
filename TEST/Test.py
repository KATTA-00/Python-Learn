from trig import factorial
import math
n = 20


def e(x):
    val = 0
    for i in range(n):
        val += x**(i) / factorial(i)
    return val


def sin(x):
    return ((e(complex(0, x)) - e(-complex(0, x)))/(2j)).real


def cos(x):
    return ((e(complex(0, x)) + e(-complex(0, x)))/(2)).real


def tan(x):
    cos_x = cos(x)
    sin_x = sin(x)

    if cos_x == 0:
        return "INF" if sin_x > 0 else "-INF"
    return round(sin_x/cos_x, 5)
