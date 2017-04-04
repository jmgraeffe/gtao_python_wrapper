from threading import Thread

import __orange__ as API
import GTAOrange.player as Player
import GTAOrange.vehicle as Vehicle
import GTAOrange.blip as Blip
import GTAOrange.text as Text
import GTAOrange.marker as Marker
import GTAOrange.object as Object


def _sendPlayerList(target):
    players = Player.getAll()
    target.chatMsg("Players:")

    for key, player in players.items():
        target.chatMsg(player.getName())


def _threadTest():
    print("Sleeping...")

    i = 0

    while True:

        print(i)
        i += 1

    print("Woke up!")


def onEventStart(bla, bli):
    print(bla)
    print(bli)
    return True


def onPlayerConnect(player, ip):
    print('Player:connect | ' + str(player.getName()) + ' | ' + ip)

    player.setPosition(100.0, -1940.0, 21.0)

    # own attributes
    player.testveh = None
    player.testblip = None

    # trying player-local events
    player.on("leftvehicle", onPlayerLeftVehicle)

    return True


def onPlayerDisconnect(player, reason):
    print('Player:disconnect | ' + str(player) + ' | ' + str(reason))


def onPlayerCommand(player, command):
    # print('Player:command | ' + str(player.getID()) + ' | ' + command)

    command = command.split()

    # player commands

    if(command[0] == "/setpos"):
        player.setPosition(float(command[1]), float(
            command[2]), float(command[3]))
    elif(command[0] == "/players"):
        _sendPlayerList(player)
    elif(command[0] == "/getpos"):
        x, y, z = player.getPosition()
        player.chatMsg("{:.9f}".format(x) + "|" +
                       "{:.9f}".format(y) + "|" + "{:.9f}".format(z))
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
        API.CreateBlipForAll("0|0|0", 0.0, 0.0, 70.0, 1.0, 17, 11)
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

    # thread tests
    elif command[0] == "/thread":
        t = Thread(target=_threadTest)
        t.daemon = True
        t.start()

    # vehicle commands
    elif command[0] == "/veh":
        if command[1] == "create":
            if player.testveh is None:
                x, y, z = player.getPosition()
                player.testveh = Vehicle.create(
                    "Burrito", x, y, z, player.getHeading())
                player.chatMsg("Created a Burrito! :-) | ID: " +
                               str(player.testveh.id))
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

    # blip commands
    elif command[0] == "/blip":
        if command[1] == "create":
            if player.testveh is None:
                x, y, z = player.getPosition()
                player.testblip = Blip.create("TADAAAA", x, y, 90)
                player.chatMsg("Created a fancy blip! :-) | ID: " +
                               str(player.testblip.id))
            else:
                player.chatMsg("Please delete your car before!")
        elif command[1] == "delete":
            if player.testblip is not None:
                player.testblip.delete()
                player.testblip = None
            else:
                player.chatMsg("Please create a blip before!")
        elif command[1] == "getpos":
            if player.testblip is not None:
                #x, y, z = player.testveh.getPosition()
                #player.chatMsg("{:.9f}".format(x) + "|" + "{:.9f}".format(y) + "|" + "{:.9f}".format(z))
                val = player.testblip.getPosition()
                print(val)
            else:
                player.chatMsg("Please create a car before!")
        elif command[1] == "setpos":
            pass

    # 3dtext commands
    elif command[0] == "/3dtext":
        if command[1] == "create":
            x, y, z = player.getPosition()
            text = Text.create("Test", x, y, z)
            player.chatMsg(
                "Created a fancy 3d text! :-) | ID: " + str(text.id))
        elif command[1] == "delete":
            text = Text.getByID(int(command[2]))
            if text is not False:
                text.delete()
        elif command[1] == "getpos":
            text = Text.getByID(int(command[2]))
            if text is not False:
                val = text.getPosition()
                print(val)
        elif command[1] == "setpos":
            pass

    # marker commands
    elif command[0] == "/marker":
        if command[1] == "create":
            x, y, z = player.getPosition()
            marker = Marker.create(x, y, z)
            marker.on("playerentered", onPlayerEnteredMarker)
            player.chatMsg("Created a fancy marker! :-) | ID: " +
                           str(marker.id))
        elif command[1] == "delete":
            marker = Marker.getByID(int(command[2]))
            if marker is not False:
                marker.delete()
        elif command[1] == "getpos":
            marker = Marker.getByID(int(command[2]))
            if marker is not False:
                val = marker.getPosition()
                print(val)
        elif command[1] == "setpos":
            pass

    # object commands
    elif command[0] == "/object":
        if command[1] == "create":
            x, y, z = player.getPosition()
            obj = Object.create(1204839864, x, y, z, 1.0, 1.0, 1.0)
            player.chatMsg("Created a fancy object! :-) | ID: " + str(obj.id))
        elif command[1] == "delete":
            obj = Object.getByID(int(command[2]))
            if obj is not False:
                obj.delete()

    else:
        print(' '.join(command))
    return True


def onPlayerEnteredVehicle(player, veh):
    print('Vehicle:playerentered | ' +
          str(player.getID()) + ' | ' + str(veh.getID()))


def onPlayerLeftVehicle(player, veh):
    print('Vehicle:playerleft | ' + str(player.getID()) + ' | ' + str(veh.getID()))


def onPlayerEnteredMarker(marker, player):
    x, y, z = marker.getPosition()
    player.setPosition(x, y, z + 5)

Player.on("connect", onPlayerConnect)
Player.on("command", onPlayerCommand)

Vehicle.on("playerentered", onPlayerEnteredVehicle)
#API.TriggerServerEvent("PlayerCommand", [0,"Test"])
