import magic
import time
import pandas as pd
X = pd.read_csv('D:\\cell500gene1000.csv') #读取表达矩阵
X = X.drop([X.columns[0]], axis=1)
X = X.transpose()

magic_operator = ma.MAGIC()
X_magic = magic_operator.fit_transform(X)
X_magic = X_magic.transpose() #填补结果
#X_magic.to_csv('E:/Magic/模拟/0/Magic.csv') 写入