import numpy as np
import pandas as pd

def model_implement():
    random_array = np.random.randint(0, 20, size=100, dtype=int)
    even_odd = ['even' if x%2==0 else 'odd' for x in random_array]
    return even_odd

print(model_implement())
