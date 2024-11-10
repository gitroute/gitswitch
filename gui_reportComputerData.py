import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
#from tcpclient import myclient
from tcpclient import save2local
from tcpclient import save2locald
from tcpclient import save2locale
from yingjian import Yingjian
'''transform xml 2 xlsx,but not ordinary xml,only downloaded from web'''
class transform:
	def __init__(self):
		self.w=tk.Tk()
		print(1)
		self.w.title('hello')
		print(2)
		self.var1,self.var2,self.var3,self.var4,self.var5,self.var6,self.var7,self.var8,self.var9,self.var10=tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
		self.var11,self.var12,self.var13,self.var14=tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
		self.var100=tk.StringVar()
		self.var1.set('泰州欢迎您')
		self.var100.set('  version:1.3.2')
		print(3)
		self.w.geometry('300x550+150+70')
		print(33)
		self.entry_show1=tk.Entry(self.w,textvariable=self.var1,width=20)
		self.entry_show2=tk.Entry(self.w,textvariable=self.var2,width=20)
		self.entry_show3=tk.Entry(self.w,textvariable=self.var3,width=20)
		self.entry_show4=tk.Entry(self.w,textvariable=self.var4,width=20)
		self.entry_show5=tk.Entry(self.w,textvariable=self.var5,width=20)
		self.entry_show6=tk.Entry(self.w,textvariable=self.var6,width=20)
		self.entry_show7=tk.Entry(self.w,textvariable=self.var7,width=20)
		self.entry_show8=tk.Entry(self.w,textvariable=self.var8,width=20)
		self.entry_show9=tk.Entry(self.w,textvariable=self.var9,width=20)
		self.entry_show10=tk.Entry(self.w,textvariable=self.var10,width=20)
		self.entry_show11=tk.Entry(self.w,textvariable=self.var11,width=20)
		self.entry_show12=tk.Entry(self.w,textvariable=self.var12,width=20)
		self.entry_show13=tk.Entry(self.w,textvariable=self.var13,width=20)
		self.entry_show14=tk.Entry(self.w,textvariable=self.var14,width=20)
		self.entry_show100=tk.Entry(self.w,textvariable=self.var100,width=30)#单行文本框，只能设置宽度，最底下一个

		self.label1=tk.Label(self.w,text='reserve')
		self.label2=tk.Label(self.w,text='姓名')
		self.label3=tk.Label(self.w,text='部门')
		self.label4=tk.Label(self.w,text='备注')##开机用户名
		self.label5=tk.Label(self.w,text='主机名')
		self.label6=tk.Label(self.w,text='mac')
		self.label7=tk.Label(self.w,text='台式机')
		self.label8=tk.Label(self.w,text='品牌型号')##操作系统版本
		self.label9=tk.Label(self.w,text='SNbios')#授权码
		self.label10=tk.Label(self.w,text='SNboard')
		self.label11=tk.Label(self.w,text='硬盘')
		self.label12=tk.Label(self.w,text='内存')
		self.label13=tk.Label(self.w,text='CPU')
		self.label14=tk.Label(self.w,text='显卡')
		self.label100=tk.Label(self.w,text='')#标签无大小，最底下一个标签不放
		
		self.resp=None
		print(4)
		#Button only discript its width and height,not mean where to place it
		self.button1=tk.Button(self.w,text='保存到C:',width=15,height=1,command=self.click_button1)
		self.button2=tk.Button(self.w,text='D:',width=2,height=1,command=self.click_button2)
		self.button3=tk.Button(self.w,text='E:',width=2,height=1,command=self.click_button3)
		self.button365=tk.Button(self.w,text='xml转换成xlsx',width=15,height=1,command=self.click_button365)
		print(5)
		self.files=None
		self.path_without_file=''
		self.gouzao()
		print('---------------------------')
		self.getInformation()
		print(60)
	def placeEntry(self):#entry放在左边
		print(6)
		self.entry_show1.place(x=10,y=10,anchor='nw')
		self.entry_show2.place(x=10,y=110)
		self.entry_show3.place(x=10,y=140)
		self.entry_show4.place(x=10,y=170)
		self.entry_show5.place(x=10,y=200)
		self.entry_show6.place(x=10,y=230)
		self.entry_show7.place(x=10,y=260)
		self.entry_show8.place(x=10,y=290)
		self.entry_show9.place(x=10,y=320)
		self.entry_show10.place(x=10,y=350)
		self.entry_show11.place(x=10,y=380)
		self.entry_show12.place(x=10,y=410)
		self.entry_show13.place(x=10,y=440)
		self.entry_show14.place(x=10,y=470)
		self.entry_show100.place(x=10,y=500)
		#print('entry place end')
	def placeClickButton(self):
		#print(10)
		self.button1.place(x=10,y=50)
		self.button2.place(x=150,y=50)
		self.button3.place(x=190,y=50)
		#self.button4.place(x=20,y=110)
		#print('button place end')
	def placeLabel(self):#label从右边放起
		self.label1.place(x=170,y=10)
		self.label2.place(x=170,y=110)
		self.label3.place(x=170,y=140)
		self.label4.place(x=170,y=170)
		self.label5.place(x=170,y=200)
		self.label6.place(x=170,y=230)
		self.label7.place(x=170,y=260)
		self.label8.place(x=170,y=290)
		self.label9.place(x=170,y=320)
		self.label10.place(x=170,y=350)
		self.label11.place(x=170,y=380)
		self.label12.place(x=170,y=410)
		self.label13.place(x=170,y=440)
		self.label14.place(x=170,y=470)
		#self.label100.place(x=170,y=500)#最底下一个标签不放

	def showfiles(self):
		print(self.files)

	def click_button100(self):##send by net
		#print(9)
		'''if pressed , messagebox out'''
		mm=myclient()
		if 1:
			a1=(self.entry_show2.get()+'%;'+self.entry_show3.get()+'%;'+self.entry_show4.get()+'%;'+self.entry_show5.get()\
                            +'%;'+self.entry_show6.get()+'%;'+self.entry_show7.get()+'%;'+self.entry_show8.get()+'%;'+self.entry_show9.get()\
                            +'%;'+self.entry_show10.get()+'%;'+self.entry_show11.get()+'%;'+self.entry_show12.get()+'%;'+self.entry_show13.get()\
                            +'%;'+self.entry_show14.get())
			mm.sendonce(a1)
			messagebox.showinfo(title='get files',message='数据已发送')
		else:
			messagebox.showinfo(title='get files',message=self.files)
		self.var100.set(mm.respondContent)
	def click_button1(self):#don't send ,only save 2 local c partition
		#print(9)
		'''if pressed , messagebox out'''
		name=self.entry_show2.get()
		mm=save2local(name)
		if 1:
			a1=(self.entry_show2.get()+'\n'+self.entry_show3.get()+'\n'+self.entry_show4.get()+'\n'+self.entry_show5.get()\
                            +'\n'+self.entry_show6.get()+'\n'+self.entry_show7.get()+'\n'+self.entry_show8.get()+'\n'+self.entry_show9.get()\
                            +'\n'+self.entry_show10.get()+'\n'+self.entry_show11.get()+'\n'+self.entry_show12.get()+'\n'+self.entry_show13.get()\
                            +'\n'+self.entry_show14.get())
			mm.save(a1)
			messagebox.showinfo(title='get files',message='已保存到c盘computers.xlsx')
		else:
			messagebox.showinfo(title='get files',message=self.files)
		self.var100.set('已保存')
	def click_button2(self):#don't send ,only save 2 local d partition
		#print(9)
		'''if pressed , messagebox out'''
		name=self.entry_show2.get()
		mm=save2locald(name)
		if 1:
			a1=(self.entry_show2.get()+'\n'+self.entry_show3.get()+'\n'+self.entry_show4.get()+'\n'+self.entry_show5.get()\
                            +'\n'+self.entry_show6.get()+'\n'+self.entry_show7.get()+'\n'+self.entry_show8.get()+'\n'+self.entry_show9.get()\
                            +'\n'+self.entry_show10.get()+'\n'+self.entry_show11.get()+'\n'+self.entry_show12.get()+'\n'+self.entry_show13.get()\
                            +'\n'+self.entry_show14.get())
			mm.save(a1)
			messagebox.showinfo(title='get files',message='已保存到d盘computers.xlsx')
		else:
			messagebox.showinfo(title='get files',message=self.files)
		self.var100.set('已保存')
	def click_button3(self):#don't send ,only save 2 local e partition
		#print(9)
		'''if pressed , messagebox out'''
		name=self.entry_show2.get()
		mm=save2locale(name)
		if 1:
			a1=(self.entry_show2.get()+'\n'+self.entry_show3.get()+'\n'+self.entry_show4.get()+'\n'+self.entry_show5.get()\
                            +'\n'+self.entry_show6.get()+'\n'+self.entry_show7.get()+'\n'+self.entry_show8.get()+'\n'+self.entry_show9.get()\
                            +'\n'+self.entry_show10.get()+'\n'+self.entry_show11.get()+'\n'+self.entry_show12.get()+'\n'+self.entry_show13.get()\
                            +'\n'+self.entry_show14.get())
			mm.save(a1)
			messagebox.showinfo(title='get files',message='已保存到e盘computers.xlsx')
		else:
			messagebox.showinfo(title='get files',message=self.files)
		self.var100.set('已保存')
	def click_button365(self):
		'''if pressed , transform xml to xlsx'''
		self.xml2xlsx()

	def gouzao(self):
		self.placeEntry()#place entry to window
		self.placeLabel()#place label
		#self.click_button1()#show info by a pop-up window
		self.placeClickButton()
#################################################################

	def getInformation(self):
		info=Yingjian()
		mac_addr=info.checkMac()#fetch mac ok########################
		laptop=info.checkNotebook()#fetch laptop or desktop ok##########
		bosn=info.checkBoardsn()#fetch mainboard sn ok##########
		bisn=info.checkBiossn()#fetch bios sn ok##########
		br=info.checkBrand()#fetch brand and model ok##########
		hostname=info.checkHostname()#fetch hostname ok########
		disk=info.checkDisk()#fetch hostname ok########
		ram=info.checkRam()#fetch hostname ok########
		cpu=info.checkCPU()#fetch hostname ok########
		gpu=info.checkGPU()#fetch hostname ok########
		#self.var2.set(2)
		#self.var3.set(3)
		#self.var4.set(4)
		self.var5.set(hostname)#LAPTOP-81K1EUFR
		self.var6.set(mac_addr)#{{'以太网': '6C:24:08:0A:41:9D'}} {{'WLAN': 'E0:0A:F6:87:D9:17'}}
		self.var7.set(laptop)###laptop
		self.var8.set(br)######LENOVO 82KC
		self.var9.set(bisn)####PF3LAC2S
		self.var10.set(bosn)###PF3LAC2S
		self.var11.set(disk)####{SAMSUNG MZALQ512HBLU-00BL2}
		self.var12.set(ram)####{{'P0 CHANNEL A': 8}} {{'P0 CHANNEL B': 8}}
		self.var13.set(cpu)####{AMD Ryzen 5 5500U with Radeon Graphics}
		self.var14.set(gpu)####{OrayIddDriver Device} {Sharing Monitor} {AMD Radeon(TM) Graphics}
		#self.var100.set()
		return [hostname,mac_addr,laptop,br,bisn,bosn,disk,ram,cpu,gpu]#10 datas
	def generate_path(self):
		'''indicate has file already'''
		b=self.files[0].split('/')
		b.pop()
		name=''
		for i in b:
			i+='/'
			name+=i
		self.path_without_file=name
	

if __name__=='__main__':
        get=transform()
        tk.mainloop()
