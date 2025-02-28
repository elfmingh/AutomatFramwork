from AutomatStage import AutomatStage
from Const import DEBUG
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
        #控制区
        self.StageDict = {}
        self.stgEMG = self.EMG(self)
        self.addStage(self.stgEMG)
        self.lastStage = 0
        self.currentStage = 0
        self.nextStage = 0
        self.shadowStage = [0,0,0]
        self.sigEMG = False
        self.timestep = 0.05
        self.startTime = time.time()
    
    def addStage(self, stage:AutomatStage):
        for loaded_stage in self.StageList:
            if loaded_stage.getIdent() == stage.getIdent():
                if DEBUG:
                    print('Automat Manager->addStage->Wrong stage ident')
                raise Exception('Manager: Fail adding stage')
        self.dict[stage.getIdent()] = stage
        
                
    def cpyStatus(self):
        self.shadowStage[0] = self.lastStage
        self.shadowStage[1] = self.currentStage
        self.shadowStage[2] = self.nextStage

    def switch(self):
        if self.sigEMG:
            self.cpyStatus()
            self.nextStage = -1
        if self.nextStage == self.currentStage:
            self.nextStage = self.dict.get(self.currentStage).Exit()
        else:
            self.currentStage = self.nextStage
            self.dict.get(self.currentStage).Entry()
        
        time.sleep(self.timestep)
    
    def quit(self):
        '''推荐重写退出机制'''
        if time.time()-self.startTime > 60:
            return True
        return False
    
    def __call__(self, *args, **kwds):
        while True:
            self.switch()
            if self.quit():
                break
            
    