import pandas as pd
import numpy as np


chat_id = 1882360450 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    from statsmodels.stats.proportion import proportions_ztest
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(count, nobs)
    if pval<=0.01: 
        answer=True
    else:
        answer=False

    return answer 

