from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
   def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill="x")
#===========Variables==============
#============Cosmetics===========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
#============Grocery===========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.dall=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

#============Cold Drinks===========
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

#==========total Product Price & tax varibles======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

#==================Customer=======
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()





#==========customer Details===========

        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bd=5,fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold"),).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial,15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Contact No.",bg=bg_color,fg="white",font=("times new roman",15,"bold"),).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(F1,width=15,textvariable=self.c_phon,font="arial,15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold"),).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial,15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

#================Cosmetics============

        F2=LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),bd=5,fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=370)

        bath_lbl=Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w=Label(F2,text="face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g=Label(F2,text="hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_lbl_txt=Entry(F2,width=10,textvariable=self.loshan,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================Grocery Frame============

        F3=LabelFrame(self.root,text="Grocery",font=("times new roman",15,"bold"),bd=5,fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=370)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F3,width=10,textvariable=self.dall,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        wheat=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sugar=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_lbl_txt=Entry(F3,width=10,textvariable=self.tea,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================Cold Drink============

        F4=LabelFrame(self.root,text="Cold Drink",font=("times new roman",15,"bold"),bd=5,fg="gold",bg=bg_color)
        F4.place(x=675,y=180,width=325,height=370)

        maza_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cock=Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cock_txt=Entry(F4,width=10,textvariable=self.cock,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooti=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        thumbs_up=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        thumbs_up_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("tiems new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

##==================Bill Area==========

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=340,height=370)
        bill_title=Label(F5,text="Bill Area",font=("arial 15 bold"),bd=7,relief=GROOVE,).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

#=========Button Frame===Bill menu===================

        F6=LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),bd=5,fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=325,height=150)

        t1_lbl=Label(F6,text="Total Cosmetic Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=1,sticky="w")
        t1_txt=Entry(F6,width=15,textvariable=self.cosmetic_price,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        t2_lbl=Label(F6,text="Total Grocery Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=5,pady=1,sticky="w")
        t2_txt=Entry(F6,width=15,textvariable=self.grocery_price,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        t3_lbl=Label(F6,text="Total Cold Drinks Price",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=5,pady=1,sticky="w")
        t3_txt=Entry(F6,width=15,textvariable=self.cold_drink_price,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        tax1_lbl=Label(F6,text="Cosmetic Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=1,sticky="w")
        tax1_txt=Entry(F6,width=15,textvariable=self.cosmetic_tax,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        tax2=Label(F6,text="Grocery Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=5,pady=1,sticky="w")
        tax2_txt=Entry(F6,width=15,textvariable=self.grocery_tax,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        tax3_lbl=Label(F6,text="Cold Drinks Tax",font=("times new roman",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=5,pady=1,sticky="w")
        tax3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font=("arial 10 bold",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=800,width=540,height=105)

        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=5,pady=15,width=8,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=8,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=5,pady=15,width=8,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


   def total(self):
      self.c_s_p=self.soap.get()*40
      self.c_fc_p=self.face_cream.get()*120
      self.c_fw_p=self.face_wash.get()*60
      self.c_hs_p=self.spray.get()*180
      self.c_hg_p=self.gell.get()*140
      self.c_bl_p=self.loshan.get()*180

      self.total_cosmetic_price=float(
                                self.c_s_p+
                                self.c_fc_p+
                                self.c_fw_p+
                                self.c_hs_p+
                                self.c_hg_p+
                                self.c_bl_p
                                )
      self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
      self.c_tax=round((self.total_cosmetic_price*0.05),2)
      self.cosmetic_tax.set("Rs. "+str(self.c_tax))

      self.g_r_p=self.rice.get()*40
      self.g_f_p=self.food_oil.get()*120
      self.g_d_p=self.dall.get()*60
      self.g_w_p=self.wheat.get()*180
      self.g_s_p=self.sugar.get()*140
      self.g_t_p=self.tea.get()*180

      self.total_grocery_price=float(
                                self.g_r_p+
                                self.g_f_p+
                                self.g_d_p+
                                self.g_w_p+
                                self.g_s_p+
                                self.g_t_p
                                )
      self.grocery_price.set("Rs. "+str(self.total_grocery_price))
      self.g_tax=round((self.total_grocery_price*0.05),2)
      self.grocery_tax.set("Rs. "+str(self.g_tax))

      self.d_m_p=self.maza.get()*60
      self.d_c_p=self.cock.get()*60
      self.d_f_p=self.frooti.get()*50
      self.d_t_p=self.thumbsup.get()*45
      self.d_l_p=self.limca.get()*40
      self.d_s_p=self.sprite.get()*60

      self.total_cold_drink_price=float(
                                self.d_m_p+
                                self.d_c_p+
                                self.d_f_p+
                                self.d_t_p+
                                self.d_l_p+
                                self.d_s_p
                                )
      self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
      self.d_tax=round((self.total_cold_drink_price*0.05),2)
      self.cold_drink_tax.set("Rs. "+str(self.d_tax))

      self.Total_bill=float(
                         self.total_cosmetic_price+
                         self.total_grocery_price+
                         self.total_cold_drink_price+
                         self.c_tax+
                         self.g_tax+
                         self.d_tax
                        )
   def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome shopping mall")
        self.textarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()} ")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()} ")
        self.textarea.insert(END,f"\n=====================================")
        self.textarea.insert(END,f"\nProducts\t\t QTY\t\tPrice")
        self.textarea.insert(END,f"\n=====================================")

   def bill_area(self):

        if self.c_name.get()=="" or self.c_phon.get()=="":
                messagebox.showerror("Error","Customer detail are Must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
                messagebox.showerror("Error","No Product Purchesed")
        else:
                self.welcome_bill()
                #======cosmetics=======
                if self.soap.get()!=0:
                        self.textarea.insert(END,f"\nBath Soap\t\t {self.soap.get()}\t\t{self.c_s_p}")
                if self.face_cream.get()!=0:
                        self.textarea.insert(END,f"\nFace Cream\t\t {self.face_cream.get()}\t\t{self.c_fc_p}")
                if self.face_wash.get()!=0:
                        self.textarea.insert(END,f"\nFace Wash\t\t {self.face_wash.get()}\t\t{self.c_fw_p}")
                if self.spray.get()!=0:
                        self.textarea.insert(END,f"\nSpray\t\t {self.spray.get()}\t\t{self.c_hs_p}")
                if self.gell.get()!=0:
                        self.textarea.insert(END,f"\ngell\t\t {self.gell.get()}\t\t{self.c_hg_p}")
                if self.loshan.get()!=0:
                        self.textarea.insert(END,f"\nBody Loshan\t\t {self.loshan.get()}\t\t{self.c_bl_p}")

                #======Grocery=======
                if self.rice.get()!=0:
                        self.textarea.insert(END,f"\nrice\t\t {self.rice.get()}\t\t{self.g_r_p}")
                if self.food_oil.get()!=0:
                        self.textarea.insert(END,f"\nfood_oil\t\t {self.food_oil.get()}\t\t{self.g_f_p}")
                if self.dall.get()!=0:
                        self.textarea.insert(END,f"\nDall\t\t {self.dall.get()}\t\t{self.g_d_p}")
                if self.wheat.get()!=0:
                        self.textarea.insert(END,f"\nWheat\t\t {self.wheat.get()}\t\t{self.g_w_p}")
                if self.sugar.get()!=0:
                        self.textarea.insert(END,f"\nSugar\t\t {self.sugar.get()}\t\t{self.g_s_p}")
                if self.tea.get()!=0:
                        self.textarea.insert(END,f"\ntea\t\t {self.tea.get()}\t\t{self.g_t_p}")

                #======Cold Drink=======
                if self.maza.get()!=0:
                        self.textarea.insert(END,f"\nMaza\t\t {self.maza.get()}\t\t{self.d_m_p}")
                if self.cock.get()!=0:
                        self.textarea.insert(END,f"\nCock\t\t {self.cock.get()}\t\t{self.d_c_p}")
                if self.frooti.get()!=0:
                        self.textarea.insert(END,f"\nFrooti\t\t {self.frooti.get()}\t\t{self.d_f_p}")
                if self.thumbsup.get()!=0:
                        self.textarea.insert(END,f"\nThumbsup\t\t {self.thumbsup.get()}\t\t{self.d_t_p}")
                if self.limca.get()!=0:
                        self.textarea.insert(END,f"\nLimca\t\t {self.limca.get()}\t\t{self.d_l_p}")
                if self.sprite.get()!=0:
                        self.textarea.insert(END,f"\nSprite\t\t {self.sprite.get()}\t\t{self.d_s_p}")

                self.textarea.insert(END,f"\n-------------------------------------")
                if self.cosmetic_tax.get()!="Rs. 0.0":
                        self.textarea.insert(END,f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")


                if self.grocery_tax.get()!="Rs. 0.0":
                        self.textarea.insert(END,f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")


                if self.cold_drink_tax.get()!="Rs. 0.0":
                       self.textarea.insert(END,f"\nCold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

                self.textarea.insert(END,f"\n=====================================")
                self.textarea.insert(END,f"\nTotal Bill\t\t\tRs.{self.Total_bill}")
                self.textarea.insert(END,f"\n=====================================")
                self.save_bill()
   def save_bill(self):
        op=messagebox.askyesno("save Bill","do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"bill_no.: {self.bill_no.get()}"" Bill saved succefully")

        else:
            return

   def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")


   def clear_data(self):
        op=messagebox.askyesno("Do you want to clear?")
        if op>0:
# ============Cosmetics===========
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
    #============Grocery===========
            self.rice.set(0)
            self.food_oil.set(0)
            self.dall.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

    #============Cold Drinks===========
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

    #==========total Product Price & tax varibles======
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

    #==================Customer=======
            self.c_name.set("")
            self.c_phon.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

   def exit_app(self):
       op=messagebox.askyesno("Exite", "Do you want to Exit?")
       if op>0:
            self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()
