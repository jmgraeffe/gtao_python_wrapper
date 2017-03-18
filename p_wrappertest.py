import GTAOrange as API
from OrangeWrapper import player as Player

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %s" % (attr, getattr(obj, attr)))

def onEventStart():
    print("TEST")
    return True

def onPlayerConnect(player, ip):
    print(player)
    print(ip)
    player = Player.getByID(player)
    player.setPosition(78.9911, -1947.52, 21.1741)
    return True
    
def onPlayerCommand(player, command):
    command = command.split()
    player = Player.getByID(player)
    
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
    elif(command[0] == "/createveh"):
        val = API.CreateVehicle(int(command[1]), float(command[2]), float(command[3]), float(command[4]), float(command[5]))
        print(val)
    elif(command[0] == "/deleteveh"):
        val = API.DeleteVehicle(int(command[1]))
        print(val)
    elif(command[0] == "/setvehpos"):
        val = API.SetVehiclePosition(int(command[1]), float(command[2]), float(command[3]), float(command[4]))
        print(val)
    elif(command[0] == "/getvehpos"):
        val = API.GetVehiclePosition(int(command[1]))
        print(val)
    elif(command[0] == "/client"):
        val = API.TriggerClientEvent(int(player), "btn1", ["btn1", False, 200.04, 'hello'])
        print(val)
    else:
        print(' '.join(command))
    return True
    
Player.on("connect", onPlayerConnect)
Player.on("command", onPlayerCommand)

API.TriggerServerEvent("PlayerCommand", [0,"Test"])