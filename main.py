import tkinter as tk

durum_text = ""
def bmi_calculate():
    global durum_text

    #eğer kullanıcı boş bırakırsa
    if not weight_entry.get() or not height_entry.get():
        durum_label.config(text="Lütfen değer giriniz!")
        return

    try:
        weight = float(weight_entry.get())
        cm_height = float(height_entry.get())
        if cm_height < 10: # kullanıcı metre olarak değer girerse,
            cm_height = cm_height * 100 #100 ile çarparak cm'ye dönüştürür.

        if weight > 300 or cm_height > 300: #anlamsız değerler girerse,
            durum_label.config(text="Lütfen geçerli değerler giriniz")
            return

        m_height = cm_height / 100
        sonuc = weight / (m_height * m_height)
        bmi = round(sonuc,2)
        print(bmi)

        if bmi <= 18.40:
            durum_text = "Underweight"
        elif bmi <= 24.90:
            durum_text = "Normal"
        elif bmi <= 39.90:
            durum_text = "Overweight"
        else:
            durum_text = "Obese"

        durum_label.config(text=f"BMI değeriniz: {bmi} = {durum_text}")

    except ValueError:
        durum_label.config(text="Lütfen sayı giriniz!")

#UYGULAMA EKRANI
window= tk.Tk()
window.title("tkinter BMI")
window.minsize(width=200,height=200)
window.config(pady=40,padx=40)

#KİLO LABEL
weight_label = tk.Label(text="Kilonuzu giriniz (kg)")
weight_label.pack()

#KİLO ENTRY
weight_entry = tk.Entry(width=10)
weight_entry.pack()
weight_entry.focus()

#BOY LABEL
height_label = tk.Label(text="Boyunuzu giriniz (cm)")
height_label.pack()

#BOY ENTRY
height_entry = tk.Entry(width=10)
height_entry.pack()

#CALCULATE BUTONU
btn_calculate = tk.Button(text="Calculate",command=bmi_calculate)
btn_calculate.pack()

#SONUC LABEL
durum_label = tk.Label(text="")
durum_label.pack()

window.mainloop()

