import time
import os
import requests
print("Minecraft files server creator")
print('(right click for paste text from clipboard)')
print("enter server files localization:")
lokalizacja = input("")
os.chdir(lokalizacja)
os.system('cls')
print("WARNING! - You need Java 17 for newer server versions!")
print("1.7.10 - 1.12.2 - 1.17 - 1.19")
print("Enter your verion")
wersja = input("")
if wersja == "1.7.10":
    x = "https://launcher.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar"
    os.system('cls')
if wersja == "1.12.2":
    x = "https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar"
    os.system('cls')
if wersja == "1.17":
    x = "https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar"
    os.system('cls')
if wersja == "1.19":
    x = "https://launcher.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar"
    os.system('cls')


# To save to an absolute path.
print("DOWNLOADING SERVER FILES ... PLEASE WAIT")
r = requests.get(x)  
with open(lokalizacja + '\server.jar' , 'wb') as f:
    f.write(r.content)
os.system('cls')

os.system('server.jar')
time.sleep(2)
os.remove(lokalizacja + '\eula.txt')
eula = ['#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).', '#Sun Nov 20 20:55:53 CET 2022', 'eula=true']
print('Do you agree to minecraft server license and regulations? - https://account.mojang.com/documents/minecraft_eula')
ansewer1 = input("yes or no - ")
if ansewer1 == "yes":
    odp1 = "True"
if ansewer1 == "no":
    odp1 = "False"
if odp1 == "True":
    with open(lokalizacja + '\eula.txt', 'w') as f:
        f.write('\n'.join(eula))
if odp1 == "False":
    os.system('cls')
    print('You need to agree if you want to continue')
    os.system("pause")
    exit()

os.system('cls')

#setting server parameters
print("NOW SET SERVER PROPERTIES:")
ip = input("SERVER IP (set your local ip for playing LAN or port forwarding, or use vpn (recomended Radmin VPN) to play witch your friends.(they need to be in your network - ")
playerslb = input("Server players limit ( recomended 20 or lower) - ")
gamemode = input("server gamemode (in older versions 0,1,3 , in newer creative,survival,spectator - ")
difficulty = input("set server difficulty - ")
commandbl = input("Enable command blocks? True or False - ")
motd = input("set server motd (server description seen in server menu) - ")
seed = input("set your world seed (set empty for default) - ")
onmd = input("online mode (set server olny for premium acc or non-premium acc) True for premium - False - non-premium - ")
resp = input("default resourcepack url - ")

os.remove(lokalizacja + '\server.properties')
lines = ['#Minecraft server properties', '#Sun Nov 20 19:55:55 CET 2022', 'view-distance=10', 'max-build-height=256', 'server-ip=' + ip, 'level-seed=' + seed, 'gamemode=' + gamemode, 'server-port=25565', 'enable-command-block=' + commandbl]
lines2 = ['', 'allow-nether=true', 'enable-rcon=false', 'op-permission-level=4', 'enable-query=false', 'prevent-proxy-connections=false', 'generator-settings=', 'resource-pack=' + resp, 'player-idle-timeout=0', 'level-name=world', 'motd=' + motd, 'force-gamemode=false', 'hardcore=false', 'white-list=false', 'pvp=true', 'spawn-npcs=true', 'generate-structures=true', 'spawn-animals=true', 'snooper-enabled=true', 'difficulty=' + difficulty, 'network-compression-threshold=256', 'level-type=DEFAULT', 'spawn-monsters=true', 'max-tick-time=60000', 'max-players=' + playerslb, 'resource-pack-sha1=', 'online-mode=' + onmd, 'allow-flight=false', 'max-world-size=29999984']
with open(lokalizacja + '\server.properties', 'w') as f:
    f.write('\n'.join(lines))
with open(lokalizacja + '\server.properties', 'a') as f:
    f.write('\n'.join(lines2))

os.system('cls')
print("")
print("")
print("Hurray!")
print("everything is done!")
print("Do you wan't to run server or do you wan't to run this manually?")
tn = input ("Type Automatic or Manual - ")
if tn == "automatic":
    os.system('server.jar')
if tn == "manual":
    print('bye! working witch you was fun!')
    os.system("pause")
if tn == "Automatic":
    os.system('server.jar')
if tn == "Manual":
    print('bye! working witch you was fun!')
    os.system("pause")