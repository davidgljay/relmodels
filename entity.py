from random import randint 

class Entity:
    
    def __init__(self, config):
        #Even though it's a questionable practice, I'm importing config_vars as a dictionary. This will make fiddling
        #with entity attributes clearer later on.
        self.max_entropy = config["max_entropy"]  
        self.reduction_on_receive = config["reduction_on_receive"]
        self.increase_on_send = config["increase_on_send"]
        self.state_index = 0
        self.entropy = config["starting_entropy"]
        self.num_targets = config["num_targets"] 
        self.generate_state(config["state_array_length"],config["neighborhood_size"])
        
    #Randomly state_index based on entropy and returns a target
    def send(self):
        switch = 0
        if (randint(0,self.max_entropy) < self.entropy):
            switch = 1
            r = randint(0,1)
            if (r == 0):
                self.state_index -= 1
            else:
                self.state_index += 1
            if (self.state_index >= len(self.state)):
                self.state_index = 0
            if (self.state_index <= len(self.state)*-1):
                self.state_index = 0
        self.entropy += self.increase_on_send
        return [self.state[self.state_index], switch]
    
    #Lowers entropy when a bit is recieved
    def receive(self):
            self.entropy -= self.reduction_on_receive
            if self.entropy < 0:
                self.entropy = 0
     
    #Generates a range of states on initialization
    def generate_state(self, state_array_length, neighborhood_size):
        self.state = []
        for i in xrange(0, state_array_length):
            self.state.append([])
            for j in range(0, self.num_targets):
                x = randint(neighborhood_size*-1, neighborhood_size)
                y = randint(neighborhood_size*-1, neighborhood_size)
                if x == 0:
                    x = 1           
                self.state[-1].append((x,y))