import numpy as np
from tkinter import *
from collections import Counter
from tkinter import messagebox
from tkinter import simpledialog

d1 = []

def mode(lst):
    # 使用Counter来统计每个元素出现的次数
    count_elements = Counter(lst)
    # 找到出现次数最多的元素
    max_count = max(count_elements.values())
    # 返回出现次数最多的元素列表
    return [element for element, count in count_elements.items() if count == max_count]

class weighfun():
    def __init__(self,e1,e2,e3):
        self.d1 = []
        self.a = False
        self.all_1 = 0
        self.b=False
        self.l2=[]
        self.l1=[]
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

        self.res1 = self.e1.get()
        self.res2 = self.e2.get()
        self.res3 = self.e3.get()
        try:
            self.res3 = int(self.res3)
            if self.res1 != "" and self.res2 != "":
                self.res2 = self.res2.replace("，", ",", len(self.res1))
                self.res1 = self.res1.replace("，", ",", len(self.res1))
                self.l1 = self.res1.split(",")
                self.lll = self.res2.split(",")

                try:
                    for i in self.lll:
                        if len(self.lll) == 1 and int(self.lll[0]) == 0:
                            for cao in self.l1:
                                self.l2.append(1)
                            print("wocnm")
                        else:
                            self.l2.append(float(i))

                    for i in self.res1:
                        for m in i:
                            if m.isdigit() or m=="," or m==".":
                                self.a=True
                            else:
                                messagebox.showerror("数据错误","原数据输入不正确")
                                self.a=False
                                break

                    for n in self.res2:
                        if n.isnumeric() or n==",":
                            self.b=True
                        else:
                            messagebox.showerror("数据错误","权重数据输入不正确")
                            self.b=False
                            break

                    if len(self.l1) != len(self.l2):
                        messagebox.showerror("数据错误","权重数据与原数据输入不一致")
                        self.b=False
                except:
                    messagebox.showerror("警告","数据输入异常1")
            else:
                messagebox.showerror("警告","数据输入异常2")
        except:
            messagebox.showerror("警告","保留小数位数输入异常3")

    def average(self):  
        if self.a and self.b:
            information = ""
            d1 =[]
            messagebox.showinfo("开始计算","即将开始计算")
            for i in self.l1:
                self.all_1 += int(i)*self.l2[self.l1.index(i)]
                d1.append(i+"的权数为:" + str(int(i)*self.l2[self.l1.index(i)]))
            print("权数总和为：", self.all_1)
            for data_1 in d1:
                information = information + data_1 + ",     "
                information = information[0:-1]
            print(information)
            print(self.l2)
            messagebox.showinfo("原数据各个权数:", information[0:-5])
            messagebox.showinfo("计算结果", "加权平均数为："+str(format(self.all_1/sum(self.l2), ".{}f".format(self.res3))))
    
    def others(self):
        if self.a and self.b:
            number = []
            for i in self.l1:
                number.append(float(format(float(i)*self.l2[self.l1.index(i)], ".4f".format(self.res3))))
                print(format(float(i)*self.l2[self.l1.index(i)], ".{}f".format(self.res3)))


            messagebox.showinfo("计算结果:", "数据计算结果为为："+str(number))
            messagebox.showinfo("计算结果:", "数据计算众数为："+str(mode(number))) 
            messagebox.showinfo("计算结果:", "数据中位数为："+str(np.median(number)))
            messagebox.showinfo("计算结果:", "数据方差为："+str(np.var(number)))

def callback(window, root):
    window.destroy()
    root.deiconify()
    
def callback1(root):
    if messagebox.askokcancel("关闭窗口", "确定要结束求平均值吗？"):
        root.destroy()
    
def am():
    m = []
    global main_window
    main_window.withdraw()
    data = simpledialog.askstring("数组","请输入原数据：（逗号隔开）")
    dof = simpledialog.askinteger("保留小数：","请输入保留位数：")
    b = 0.0
    if data == None:
        dof=3
        messagebox.showerror("警告","数据输入异常5")
        main_window.deiconify()
    elif dof == None:
        messagebox.showerror("警告","数据输入异常6")
        main_window.deiconify()
    else:
        res = data.replace("，", ",", len(data))
        try:
            for i in res.split(","):
                m.append(float(i))
            
            for i in m:
                if i !=",":
                    try:
                        float(i)
                        a=True
                    except ValueError:
                        a = False
                        messagebox.showerror("数据错误","原数据输入不正确")
                        main_window.deiconify()
                        break
        except:
            a = False
            messagebox.showerror("数据错误","原数据输入不正确")
            main_window.deiconify()


        if a:
            num1 = Counter(m)
            mean = np.sum(m)/len(m)
            for i in m:
                b += float(i)
            b=format(b,".{}f".format(dof))
            messagebox.showinfo("统计结果","统计所得频次为："+str(num1))
            messagebox.showinfo("统计结果","数据和为：%s" % b)
            messagebox.showinfo("统计结果", "平均数为: {}".format(mean,".{}f".format(dof)))
            main_window.deiconify()

def wa():
    global main_window
    main_window.withdraw()
    am_window = Toplevel(main_window)
    am_window.resizable(False,False)
    am_window.geometry("530x400")
    am_window.protocol("WM_DELETE_WINDOW",lambda:callback(am_window, main_window))
    main_window.withdraw()

    e1 = Entry(am_window,font=("kaiti", 20), width=30, bd=10, justify=CENTER)
    e1.place(relx=0.5, rely=0.15, anchor="center")
    Label(am_window, font=('华文新魏',15), text="请输入一组数代表原数据(逗号隔开):",bg="pink",relief="ridge").place(relx=0.5, rely=0.05, anchor="center")

    e2 = Entry(am_window,font=("kaiti", 20), width=30, bd=10, justify=CENTER)
    e2.place(relx=0.5, rely=0.42, anchor="center")
    Label(am_window, font=('华文新魏',15), text="请输入原数据所占比例权重（逗号隔开）",bg="red",relief="ridge").place(relx=0.5, rely=0.28, anchor="center")
    Label(am_window, font=('华文新魏',8), text="单独输入0时默认为算术平均数",bg="#00fa9a",relief="ridge").place(relx=0.5, rely=0.34, anchor="center")

    e3 = Entry(am_window, font=("kaiti", 20), width=30, bd=10, justify=CENTER)
    e3.place(relx=0.5, rely=0.68, anchor="center")
    Label(am_window, font=('华文新魏',15), text="请输入小数保留位数：",bg="green",relief="ridge").place(relx=0.5, rely=0.59, anchor="center")

    Button(am_window,text="开始计算加权平均数", command=lambda:weighfun(e1,e2,e3).average(), width=18, font=('华文楷体',20),height=1).place(relx=0.25, rely=0.91, anchor="center")
    Button(am_window,text="开始计算小四个", command=lambda:weighfun(e1,e2,e3).others(), width=18, font=('华文楷体',20),height=1).place(relx=0.75, rely=0.91, anchor="center")

    am_window.mainloop()


main_window = Tk()
main_window.resizable(False,False)
main_window.geometry("400x200")
main_window.title("平均数神器——by LYK")



# Button(main_window, text="算数平均数", font=("宋体", 17, "bold"), command=lambda:am()).place(relx=0.5, rely=0.3, anchor="center")
Button(main_window, text="加权平均数", font=("宋体", 17, "bold"), command=lambda:wa()).place(relx=0.5, rely=0.5, anchor="center")

main_window.protocol("WM_DELETE_WINDOW", lambda:callback1(main_window))
main_window.mainloop()

