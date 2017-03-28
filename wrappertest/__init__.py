import GTAOrange as API
from OrangeWrapper import player as Player
from OrangeWrapper import vehicle as Vehicle

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %s" % (attr, getattr(obj, attr)))

def onEventStart(bla, bli):
    print(bla)
    print(bli)
    return True

def onPlayerConnect(player, ip):
    print('Player:connect | ' + str(player.getName()) + ' | ' + ip)
    
    player.setPosition(78.9911, -1947.52, 21.1741)
    
    # own attributes
    player.testveh = None
    
    return True
    
def onPlayerDisconnect(player, reason):
    print('Player:disconnect | ' + str(player) + ' | ' + str(reason))
    
def onPlayerCommand(player, command):
    print('Player:command | ' + str(player.getID()) + ' | ' + command)

    command = command.split()
    
    # player commands
    
    if(command[0] == "/setpos"):
        player.setPosition(float(command[1]), float(command[2]), float(command[3]))
    elif(command[0] == "/getpos"):
        x, y, z = player.getPosition()
        player.chatMsg("{:.9f}".format(x) + "|" + "{:.9f}".format(y) + "|" + "{:.9f}".format(z))
        cords = player.getPosition()
        print(cords)
    elif(command[0] == "/sethead"):
        player.setHeading(float(command[1]))
    elif(command[0] == "/gethead"):
        player.chatMsg(str(player.chatMsg(player.getHeading())))
    elif(command[0] == "/removeweapons"):
        player.removeWeapons()
    elif(command[0] == "/giveweapon"):
        player.giveWeapon(int(command[1]), int(command[2]))
    elif(command[0] == "/giveammo"):
        pass
    elif(command[0] == "/givemoney"):
        player.giveMoney(int(command[1]))
    elif(command[0] == "/setmoney"):
        player.setMoney(int(command[1]))
    elif(command[0] == "/resetmoney"):
        player.resetMoney()
    elif(command[0] == "/getmoney"):
        player.chatMsg(str(player.getMoney()))
    elif(command[0] == "/setmodel"):
        player.setModel(int(command[1]))
    elif(command[0] == "/getmodel"):
        player.chatMsg(str(player.getModel()))
    elif(command[0] == "/setname"):
        player.setName(command[1])
    elif(command[0] == "/getname"):
        player.chatMsg(player.getName())
    elif(command[0] == "/sethealth"):
        player.setHealth(float(command[1]))
    elif(command[0] == "/gethealth"):
        player.chatMsg(str(player.getHealth()))
    elif(command[0] == "/setarmour"):
        player.setArmour(float(command[1]))
    elif(command[0] == "/getarmour"):
        player.chatMsg(str(player.getArmour()))
    elif(command[0] == "/playerblip"):
        player.attachBlip(player.getName() + "'s super special blip", 2)
    elif(command[0] == "/nullblip"):
        player.createBlip("0|0|0", 0, 0, 0, 3)
    elif(command[0] == "/setcolor"):
        val = API.SetPlayerColor(player, int(command[1]))
        print(val)
    elif(command[0] == "/getcolor"):
        val = API.GetPlayerColor(player)
        print(val)
    elif(command[0] == "/broadcast"):
        player.broadcast(command[1], int(command[2]))
    elif(command[0] == "/sendmessage"):
        player.chatMsg(command[1])
    elif(command[0] == "/disablehud"):
        if command[1] == 1:
            player.disableHUD()
        else:
            player.enableHUD()
            
    # vehicle commands    
    elif(command[0] == "/veh"):
        if command[1] == "create":
            if player.testveh is None:
                x, y, z = player.getPosition()
                player.testveh = Vehicle.create("Burrito", x, y, z, player.getHeading())
                player.chatMsg("Created a Burrito! :-) | ID: " + str(player.testveh.id))
            else:
                player.chatMsg("Please delete your car before!")
        elif command[1] == "delete":
            if player.testveh is not None:
                player.testveh.delete()
                player.testveh = None
            else:
                player.chatMsg("Please create a car before!")
        elif command[1] == "getpos":
            if player.testveh is not None:
                #x, y, z = player.testveh.getPosition()
                #player.chatMsg("{:.9f}".format(x) + "|" + "{:.9f}".format(y) + "|" + "{:.9f}".format(z))
                val = player.testveh.getPosition()
                print(val)
            else:
                player.chatMsg("Please create a car before!")
        elif command[1] == "setpos":
            pass

    else:
        print(' '.join(command))
    return True

def onPlayerEnteredVehicle(p0, p1):
    print('Vehicle:playerentered | ' + str(p0) + ' | ' + str(p1))

def onPlayerLeftVehicle(p0, p1):
    print('Vehicle:playerleft | ' + str(p0) + ' | ' + str(p1))

Player.on("connect", onPlayerConnect)
Player.on("command", onPlayerCommand)

Vehicle.on("playerentered", onPlayerEnteredVehicle)
Vehicle.on("playerleft", onPlayerLeftVehicle)

API.TriggerServerEvent("PlayerCommand", [0,"Test"])