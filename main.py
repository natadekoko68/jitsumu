import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
from scipy.stats import linregress
import seaborn as sns

kenryosen_uox_quantity = [0,0.5,1,2,4,6,8]
kenryosen_uox_abs = [0.055,0.098,0.138,0.173,0.399,0.59,0.719]
kenryosen_opg_quantity = [0,2.5,5,7.5,10,12.5,15]
kenryosen_opg_abs = [0.042,0.101,0.147,0.18,0.219,0.28,0.329]


def uox(x):
    slope, intercept, r_value, p_value, std_err = linregress(kenryosen_uox_quantity, kenryosen_uox_abs)
    return (x-intercept)/slope

def opg(x):
    slope, intercept, r_value, p_value, std_err = linregress(kenryosen_opg_quantity, kenryosen_opg_abs)
    return (x-intercept)/slope

p = np.linspace(0,10,100)
plt.scatter(kenryosen_uox_quantity,kenryosen_uox_abs)

slope, intercept, r_value, p_value, std_err = linregress(kenryosen_uox_quantity, kenryosen_uox_abs)
plt.plot(p,slope*p+intercept)
plt.title("吸光度(590nm)と標準検体(mg/dL)の関係 (Uox)")
plt.text(6,0.5,"y = " + str(round(slope,4)) + "x + " + str(round(intercept,4)) +" \n ($R^{2}$ = " + str(round(r_value**2,4)) + ")")
plt.ylabel("吸光度(590nm)")
plt.xlabel("標準検体 (mg/dL)")
plt.xlim([0.0,10])
plt.ylim([0.0,0.8])
plt.grid()
plt.tight_layout()
plt.savefig("/Users/kotaro/Desktop/検量線(Uox).jpg")
plt.show()
plt.close()


p = np.linspace(0,20,100)
plt.scatter(kenryosen_opg_quantity,kenryosen_opg_abs)
slope, intercept, r_value, p_value, std_err = linregress(kenryosen_opg_quantity, kenryosen_opg_abs)
plt.plot(p,slope*p+intercept)
plt.title("吸光度(590nm)と標準検体(mg/dL)の関係 (Opg)")
plt.text(13,0.25,"y = " + str(round(slope,4)) + "x + " + str(round(intercept,4)) +" \n ($R^{2}$ = " + str(round(r_value**2,4)) + ")")
plt.ylabel("吸光度(590nm)")
plt.xlabel("標準検体 (mg/dL)")
plt.xlim([0.0,22])
plt.ylim([0.0,0.4])
plt.grid()
plt.xticks(np.arange(0, 22, 2))
plt.tight_layout()
plt.savefig("/Users/kotaro/Desktop/検量線(Opg).jpg")
plt.show()
plt.close()


sample_uox_abs = np.array([0.2165,0.214,0.2115,0.236,0.533,0.224,0.514,0.234])
sample_uox_name = ["1","2","3","4","5","P1","P2","P3"]
sample_opg_abs = np.array([0.419,0.364,0.4045,0.366,0.365,0.3595,0.385,0.434])
sample_opg_name = ["1","2","3","4","5","P1","P2","P3"]

# df_uox = pd.DataFrame(data=sample_uox_abs, index=sample_uox_name, columns=["Abs"])
# df_opg = pd.DataFrame(data=sample_opg_abs, index=sample_opg_name, columns=["Abs"])
# sns.barplot(x = df_uox.columns, y="Abs", data=df_uox)
# plt.show()

plt.title("サンプルごとの尿酸濃度(mg/dL)")
plt.bar(np.arange(1,9,1), uox(sample_uox_abs), tick_label=sample_uox_name)
plt.ylabel("濃度(mg/dL)")
plt.xlabel("各サンプル")
plt.savefig("/Users/kotaro/Desktop/結果(Uox).jpg")
plt.show()

plt.title("サンプルごとのリン酸濃度(mg/dL)")
plt.bar(np.arange(1,9,1), opg(sample_opg_abs), tick_label=sample_opg_name)
plt.ylabel("濃度(mg/dL)")
plt.xlabel("各サンプル")
plt.savefig("/Users/kotaro/Desktop/結果(Opg).jpg")
plt.show()