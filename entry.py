import targets
import users
import entryTypes

class Entry:
    
    def __init__(self, op, user, target, points, proof, msg):

        self.op = op
        self.user = user
        self.target = target
        self.msg = msg
        self.proof = proof

        if points:
            self.points = points
        else:
            self.points = targets.getBounty(target)

        self.user_id = users.getID(user)
        self.target_id = targets.getID(target)
        targets.incrKC(target)
        self.type_id = entryTypes.getID(op)
    




# entries(
#     entry_id INTEGER PRIMARY KEY, 
#     type_id INTEGER, 
#     user_id INTEGER, 
#     target_id INTEGER, 
#     points FLOAT, 
#     entryDT TIMESTAMP, 
#     entryMSG TEXT, 


#     FOREIGN KEY (type_id) REFERENCES entryTypes(type_id),
#     FOREIGN KEY (user_id) REFERENCES users(user_id),
#     FOREIGN KEY (target_id) REFERENCES targets(target_id)
#     )
