import AutomatFramwork
import AutomatStage
import time
class S1(AutomatStage.AutomatStage):
    def __init__(self, ident, manager):
        super().__init__(ident, manager)
        self.disc = '第一状态'
    def WORK(self):
        print('S1')
        time.sleep(0.1)
        
    def Exit(self):
        if True:
            return 2
        return super().Exit()


tester = AutomatFramwork.AutomatManager()

tester.addStage(S1(1,tester))

def newS2work():
    print('S2')
    time.sleep(0.1)
def newS2Exit():
    if True:
        return 1
S2 = AutomatStage.AutomatStage(2,tester)
tester.addStage(S2)
S2.WORK = newS2work
S2.Exit = newS2Exit
print(tester.StageDict.get(2).Exit())
tester.load()