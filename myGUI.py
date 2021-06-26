
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import tkinter as tk
#daha önce oluşturmuş olduğum dataseti koduma dahil ettim
data= pd.read_csv('C:/Users/Kutay/Desktop/Bitirme projesi/Pythpn Codes/datasetCovit19.csv')
#Tkinter kütüphnesini kontrol edebilmek için
gui=tk.Tk()
gui.geometry("900x900+200+150")
gui.title("Covit-19 Risk Belirleme Uygulaması")

tk.Label(text="Covit-19 Risk Belirleme Uygulaması",font=150).pack()
tk.Label(text="Covit-19 hastalığına yakalanırsanız durmunuz ne kadar kötü olabileceğini tahmin eden bir sistem ",font=120).pack()

#entry (text box)lardan gelen data'yı kaydetmek için kullanılan StringVar fonkisyonu
ageInfo=tk.StringVar()
heightInfo=tk.StringVar()
weightInfo=tk.StringVar()
sporInfo=tk.StringVar()
smokerInfo=tk.StringVar()
cronichInfo=tk.StringVar()
# Entrylerin başlangıcı
tk.Label(text="Lütfen yaşınızı girin.. örneğin 18").pack()
age=tk.Entry(textvariable=ageInfo).pack()
tk.Label(text="Lütfen boyunuzu cm cinsinden girin.. örneğin 180").pack()
height=tk.Entry(textvariable=heightInfo).pack()
tk.Label(text="Lütfen kilonuzu kg cinsinden girin.. örneğin 70").pack()
weight=tk.Entry(textvariable=weightInfo).pack()
tk.Label(text="Devamlı olarak spor yapıyorsanız 1 yapmıyorsanız 0 giriniz").pack()
spor=tk.Entry(textvariable=sporInfo).pack()
tk.Label(text="Sigara içiyorsanız 1 içmiyorsanız 0 giriniz").pack()
smoker=tk.Entry(textvariable=smokerInfo).pack()
tk.Label(text="Kronik bir hastalığınız varsa 1 giriniz yoksa 0 giriniz").pack()
cronich=tk.Entry(textvariable=cronichInfo).pack()

#   Y'ler
risk=data.RiskGroup.values.reshape(-1,1)
#  X'ler
degerler=data.iloc[:,[0,3,5,6,7]].values
# instance from class
reg=LinearRegression()
#multiple regression fitine x ve y vermek
reg.fit(degerler,risk)

# buton tıklanınca yapılacak işler:
def btnClick():
    # vucüt kitle indexi hesaplayıp daha sonra prediction işlemi yapabilmek için
    bmi=int(weightInfo.get())/((int(heightInfo.get()))/100)**2
    # tahminlerin yapılması 
    sonuc=reg.predict(np.array([[int(ageInfo.get()),bmi,int(sporInfo.get()),int(smokerInfo.get()),int(cronichInfo.get())]]))

   # Sonuca göre risk belirlemesi yapan ve ekrana yazdıran kısım
    if sonuc<=2 and sonuc>=1:
        lblSonuc.config(text="Sonuç: Orta risklisiniz "+str(sonuc[0][0]),fg='gray')     
    elif sonuc>2:
        lblSonuc.config(text="Sonuç: Çok risklisiniz "+ str(sonuc[0][0]),fg='red')
    elif sonuc<1:
        lblSonuc.config(text="Sonuç: Az risklisiniz "+str(sonuc[0][0]), fg='green')
# butonun yapılandırılması ve btnClick metoduna bağlanması   
btn=tk.Button(text="Risk Hesapla",command=btnClick).pack()
# Kullanıcı bilgilendirme 
tk.Label(text="0-1 arası az riskli",font=90,fg='green').pack()
tk.Label(text="1-2 arası orta riskli",font=90,fg='gray').pack()
tk.Label(text="2 ve üzeri çok riskli",font=900,fg='red').pack()
# Sonuc labeli btna tıklanınca değişir
lblSonuc=tk.Label(text="Sonuç: ")
lblSonuc.pack()
tk.mainloop()