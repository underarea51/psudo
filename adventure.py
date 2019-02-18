import time

print("\n" * 200)
print("      >>>>>>>>>>>>>> Welcome Adventure <<<<<<<<<<<<<<\n")
print("\n" * 3)
time.sleep(3)
print("\nA long time ago, a rider strobe forth from the frozen North.")
time.sleep(2)
print("\n")
print("Does this warrior have a name?")
name=input("> ")
print(name, "the barbarian, sword in hand and looking for adventure!")
time.sleep(2)
print("However, evil is lurking nearby...?")
time.sleep(2)
print("Will", name, "prevail, and win great fortune...")
time.sleep(3)
print("\n")
print("Or die by the hands of great evil...?","\n" *4)
time.sleep(4)
print("\n" *3)
print("Only time will tell...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("\n" *200)

print("You find yourself at a small inn. There's little gold inn your purse but your\nsword is sharp, and you're ready for adventure. With you are three other\ncustomers. A ragged looking man, and a pair of dangerous looking guards.")      

def start():
    print("\n--------")
    print("Do you appraoh the...")
    print("1. Ragged looking man")
    print("2. Dangerious looking guards")
          
    cmdlist=["1", "2"]
    cmd=getcmd(cmdlist)
    
    if cmd=="1":
        ragged()
        
    elif cmd=="2":
        guards()
        
def ragged():
    print("/n" * 200)
    print("You walk up to the ragged looking man and greet him. He smiles a toothless grin and, with a strange accent, says \"Buy me a mug of wine, and I shall tell you a tell of great treasure...\"" )
          
    
def guards():
    print("\n" * 200)
    print("You walk up to the dangerious guards and greet them.")
    print("The guards look at their drinks and snarl at you.")
    print('"And says to you, What do you want Barbarian?  One guard reaches for his axe..."')
    time.sleep(2)
    
def getcmd(cmdlist):
    cmd = input(name + ">")
    if cmd in cmdlist:
        return cmd
    elif cmd == "help":
        print("\nEnter your choice as detailed in the game.")
        print("or enter 'quit' to leave the game")
        return getcmd(cmdlist)
    elif cmd == "quit":
        print("\n--------")
        time.sleep(1)
        print("Sadly you return your homeland without fame or fortune...")
        time.sleep(5)
        
if name ==" _ _main_ _ ":
    start()


 
