import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pickle
from sklearn.pipeline import make_pipeline
import numpy as np
import pandas as pd

def printvar(a):
    new_option = [i for i in laptop_card if gpubrand_laptop.get() in i]
    gpu_laptop['values'] = [*new_option]




root = tk.Tk()
root.geometry("650x700")
df1 = pickle.load(open('laptop dataset\linearregression.pkl', 'rb'))
print(df1)
bg = ImageTk.PhotoImage(Image.open("laptop dataset/back.jpg").resize((650,700), Image.ANTIALIAS))
  
# Create Canvas
canvas1 = tk.Canvas( root, width = 650,
                 height =700)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
# #C48EFE
style = ttk.Style(root)
style.configure("TFrame", background="#96ACB9")
style.configure('TLabel',background='#96ACB9')
company_name = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[0]
print(company_name)
laptop_type = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[1]
print(laptop_type)

laptop_processor = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[2]
print(laptop_processor)

laptop_card = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[3]
print(laptop_card)

laptop_os = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[4]
print(laptop_os)

laptop_cardcompany = df1.named_steps['columntransformer'].named_transformers_['onehotencoder'].categories[5]
print(laptop_cardcompany)

def predict_model():
    resolution = res_laptop.get().split('x')
    y_pred1=df1.predict(pd.DataFrame([[company.get(),type_laptop.get(),float(inch.get()),cpu_laptop.get(),int(ram_laptop.get()),gpu_laptop.get(),opsys_laptop.get(),float(weight_laptop.get()),touch_laptop.get(),int(resolution[0]),int(resolution[1]),ips_laptop.get(),int(hdd_laptop.get()),int(ssd_laptop.get()),gpubrand_laptop.get()]],
                             columns= ['Company', 'TypeName', 'Inches', 'Cpu', 'Ram', 'Gpu', 'OpSys', 'Weight','touchscreen', 'y_res', 'x_res', 'IPS', 'HDD', 'SSD', 'Gpu_Brand']))
    print(np.exp(y_pred1))
    prediction.config(text=np.exp(y_pred1)[0])
    prediction.pack()
    frame16.pack()
    frame16_canvas = canvas1.create_window( 200, 680, anchor='nw',
                                       window = frame16 , width=270)
frame17 = ttk.Frame(root)
img = ImageTk.PhotoImage(Image.open("laptop dataset\download.jpeg").resize((35,50), Image.ANTIALIAS))
label2 = tk.Label(frame17,image=img)
label2.pack(side=tk.LEFT,padx=10)
label1 = tk.Label(frame17,text='LAPTOP PRICE PREDICTION' , font=('',24), background='#BBC4FE')
label1.pack(side = tk.LEFT , padx=50)
head = canvas1.create_window( 0, 0,anchor='nw',
                                       window = frame17 , width=700)
# name of company
frame = ttk.Frame(root)
ttk.Label(frame,text='Company',font=('',16)).pack(side=tk.LEFT, padx=5)
company_selected = tk.StringVar()
company = ttk.Combobox(frame,textvariable=company_selected)
company['values'] = [*company_name]
company.pack(side=tk.RIGHT, padx=5,pady=5)
frame.pack(pady=10)
heading = canvas1.create_window( 0, 10,anchor='nw',
                                       window = frame , width=700)

frame_canvas = canvas1.create_window( 200, 80, 
                                       anchor = "nw",
                                       window = frame,width=270)
#type of laptop
frame1 = ttk.Frame(root)
ttk.Label(frame1,text='Type',font=('',16)).pack(side=tk.LEFT, padx=5)
type_selected = tk.StringVar()
type_laptop = ttk.Combobox(frame1,textvariable=type_selected)
type_laptop['values'] = [*laptop_type]
type_laptop.pack(side=tk.RIGHT, padx=5)
frame1.pack()
frame1_canvas = canvas1.create_window( 200, 120, 
                                       anchor = "nw",
                                       window = frame1 , width=270)
#inches
frame2 = ttk.Frame(root)
ttk.Label(frame2,text='Inches',font=('',16)).pack(side=tk.LEFT, padx=5)
inches = tk.IntVar()
inch = tk.Entry(frame2, textvariable=inches)
inch.pack(side=tk.RIGHT, padx=5)
frame2.pack()
frame2_canvas = canvas1.create_window( 200, 160, 
                                       anchor = "nw",
                                       window = frame2 , width=270)
#cpu 
frame3 = ttk.Frame(root)
ttk.Label(frame3,text='Cpu',font=('',16)).pack(side=tk.LEFT, padx=5)
cpu_selected = tk.StringVar()
cpu_laptop = ttk.Combobox(frame3,textvariable=cpu_selected)
cpu_laptop['values'] = [*laptop_processor]
cpu_laptop.pack(side=tk.RIGHT, padx=5)
frame3.pack()
frame3_canvas = canvas1.create_window( 200, 200, 
                                       anchor = "nw",
                                       window = frame3 , width=270)

# ram
frame4 = ttk.Frame(root)
ttk.Label(frame4,text='Ram',font=('',16)).pack(side=tk.LEFT, padx=5)
ram = tk.IntVar()
ram_laptop = ttk.Combobox(frame4,textvariable=ram)
ram_laptop['values'] = [2,4,6,8,12,16,24,32,64]
ram_laptop.pack(side=tk.RIGHT, padx=5)
frame4_canvas = canvas1.create_window( 200, 240, 
                                       anchor = "nw",
                                       window = frame4 , width=270)
# gpu_brand
frame5 = ttk.Frame(root)
ttk.Label(frame5,text='Gpu Brand',font=('',16)).pack(side=tk.LEFT, padx=5)
gpubrand_selected = tk.StringVar()
gpubrand_laptop = ttk.Combobox(frame5,textvariable=gpubrand_selected)
gpubrand_laptop['values'] = [*laptop_cardcompany]
gpubrand_laptop.pack(side=tk.RIGHT, padx=5)
gpubrand_laptop.bind('<<ComboboxSelected>>', printvar)
frame5.pack()
frame5_canvas = canvas1.create_window( 200, 280, 
                                       anchor = "nw",
                                       window = frame5 , width=270)
#gpu
frame6 = ttk.Frame(root)
ttk.Label(frame6,text='Gpu',font=('',16)).pack(side=tk.LEFT, padx=5)
gpu_selected = tk.StringVar()
gpu_laptop = ttk.Combobox(frame6,textvariable=gpu_selected)
gpu_laptop.pack(side=tk.RIGHT, padx=5)
frame6.pack()
frame6_canvas = canvas1.create_window( 200, 320, 
                                       anchor = "nw",
                                       window = frame6 , width=270)

#opsys
frame7 = ttk.Frame(root)
ttk.Label(frame7,text='OS',font=('',16)).pack(side=tk.LEFT, padx=5)
opsys_selected = tk.StringVar()
opsys_laptop = ttk.Combobox(frame7,textvariable=opsys_selected)
opsys_laptop['values'] = [*laptop_os]
opsys_laptop.pack(side=tk.RIGHT, padx=5)
frame7.pack()
frame7_canvas = canvas1.create_window( 200, 360, 
                                       anchor = "nw",
                                       window = frame7 , width=270)
#weight
frame8 = ttk.Frame(root)
ttk.Label(frame8,text='Weight',font=('',16)).pack(side=tk.LEFT, padx=5)
weight = tk.IntVar()
weight_laptop = tk.Entry(frame8, textvariable=weight)
weight_laptop.pack(side=tk.RIGHT, padx=5)
frame8.pack()
frame8_canvas = canvas1.create_window( 200, 400, 
                                       anchor = "nw",
                                       window = frame8 , width=270)

#touchscreen
frame9 = ttk.Frame(root)
ttk.Label(frame9,text='Touchscreen',font=('',16)).pack(side=tk.LEFT, padx=5)
touch_selected = tk.StringVar()
touch_laptop = ttk.Combobox(frame9,textvariable=touch_selected)
touch_laptop['values'] = [0,1]
touch_laptop.pack(side=tk.RIGHT, padx=5)
frame9.pack()
frame9_canvas = canvas1.create_window( 200, 440, 
                                       anchor = "nw",
                                       window = frame9 , width=270)
# screenresolution
frame10 = ttk.Frame(root)
ttk.Label(frame10,text='Resolution WxH',font=('',16)).pack(side=tk.LEFT, padx=5)
res = tk.StringVar()
res_laptop = tk.Entry(frame10, textvariable=res)
res_laptop.pack(side=tk.RIGHT, padx=5)
frame10.pack()
frame10_canvas = canvas1.create_window( 200, 480, anchor='nw',
                                       window = frame10 , width=270)

#IPS
frame11 = ttk.Frame(root)
ttk.Label(frame11,text='IPS',font=('',16)).pack(side=tk.LEFT,padx=5)
ips_selected = tk.IntVar()
ips_laptop = ttk.Combobox(frame11,textvariable=ips_selected)
ips_laptop['values'] = [0,1]
ips_laptop.pack(side=tk.RIGHT, padx=5)
frame11.pack()
frame11_canvas = canvas1.create_window( 200, 520, anchor='nw', window=frame11,width=270)

# HDD
frame12 = ttk.Frame(root)
ttk.Label(frame12,text='HDD (IN GB)',font=('',16)).pack(side=tk.LEFT, padx=5)
hdd = tk.StringVar()
hdd_laptop = tk.Entry(frame12, textvariable=hdd)
hdd_laptop.pack(side=tk.RIGHT, padx=5)
frame12.pack()
frame12_canvas = canvas1.create_window( 200, 560, anchor='nw',
                                       window = frame12 , width=270)

# SSD
frame14 = ttk.Frame(root)
ttk.Label(frame14,text='SSD (IN GB)',font=('',16)).pack(side=tk.LEFT, padx=5)
ssd = tk.StringVar()
ssd_laptop = tk.Entry(frame14, textvariable=ssd)
ssd_laptop.pack(side=tk.RIGHT, padx=5)
frame14.pack()
frame14_canvas = canvas1.create_window( 200, 600, anchor='nw',
                                       window = frame14 , width=270)

# submit
frame15 = ttk.Frame(root)
submit = tk.Button(frame15,text='PREDICT' , command=predict_model).pack(padx=5)
frame15.pack()
frame15_canvas = canvas1.create_window( 200, 640, anchor='nw',
                                       window = frame15 , width=270)

# output
frame16 = ttk.Frame(root)
prediction = tk.Label(frame16)

root.mainloop()