
from numpy import random
import pandas as pd

Age=[]
height=[]
weight=[]
BMI=[] #body math index
Gender=[]
athlete=[]
smoker=[]
AnotherChronicIllness=[]
riskGroup=[] # if 0 there is  no risk-------- if 1 there is medium risk----- if 2 there is high risk
Sex=["Male","Female"]
YesNo=["Yes","No"]


for i in range(20000):
    Age.append(random.randint(10,120))
    height.append(random.randint(140, 210))
    weight.append(random.randint(40, 130))
    Gender.append(random.choice(Sex))
    athlete.append(random.choice([1,0],p=[0.4,0.6]))
    smoker.append(random.choice([1,0],p=[0.3,0.7]))
    AnotherChronicIllness.append(random.choice([1,0],p=[0.1,0.9]))
#Body math index hesaplama
for i in range(20000):
    BMI.append(weight[i] / (height[i]/100)**2)


    
data = {'Age':  Age,
        'Height':height,
       'Weight':weight,
       'BMI':BMI,
        'Gender':Gender,
        'Athlete':athlete,
        'Smoker':smoker,
        'AnotherChronic':AnotherChronicIllness,

        }
Dataset=pd.DataFrame(data)
# Risk Grupları belirleme
for i in Dataset.values:
    #************************* Riskli Grup (2)*******************************
    if (i[0]>=75): # yaş 75ten büyükse başka kritere bakmaya gerek duymadan riskli olarak belirle
        riskGroup.append(2)
    # yaşı 60 ile 75 arasına olup spor yapmayan veya sigara içen riskli say    
    elif ((i[0]>=60 and i[0]<75) and i[5]==0 ) or ((i[0]>=60 and i[0]<75) and i[6]==1):
        riskGroup.append(2)
    elif (i[3]<20 or i[3]>=40): # BMI bu değerlerde olursa riskli say
        riskGroup.append(2)
    #yaşa bakmadan kronik rahatsızlık varsa riskli say
    elif (i[7]==1):
        riskGroup.append(2)
    #************************* Orta Riskli Grup (1)*******************************
    # 60 ile 75 yaşlarında geri kalanlar orta riskli
    elif (i[0]>=60 and i[0]<75):
        riskGroup.append(1)
    #geri kalanlar hepsi riskiz
    elif i[0]<=16:
        riskGroup.append(0)    
    elif  i[5]==1:
        riskGroup.append(0)
        
    else:
        riskGroup.append(0)
Dataset['RiskGroup']=riskGroup

        
    
Dataset.to_csv (r'C:/Users/Kutay/Desktop/Bitirme projesi/Pythpn Codes/datasetCovit19.csv', index = False, header=True)
