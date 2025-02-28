#from AutomatFramwork import AutomatManager
from Global import DEBUG
from time import time

class AutomatStage:
    def __init__(self, ident:int, disc = ''):
        '''
        ident -> 特征id
        
        '''
        self.ident = ident
        self.disc = disc
        self.manager = None
        self.entryTime = 0
        pass
    
    def setName(self, disc:str):
        self.disc = disc
    
    def getName(self):
        return self.disc
        
    def getIdent(self):
        return self.ident
        
    def WORK(self):
        '''重写此方法以进行工作'''
        if DEBUG:
            print(f'状态{self.disc}操作函数未重写')
        
    def Entry(self):
        self.entryTime = time()
        self.WORK()
        return self.manager()
    
    def Exit(self):

        '''重写此函数以计算出口状态\n
        例:\n
        if(条件1):\n
            return 状态1\n
        elif(条件2):\n
            retuen 状态2\n
        retuen super().Exit()'''

        return self.ident #defalt
    
    