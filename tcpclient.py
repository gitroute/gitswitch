import socket
import time
class myclient:
          def __init__(self):
                    self.phone=1
                    self.content=None
                    self.respondContent=None
                    self.nextsend=0
          def sendonce(self,a):
                    self.phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket must construct every time
                    self.phone.connect(('10.11.16.12',6666))
                    if a:
                              self.content=str(a).strip()
                              print(self.content)
                              self.phone.send(self.content.encode('utf-8'))
                              self.nextsend=1
                    else:
                              print('请不要发送空值')
                              self.nextsend=0
                    try:
                              if self.nextsend==0:
                                    self.phone.send('NONE'.encode('utf-8'))#in case bad tcp finish
                              self.phone.settimeout(5)
                              self.respondContent=self.phone.recv(1025)
                              print('.....................................',self.respondContent.decode('utf-8'))
                    except:
                              print('timeout')
                    self.phone.close()#shutdown link after once send
class save2local:
          def __init__(self,file='1'):
                    self.pathfile='c:\\computers'+file+'.txt'
          def save(self,a):
                    self.f=open(self.pathfile,'w')
                    self.f.write(a)
                    self.f.close()

class save2locald:
          def __init__(self,file='1'):
                    self.pathfile='d:\\computers'+file+'.txt'
          def save(self,a):
                    self.f=open(self.pathfile,'w')
                    self.f.write(a)
                    self.f.close()

class save2locale:
          def __init__(self,file='1'):
                    self.pathfile='e:\\computers'+file+'.txt'
          def save(self,a):
                    self.f=open(self.pathfile,'w')
                    self.f.write(a)
                    self.f.close()
