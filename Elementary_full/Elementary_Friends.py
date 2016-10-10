# -*- coding: utf-8 -*-

class Friends(object):
    def __init__(self, connections):
        self.connections = list(connections)
        

    def add(self, pair):
        if pair in self.connections:
            return False
        else:
            self.connections.append(pair)
            return True

    def remove(self, pair):
        if pair not in self.connections:
            return False
        else:
            self.connections.remove(pair)
            return True

    def names(self):
        name = set()
        for pair in self.connections:
            name.update(pair)
        return name

    def connected(self, name):
        connections = set()
        for pair in self.connections:
            if name in pair:
                connections.update(pair)
        if len(connections)>0:
            connections.remove(name)
        return connections

    
        
    def __repr__(self):
        return str(self.connections)

   
     
f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
print(f)
f.remove({"stephen", "robot"})
print(f)
f.names()

print(f)



