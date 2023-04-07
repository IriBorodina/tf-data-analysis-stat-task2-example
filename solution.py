import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import norm


chat_id = 5223715667 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len (x)
    return x.max()/(2*alpha**(1./n)), \
           x.max()/2
