import DB_init
from operations import targets
from operations import entryTypes
from operations import users
from operations import bountyboard
from operations import entries
import handler
import os
from tabulate import tabulate
dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\data\\ledger.db'

if input("This will clear current DB. Continue?") != 'Y':
    quit()
if os.path.exists("data/ledger.db"):
    os.remove("data/ledger.db")
if os.path.exists("ledger.db"):
    os.remove("ledger.db")

DB_init.initDB()
# entryTypes.put("claim")
# entryTypes.put("ledger")

testip = [
    "addtarget <Adam> <10.0>",
    "addtarget <Sixth> <9.5>",
    "addtarget <VTE> <3>",
    "adduser <DEFYN> <DEFYN>",
    "adduser <Squish> <unknown>",
    "adduser <ssn> <simhendramadhya_>",
    "claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>",
    "ledger <Squish> <-4.5> https://streamable.com/rmxqv332 <remtest>",
    "claim <Squish> <VTE> https://streamable.com/rmxqv334 <I'm a killa4>",
    "claim <Squish> <Sixth> https://streamable.com/rmxqv334 <I'm a killa4>",
    "changebounty <Adam> <1>",
    "claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>",
    "ledger <DEFYN> <100> https://streamable.com/rmxqv332 <booty>",
    "claim <DEFYN> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>",
    "adduser <cork> <TheCorkster>",
    "addtarget <WhooptieDo> <15>",
    "changebounty <WhooptieDo> <9.22>",
    "claim <cork> <WhooptieDo> https://streamable.com/rmxqv334 <yee>"
]

for ip in testip:
    handler.handle(ip)



# targets.put("Adam",10.0)
# targets.put("Sixth", 9.5)
# targets.put("VTE", 3.0)



# users.put("Squish", "unknown")
# users.put("ssn", "simhendramadhya_")

# handler.handleClaim("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# handler.handleLedger("ledger <Squish> <-4.5> https://streamable.com/rmxqv332 <remtest>")
# handler.handleClaim("claim <Squish> <VTE> https://streamable.com/rmxqv334 <I'm a killa4>")
# handler.handleClaim("claim <Squish> <Sixth> https://streamable.com/rmxqv334 <I'm a killa4>")
# targets.changeBounty("Adam", 1)
# handler.handleClaim("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# users.put("DEFYN", "DEFYN")
# handler.handleClaim("claim <DEFYN> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")
# handler.handleLedger("ledger <DEFYN> <100> https://streamable.com/rmxqv332 <booty>")


# print("-------------------")
# print(targets.getAllTargets())
# print()
# print(users.getAllUsers())
# print()
# entrylist = entries.getAll()
# for ent in entrylist:
#     print(ent)
# print()
# for b in bountyboard.boardToPrint("leaderboard"):
#     print(b)
# print()
# for b in bountyboard.boardToPrint("weeklyboard"):
#     print(b)
# print()
# bountyboard.reset()
# for b in bountyboard.boardToPrint("leaderboard"):
#     print(b)
# print()
# for b in bountyboard.boardToPrint("weeklyboard"):
#     print(b)

table = bountyboard.boardToPrint("leaderboard")[1:]
out = tabulate(table, headers=bountyboard.boardToPrint("leaderboard")[0])
print(type(out))
print(out)