import sqlite3
import entry
import targets

# leaderboard(user_id, score, FOREIGN KEY (user_id) REFERENCES users(user_id))

dbpath = 'ledger.db'


def addRow(user_id):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ncols = len(targets.getAllTargets())
    command = "INSERT INTO leaderboard VALUES ({}, 0".format(user_id)
    for i in range(1, ncols):
        command = command + ", 0"
    command = command + ")"   
    c.execute(command)
    conn.commit()
    command = "INSERT INTO weeklyboard VALUES ({}, 0".format(user_id)
    for j in range(1, ncols):
        command = command + ", 0"
    command = command + ")"   
    c.execute(command)
    conn.commit()
    conn.close()

def addCol(name):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute("ALTER TABLE leaderboard ADD COLUMN {} INTEGER DEFAULT 0".format(name))
    conn.commit()
    c.execute("ALTER TABLE weeklyboard ADD COLUMN {} INTEGER DEFAULT 0".format(name))
    conn.commit()
    conn.close()
    #c.execute("UPDATE leaderboard SET {}=0".format(name))

def getAll():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM leaderboard").fetchall()
    conn.close()
    return ret

def getWeek():
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM weeklyboard").fetchall()
    conn.close()
    return ret

def getCount(user_id, target, board):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT {} FROM {} WHERE user_id={}".format(target, board, user_id)).fetchall()
    conn.close()
    return ret[0][0]

def getScore(user_id,board):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT score FROM {} WHERE user_id={}".format(board, user_id)).fetchall()
    conn.close()
    return ret[0][0]

def update(ne):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    if ne.type_id == 1:
        c.execute("UPDATE leaderboard SET {}={} WHERE user_id={}".format(ne.target, getCount(ne.user_id, ne.target, "leaderboard")+1, ne.user_id))
        c.execute("UPDATE leaderboard SET score={} WHERE user_id={}".format(getScore(ne.user_id, "leaderboard")+ne.points, ne.user_id))
        c.execute("UPDATE weeklyboard SET {}={} WHERE user_id={}".format(ne.target, getCount(ne.user_id, ne.target, "weeklyboard")+1, ne.user_id))
        c.execute("UPDATE weeklyboard SET score={} WHERE user_id={}".format(getScore(ne.user_id, "weeklyboard")+ne.points, ne.user_id))
        conn.commit()
    elif ne.type_id == 2:
        c.execute("UPDATE leaderboard SET score={} WHERE user_id={}".format(getScore(ne.user_id,"leaderboard")+ne.points, ne.user_id))
        c.execute("UPDATE weeklyboard SET score={} WHERE user_id={}".format(getScore(ne.user_id, "weeklyboard")+ne.points, ne.user_id))
        conn.commit()
    conn.close()
    return

def reset():
    targs = targets.getAllTargets()
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    for targ in targs:
        tar = targ[1]
        if tar == 'dummy':
            continue
        c.execute("UPDATE weeklyboard SET {}=0".format(tar))
        conn.commit()
    c.execute("UPDATE weeklyboard SET score=0")
    conn.commit()
    conn.close()

def boardToPrint(board):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT * FROM users LEFT JOIN {} USING (user_id) ORDER BY score DESC".format(board)).fetchall()
    conn.close()
    header = targets.getTargetList()
    header.insert(0, None)
    header.insert(0, None)
    header.insert(0,"HUNTER")
    header.insert(0,None)
    header[4] = "Score"
    first = tuple(header)
    ret.insert(0, first)
    rett = []
    for i in ret:
        ii = i[1:2] + i[4:]
        rett.append(list(ii))
    return rett

def sbToPrint(board):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    ret = c.execute("SELECT user, score FROM users LEFT JOIN {} USING (user_id) ORDER BY score DESC".format(board)).fetchall()
    conn.close()
    header = ["HUNTER", "SCORE"]
    first = tuple(header)
    ret.insert(0, first)
    return ret