import pandas as pd
import numpy as np


chat_id = 1882360450 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
       
    import scipy.stats as st
    df = np.array([[x_success, x_cnt - x_success], [y_success, y_cnt - y_success]])
    res = st.chi2_contingency(df)
    if res[1]<=0.01: 
        answer=True
    else:
        answer=False

    return answer 

