import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode


def qrolustur():
    url= urlgeldi.get()
    if url:
        qr_url=pyqrcode.create(url)
        dosyayolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG dosyaları","*.svg")])
        if dosyayolu:
            qr_url.svg(dosyayolu, scale=8)
            durum_etiketi.config(text="QR kod oluşturuldu ve kaydedildi")


#tasarım
pencere=tk.Tk()
pencere.title("QR kod oluşturucu")
pencere.resizable(False,False)
etiket=tk.Label(pencere,text="URL GİRİN")
urlgeldi=tk.Entry(pencere,width=40)
buton=tk.Button(pencere,text="Oluştur",command=qrolustur)
durum_etiketi=tk.Label(pencere,text="")
etiket.grid(row=0,column=0,padx=10,pady=10)
urlgeldi.grid(row=0,column=1,padx=10,pady=10)
buton.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
pencere.mainloop()