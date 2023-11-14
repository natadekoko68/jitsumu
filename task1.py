idenshi_dict = {
    "Japanese":[35.0,11.1],
    "Chinese":[39.9,6.1],
    "Swedish Caucasian":[23.1,0.3],
    "Jewish Israell":[15.0,1.0],
    "Ethiopian":[13.6,1.8],
}

expression = {}

for key in idenshi_dict:
    a,b = idenshi_dict[key]
    a /= 100
    b /= 100
    expression[key] = (1-a-b)**2,2*(1-a-b)*(a+b),(a+b)**2

for key in expression:
    em, im, pm = expression[key]
    print(key)
    print("EM :",round(em*100,1),"%")
    print("IM :", round(im * 100, 1),"%")
    print("PM :", round(pm * 100, 1),"%")
    print("=====")
