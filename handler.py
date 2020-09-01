import entry
import re
from operations import targets, users, entries, bountyboard

# claim <user> <target> proof <message>
# ledger <user> <points> proof <message>
# board <timescale>
# settleup

def handleClaim(ip):
    ne = claimEntry(ip)
    entries.add(ne)
    bountyboard.update(ne)

def handleLedger(ip):
    ne = ledgerEntry(ip)
    entries.add(ne)
    bountyboard.update(ne)

def claimEntry(ip):
    res = re.findall(r"<[^<>]+>", ip)
    inputcmds = []
    for word in res:
        a = word.replace("<","")
        c = a.replace(">","")
        b = c.replace("'", "")
        inputcmds.append(b)
        #print(b)
    #print(len(inputcmds))
    proof = re.findall("https:\/\/streamable\.com\/[\S]+",ip)[0]
    #print("target:" + inputcmds[1])
    ret = entry.Entry('claim',inputcmds[0], inputcmds[1], None, proof, inputcmds[2])
    return ret
    


def ledgerEntry(ip):
    res = re.findall(r"<[^<>]+>", ip)
    inputcmds = []
    for word in res:
        a = word.replace("<","")
        c = a.replace(">","")
        b = c.replace("'", "")
        inputcmds.append(b)
        #print(b)
    #print(len(inputcmds))
    proof = re.findall("https:\/\/streamable\.com\/[\S]+",ip)[0]
    #print("target:" + inputcmds[1])
    ret = entry.Entry('ledger',inputcmds[0], 'dummy', float(inputcmds[1]), proof, inputcmds[2])
    return ret

def lbInput(ip):
    pass



# testentry = claimEntry("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# entries.add(testentry)
# dockentry = ledgerEntry("ledger <Squish> <-4.5> https://streamable.com/rmxqv332 <remtest>")
# entries.add(dockentry)
# print(entries.getAll())