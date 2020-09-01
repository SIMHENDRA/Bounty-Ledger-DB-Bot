import DB_init
from operations import targets
from operations import entryTypes
from operations import users
from operations import bountyboard
from operations import entries
import handler
import os
dbpath = 'C:\\Users\\Shyam\\Documents\\GitHub\\Bounty-Ledger-DB-Bot\\data\\ledger.db'

if input("This will clear current DB. Continue?") != 'Y':
    quit()
if os.path.exists("data/ledger.db"):
    os.remove("data/ledger.db")
if os.path.exists("ledger.db"):
    os.remove("ledger.db")

DB_init.initDB()

targets.put("Adam",10.0)
targets.put("Sixth", 9.5)
targets.put("VTE", 3.0)

entryTypes.put("claim")
entryTypes.put("ledger")

users.put("Squish", "unknown")
users.put("ssn", "simhendramadhya_")

handler.handleClaim("claim <Squish> <Adam> https://streamable.com/rmxqv334 <I'm a killa4>")


print("-------------------")
print(targets.getAllTargets())
print()
print(users.getAllUsers())
print()
print(bountyboard.getAll())
