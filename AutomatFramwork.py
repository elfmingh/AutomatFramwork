from AutomatStage import AutomatStage
from Global import DEBUG
import time
class AutomatManager:
    class EMG(AutomatStage):
        def __init__(self, manager):
            super().__init__(-1, manager)
            self.sigEMG = False
            self.sigBack = False
        def Exit(self):
            if not self.sigEMG:
                if self.sigBack:
                    self.manager.lastStage = self.manager.shadowStage[0]
                    return self.manager.shadowStage[1]
                else:
                    return 0
            return -1
            
        def reset(self):
            self.sigEMG = False
            self.sigBack = False
    
    
    def __init__(self):
        '''推荐重写增加功能'''
        #控制区
        self.StageDict = {}
        self.stgEMG = self.EMG(self)
        self.addStage(self.stgEMG)
        init = AutomatStage(0,self,'初始化')
        init.Exit = self.exitINIT
        init.WORK = self.workINIT
        self.addStage(init)
        self.lastStage = 0
        self.currentStage = 0
        self.nextStage = 0
        self.shadowStage = [0,0,0]
        self.sigEMG = False
        self.timestep = 0.05
        self.startTime = time.time()
    
    
    def addStage(self, stage:AutomatStage):
        '''不需重写'''
        if stage.getIdent() in self.StageDict:
            if DEBUG:
                print('Automat Manager->addStage->Wrong stage ident')
            raise Exception('Manager: Fail adding stage')
        stage.manager = self
        self.StageDict[stage.getIdent()] = stage
        
                
    def cpyStatus(self):
        '''不需重写'''
        self.shadowStage[0] = self.lastStage
        self.shadowStage[1] = self.currentStage
        self.shadowStage[2] = self.nextStage


    def __call__(self):
        '''不需重写'''
        self.currentStage = self.nextStage


    def switch(self):
        if self.sigEMG:
            self.cpyStatus()
            self.nextStage = -1
        #if DEBUG:
        #    print(self.currentStage, self.nextStage)
        if self.nextStage == self.currentStage:

            try:
                self.nextStage = self.StageDict.get(self.currentStage).Exit()
            except:
                if DEBUG:
                    print(f'Automat Manager->switch->Error in exiting current Stage->{self.StageDict.get(self.currentStage).getName()}')
                raise Exception('Wrong in exiting current stage')
        else:
            try:
                self.StageDict.get(self.currentStage).Entry()
            except:
                if DEBUG:
                    print(f'Automat Manager->switch->Error in entrying next Stage->{self.StageDict.get(self.currentStage).getName()}')
                raise Exception('Wrong in exiting current stage')
        time.sleep(self.timestep)
    
    
    def quit(self):
        '''应当根据需求重写退出机制'''
        if time.time()-self.startTime > 60:
            return True
        return False
    
    
    def load(self):
        while True:
            self.switch()
            if self.quit():
                break
            
            
    def exitINIT(self):
        '''必须重写：定义从初始化阶段退出的条件'''
        return 1
    
    
    def workINIT(self):
        '''可选重写：定义初始化阶段的工作内容'''
        print('跳过初始化阶段')