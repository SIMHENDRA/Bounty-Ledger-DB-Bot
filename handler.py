import entry
import re
import targets
import users
import entries
import bountyboard
import DB_init
from tabulate import tabulate

# claim <user> <target> proof <message>
# ledger <user> <points> proof <message>
# board <timescale>
# adduser <name> <ign>
# addtarget <name> <BV>
# changebounty <name> <BV>
# settleup
def handle(ip):
    command = getOp(ip)
    if command == "claim":
        print("handling claim")
        return handleClaim(ip)
    elif command == "ledger":
        print("handling ledger")
        return handleLedger(ip)
    elif command == "adduser":
        print("handling adduser")
        return handleUser(ip)
    elif command == "addtarget":
        print("handling add target")
        return handleTarget(ip)
    elif command == "changebounty":
        print("handling bounty change")
        return handleBounty(ip)
    elif command == "board":
        print("handling board req")
        return handleBoard(ip)
    elif command == "hardreset":
        print("hard resetting")
        return handleReset(ip)
    else:
        return "errrrrrr"

def getOp(ip):
    return ip.split()[0]

def getArgs(ip):
    res = re.findall(r"<[^<>]+>", ip)
    inputcmds = []
    for word in res:
        a = word.replace("<","")
        c = a.replace(">","")
        b = c.replace("'", "")
        inputcmds.append(b)
    return inputcmds 

def handleClaim(ip):
    ne = claimEntry(ip)
    entries.add(ne)
    bountyboard.update(ne)
    return None

def handleLedger(ip):
    ne = ledgerEntry(ip)
    entries.add(ne)
    bountyboard.update(ne)
    return None

def handleUser(ip):
    imputcmds = getArgs(ip)
    users.put(imputcmds[0],imputcmds[1]) 
    return None

def handleTarget(ip):
    inputcmds = getArgs(ip)
    targets.put(inputcmds[0],float(inputcmds[1]))
    return None

def handleBounty(ip):
    inputcmds = getArgs(ip)
    targets.changeBounty(inputcmds[0],float(inputcmds[1]))
    return None

def handleBoard(ip):
    inputcmds = getArgs(ip)
    if inputcmds[0] == "alltime":
        return lbInput("leaderboard")
    elif inputcmds[0] == "weekly":
        return lbInput("weeklyboard")
    return "arg error"

def handleReset(ip):
    DB_init.initDB()

def claimEntry(ip):
    inputcmds = getArgs(ip)
    proof = re.findall("https:\/\/streamable\.com\/[\S]+",ip)[0]
    ret = entry.Entry('claim',inputcmds[0], inputcmds[1], None, proof, inputcmds[2])
    return ret

def ledgerEntry(ip):
    inputcmds = getArgs(ip)
    proof = re.findall("https:\/\/streamable\.com\/[\S]+",ip)[0]
    ret = entry.Entry('ledger',inputcmds[0], 'dummy', float(inputcmds[1]), proof, inputcmds[2])
    return ret

def lbInput(ip):
    table = bountyboard.boardToPrint(ip)[1:]
    return tabulate(table, headers=bountyboard.boardToPrint(ip)[0])







# testentry = claimEntry("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# entries.add(testentry)
# dockentry = ledgerEntry("ledger <Squish> <-4.5> https://streamable.com/rmxqv332 <remtest>")
# entries.add(dockentry)
# print(entries.getAll())
