import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ----------pic1---------------
# 讀取資料
vitamin = pd.read_csv('vitamin.csv')

# 產生圖表
sns.lineplot(x='unit', y='Pr', hue = 'type', data = vitamin);
# 設定圖表參數
plt.title('vitamin')
plt.xlabel('unit')
plt.ylabel('Pr')
plt.yticks([])
plt.show()


# -----------pic2--------------

# 產生圖表
sns.lineplot(x='unit', y='Pr', hue = 'type', data = vitamin);

# 標準線
x = range(1,25)
y4 = [6]*24
plt.plot(x, y4, linestyle='--', c = 'red')

# 產生圖表
y4 = range(0,7)
x1 = [7.3]*7
x2 = [21.8]*7
plt.plot(x1, y4, linestyle='--', c = 'red')
plt.plot(x2, y4, linestyle='--', c = 'red')

# 設定圖表參數
plt.title('vitamin')
plt.xlabel('unit')
plt.ylabel('Pr')
plt.yticks([])
plt.show()
