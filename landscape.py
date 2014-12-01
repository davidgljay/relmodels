from random import randint
from entity import Entity

class Landscape:
    
    #Initializes the landscape, creating entities in a 2d grid
    def __init__(self, size, density,entity_vars):
        self.transaction_log = []
        self.entropy_log = []
        self.switch_log = []
        self.output_log = []
        self.model = []
        for i in xrange(0, size-1):
            self.model.append([])
            for j in xrange(0, size-1):
                if (randint(0,100)<density):
                    self.model[-1].append(Entity(entity_vars))
                else:
                    self.model[-1].append(0)
                
    #Runs through each entity, transmitting bits and loging information about the entity
    def step(self):
        self.transaction_log.append([])
        self.entropy_log.append([])
        self.switch_log.append([])
        self.output_log.append([])
        for i in xrange(0,len(self.model)-1):
            for j in xrange(0,len(self.model[i])-1):
                if(self.model[i][j]):
                    entity = self.model[i][j]
                    if (entity.entropy < entity.max_entropy):
                        send = entity.send()
                        t = send[0]
                        self.switch_log[-1].append(send[1])
                        tx = t[0]+i
                        ty = t[1]+j
                        while(tx >= len(self.model)):
                            tx -= len(self.model)
                        while(ty >= len(self.model[i])):
                            ty -= len(self.model[i])

                        target = self.model[tx][ty]
                        if(target):
                            target.receive()
                            self.transaction_log[-1].append([(i,j),(tx,ty)])
                            self.output_log[-1].append(0)
                        else:
                            self.output_log[-1].append(1)
                    else:
                        self.output_log[-1].append(5)
                        self.switch_log[-1].append(2)
                        if (randint(0,1000) == 1):
                            entity.entropy = 20
                    self.entropy_log[-1].append(entity.entropy)
                    
                    
    def run(self, count):
        for i in xrange(1,count):
            self.step()
        logs = {"transaction_log":self.transaction_log, "entropy_log":self.entropy_log, 
                "output_log":self.output_log, "switch_log":self.switch_log}
        return logs