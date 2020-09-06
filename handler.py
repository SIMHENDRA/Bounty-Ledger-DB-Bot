import entry
import re
import targets
import users
import entries
import bountyboard
import DB_init
from tabulate import tabulate
import discord
from datetime import datetime

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
        print("handling claim : " + ip)
        return handleClaim(ip)
    elif command == "ledger":
        print("handling ledger : " + ip)
        return handleLedger(ip)
    elif command == "adduser":
        print("handling adduser : " + ip)
        return handleUser(ip)
    elif command == "addtarget":
        print("handling add target : " + ip)
        return handleTarget(ip)
    elif command == "changebounty":
        print("handling bounty change : " + ip)
        return handleBounty(ip)
    elif command == "board":
        print("handling board req : " + ip)
        ret = handleBoard(ip)
        print(ret)
        today = datetime.now()
        d1 = today.strftime("%d/%m/%Y %H:%M:%S")
        head = """---
title: {} Leaderboard
author: The sheriff
date: {}
output: html_document
---""".format(getArgs(ip)[0], d1)
        f = open("leaderboard.Rmd", 'w')
        f.write(head + "\n```\n" + ret + "\n```")
        f.close()
        rett = discord.File("leaderboard.Rmd")
        return rett
    elif command == "hardreset":
        print("hard resetting : " + ip)
        return handleReset(ip)
    elif command == "softreset":
        print("soft reseting : " + ip)
        return handleSoftReset(ip)
    elif command == "kills":
        print("getting entry list : " + ip)
        return handleEntryboard(ip)
    elif command == "targets":
        print("printing targets" + ip)
        return handleTargetBoard(ip)
    elif command == "score":
        print("printing score" + ip)
        return handleScoreboard(ip)
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

def handleScoreboard(ip):
    inputcmds = getArgs(ip)
    if inputcmds[0] == "alltime":
        return sbInput("leaderboard")
    elif inputcmds[0] == "weekly":
        return sbInput("weeklyboard")
    return "arg error"


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

def handleEntryboard(ip):
    return entriesInput("entryDT")

def handleTargetBoard(ip):
    return targetInput(ip)

def handleReset(ip):
    DB_init.initDB()
    return None

def handleSoftReset(ip):
    bountyboard.reset()
    return None

def claimEntry(ip):
    inputcmds = getArgs(ip)
    prooflist = re.findall("http[\S]+",ip)
    if len(prooflist) == 0:
        proof = "proofless"
    else:
        proof = prooflist[0]
    ret = entry.Entry('claim',inputcmds[0], inputcmds[1], None, proof, inputcmds[2])
    return ret

def ledgerEntry(ip):
    inputcmds = getArgs(ip)
    prooflist = re.findall("http[\S]+",ip)
    if len(prooflist) == 0:
        proof = "proofless"
    else:
        proof = prooflist[0]
    ret = entry.Entry('ledger',inputcmds[0], 'dummy', float(inputcmds[1]), proof, inputcmds[2])
    return ret

def lbInput(ip):
    table = bountyboard.boardToPrint(ip)[1:]
    return tabulate(table, headers=bountyboard.boardToPrint(ip)[0])

def sbInput(ip):
    table = bountyboard.sbToPrint(ip)
    return tabulate(table[1:], headers=table[0] )

def entriesInput(ip):
    table = entries.entriesToPrint(ip)
    return tabulate(table[1:], headers=table[0])

def targetInput(ip):
    table = targets.targetsToPrint()
    return tabulate(table[1:], headers=table[0])



# testentry = claimEntry("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# entries.add(testentry)
# dockentry = ledgerEntry("ledger <Squish> <-4.5> https://streamable.com/rmxqv332 <remtest>")
# entries.add(dockentry)
# print(entries.getAll())
