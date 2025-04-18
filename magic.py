import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Math calculations with no functions defined
# Adding 5 & 4 = 9
5 + 4
# Displaying Variable 'a' and its value
a = 5
"a =", a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

df = pd.DataFrame({'col1': [1,2]})
"dataframe", df

# Magic working on Charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart