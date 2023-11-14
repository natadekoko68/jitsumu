idensi_tsui_receptor = ["WW", "Wm", "mm"]
idensi_tsui_cyp2d6 = ["WW", "Wm", "mm"]
hindo_receptor = [0.64, 0.32, 0.04]
hindo_cyp2d6 = [0.25, 0.5, 0.25]
p_receptor = [10, 5, 2]
q_receptor = [300, 150, 60]
activity_cyp2d6 = [100, 60, 20]
AUC_cyp2d6 = [1, 10 / 6, 5]


def soukou_ritsu(p, auc):
    return auc / (p + auc) * 100

def soukou_ritsu_80(p,auc_bairitsu):
    """
    0.8 = a*bairitsu/(a*bairitsu+p)
    thus a = 4p/bairitsu
    :param p:
    :return: a
    """
    return 4*p/auc_bairitsu

def hukusayo_ritsu(q, auc):
    return auc / (q + auc) * 100


def hindo(x, y):
    return x*y*100


sum_soko = 0
sum_hukusayo = 0


print("問1")
for i in range(3):
    for j in range(3):
        type_receptor = idensi_tsui_receptor[i]
        type_cyp2d6 = idensi_tsui_cyp2d6[j]
        hindo_receptor_temp = hindo_receptor[i]
        hindo_cyp2d6_temp = hindo_cyp2d6[j]
        p_temp = p_receptor[i]
        q_temp = q_receptor[i]
        AUC_temp = 40 * AUC_cyp2d6[j]
        print("受容体", type_receptor, "- CYP2D6", type_cyp2d6)
        print("頻度", round(hindo(hindo_receptor_temp, hindo_cyp2d6_temp),1), "%")
        print("奏効率", round(soukou_ritsu(p_temp, AUC_temp),1), "%")
        print("副作用発現率", round(hukusayo_ritsu(q_temp, AUC_temp),1), "%")
        print("====")
        sum_soko += hindo(hindo_receptor_temp, hindo_cyp2d6_temp) / 100 * soukou_ritsu(p_temp, AUC_temp) / 100
        sum_hukusayo += hindo(hindo_receptor_temp, hindo_cyp2d6_temp) / 100 * hukusayo_ritsu(q_temp, AUC_temp) / 100
print("")
print("問2")
print("全体")
print("奏効率", round(sum_soko * 100, 1), "%")
print("副作用発現率", round(sum_hukusayo * 100, 1), "%")

print("")
print("問3")
sum_80_hukusayo = 0
for i in range(3):
    for j in range(3):
        type_receptor = idensi_tsui_receptor[i]
        type_cyp2d6 = idensi_tsui_cyp2d6[j]
        hindo_receptor_temp = hindo_receptor[i]
        hindo_cyp2d6_temp = hindo_cyp2d6[j]
        p_temp = p_receptor[i]
        q_temp = q_receptor[i]
        AUC_temp = soukou_ritsu_80(p_temp, AUC_cyp2d6[j]) * AUC_cyp2d6[j]
        print("受容体", type_receptor, "- CYP2D6", type_cyp2d6)
        print("頻度", round(hindo(hindo_receptor_temp, hindo_cyp2d6_temp),1), "%")
        assert(round(soukou_ritsu(p_temp, AUC_temp),1)==80.0)
        print("副作用発現率", round(hukusayo_ritsu(q_temp, AUC_temp),1), "%")
        print("====")
        sum_80_hukusayo += hindo(hindo_receptor_temp, hindo_cyp2d6_temp) / 100 * hukusayo_ritsu(q_temp, AUC_temp) / 100
print("全体")
print("副作用発現率", round(sum_80_hukusayo * 100, 1), "%")

print("")
print("問4")
print("差", round((sum_hukusayo-sum_80_hukusayo)*100,1), "%")
print(round(1/(sum_hukusayo-sum_80_hukusayo),2),"人以上 =",int(1/(sum_hukusayo-sum_80_hukusayo))+1,"人必要")