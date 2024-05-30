import os,sys,string,random,time
from os import system as dick
def clear():
	dick('clear')
	print(logo)
class boobs:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.11)
logo= ("""
<|> ITS A SIMPLE ACOUNT DUMPER TOOL <|>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

line= '\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
filex=str(input("\033[1;91mENTER A FILE NAME : "))
f=filex.upper()

def dump():
    clear()
    print('\033[1;97mEXAMPLE \033[1;91m: \033[1;97mminhaj, mahmud, xaiver,\033[1;97m')
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    first = input('\033[1;97mENTER FIRST NAME : ')
    print(line)
    print('\033[1;97mEXAMPLE \033[1;91m: \033[1;97mahmed, islam, ali, khan \033[1;97m')
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    last = input('\033[1;97mENTER LAST NAME : ')
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;97mEXAMPLE \033[1;91m: @gmail.com,@yahoo.com etc ;)')
    domain = input('\033[1;97mENTER DOMAIN : ')
    print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    try:
            limit=int(input('\033[1;97mCHOOSE AMOUNT : '))
    except ValueError:
            limit = 5000
   
    boobs('\033[1;93mACOUNT DUMPING..\033[1;37m')
    
    lists = ['3','4']
    for xd in range(limit):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                    mail = ''.join(random.choice(string.digits) for _ in range(3))
                    open(f'.{f}','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                    mail = ''.join(random.choice(string.digits) for _ in range(4))
                    open(f'.{f}','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open(f'.{f}', 'r').read().splitlines()
    print('ACCOUNTS SAVED ON YOUR FILE NAME ')
            

dump()