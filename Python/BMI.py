# bmi.py
# -*- coding: utf-8 -*-
# 参照: https://gist.github.com/LouP-PV/65f3ff2ba2564e85a889787e993ba023
# BMI判定プログラム

weight = float(input("体重(kg)は？:"))
height = float(input("身長(cm)は？:")) / 100
bmi = round(weight / (height ** 2),1)

if bmi < 18.5:
    BMI_CATEGORY = "痩せ型"
elif (bmi >= 18.5) and (bmi < 25):
    BMI_CATEGORY = "標準体型"
elif (bmi >= 25) and (bmi < 30):
    BMI_CATEGORY = "肥満(軽)"
else:
    BMI_CATEGORY = "肥満(重)"

print("BMI: " + str(bmi))
print("判定: " + BMI_CATEGORY)
