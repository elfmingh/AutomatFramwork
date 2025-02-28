from AutomatFramwork import AutomatManager
from Const import DEBUG
from time import time

class AutomatStage:
    def __init__(self, ident:int, manager:AutomatManager):
        '''
        ident -> 特征id
        
        '''
        self.ident = ident
        self.disc = ''
        self.manager = manager
        self.entryTime = 0
        pass
    
    def setName(self, disc:str):
        self.disc = disc
    
    def getName(self):
        return self.disc
        
    def getIdent(self):
        return self.ident
        

        
    def Entry(self):
        self.entryTime = time()
        '''重新此方法以完成状态操作'''
        return True
    
    def Exit(self):
        '''if(出口条件):    return 下一个状态'''
        
        return self.ident
    
    