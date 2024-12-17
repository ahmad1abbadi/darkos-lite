import os
import re
import subprocess
import time
import threading
import shutil
import sys, urllib.request, urllib.error
import tarfile
import socket
import fnmatch

current_version = "0.4"
url = 'https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/currently%20version.txt'
def start_darkos():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("Starting")
    os.system("termux-x11 :0 &>/dev/null &")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
def wine_container():
    os.system("clear")
    photo()
    print("Select Wine container:")
    
    wine_paths = {
        "1": "/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin",
        "2": "/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin",
        "3": "/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"
    }
    
    for key, path in wine_paths.items():
        if os.path.exists(path):
            if key == "1":
                print("1) wine 1")
            if key == "2":
                print("2) wine 2")
            if key == "3":
                print("3) wine 3")
    
    print("Else) Back to the main menu 👑")
    print("")
    
    prefix_path = input("Enter your selection: ")
    
    if prefix_path not in wine_paths.keys():
        print("Incorrect or empty option!")
        time.sleep(1)
        main_menu()
    else:
        conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/os.conf"
        wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/.wine"
        os.system("chmod +x $PREFIX/glibc/bin/box64")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine")
        os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine")
        if not os.path.exists(f"/data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64"):
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/bin/wine64")
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine $PREFIX/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
        else:
            os.system(f"chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64")
            os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wine64 $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineserver $PREFIX/glibc/bin/wineserver")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/wineboot $PREFIX/glibc/bin/wineboot")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/{prefix_path}/wine/bin/winecfg $PREFIX/glibc/bin/winecfg")
        os.system("ln -sf /data/data/com.termux/files/usr/var/lib/dbus/machine-id /etc/machine-id")
        os.environ.pop('LD_PRELOAD', None)
        ### AZ DARK 
        if os.path.exists(conf_path):
            exec(open(conf_path).read())
        if not os.path.exists(wine_prefix):
            print("Creating wine prefix 💫")
            os.system(f'WINEUSERNAME="DARKOS" WINEDLLOVERRIDES="mscoree=disabled" BOX64_FUTEX_WAITV=0 box64 wine64 wineboot &>/sdcard/darkos/darkos-py.log')
            os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
            os.system(f'rm "{wine_prefix}/dosdevices/z:"')
            os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
            os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
            os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
            print("Installing DXVK+Zink...")
            os.system(f'box64 wine "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
            print("Done!")
            os.system("clear") 
            print("prefix done enjoy 🤪 ")
            time.sleep(3)
            os.system("box64 wineserver -k &>/dev/null")
            start_container()
    start_container()
def internet_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=1)
        return True
    except OSError:
        pass
    return False
def remove():
    folder_path = '/data/data/com.termux/files/home'
    for filename in os.listdir(folder_path):
        if fnmatch.fnmatch(filename, '*.tar.xz*'):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f'{filename} has been deleted.')
            
def uninstall_wine_lite():
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/1/wine")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
            shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
    if os.path.exists("/sdcard/darkos"):
        os.system("rm -r /sdcard/darkos")
def install_files():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/AZ-lite.tar.xz")
    os.system("tar -xJf AZ-lite.tar.xz -C $PREFIX/glibc")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/wine-default.tar.xz")
    os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/darkos.tar.xz")
    os.system("tar -xJf darkos.tar.xz -C /sdcard/")
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/update.tar.xz")
    os.system("tar -xJf update.tar.xz")
    os.system("rm $PREFIX/bin/darkos.py")
    os.system("rm $PREFIX/bin/update-darkos.py")
    os.system("rm $PREFIX/bin/run-darkos.py")
    os.system("rm $PREFIX/bin/debug-darkos.py")
    os.system("rm $PREFIX/bin/darkos")
    os.system("wget -O run-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/run-darkos.py")
    os.system("wget -O darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/darkos.py")
    os.system("wget -O darkos https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/darkos")
    os.system("wget -O debug-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/debug-darkos.py")
    os.system("wget -O update-darkos.py https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/update-darkos.py")
    os.system("chmod +x darkos")
    os.system("mv update-darkos.py darkos.py run-darkos.py debug-darkos.py darkos $PREFIX/bin/")
    remove()
    print("")
    print("DARKOS-lite files repaired successfully")
def photo():
    os.system("python3 $PREFIX/bin/photo.py")
def check_network_connection():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True
    except urllib.error.URLError:
        return False
def main():
    if not check_network_connection():
        print("No network connection available.")
        return
    try:
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        if latest_version < current_version:
            os.system("curl -o install https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/installO.sh && chmod +x install && ./install")
        if latest_version > current_version:
            print("update available....please update DARKOS")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("🙅‍♂️🛜", e)
        else:
            print("something went wrong please send this error to developer")
def winetricks():
    os.system("clear")
    photo()
    print(" winetricks menu : ")
    print("")
    print(" 1) winetricks gui 🖥️")
    print("")
    print(" 2) winetricks verbs 🧑‍💻")
    print("")
    print(" Else) Back to the main menu 👑")
    print("")
    choise = input()
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/os.conf"
    if choise != "1" and choise != "2":
        print("backing to main menu")
        time.sleep(2)
        main_menu()
    elif choise == "1":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        exec(open('/sdcard/darkos/VKD3D.conf').read())
        os.system("clear")
        photo()
        print("loading...... winetrick")
        print("winetricks working just wait its take 1 minute to launch menu if you want to close it and back to main menu press control+C")
        os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
        os.system("LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/opt/box64_bash $PREFIX/bin/winetricks &>/dev/null")
        main_menu()
    elif choise == "2":
        exec(open(conf_path).read())
        exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
        exec(open('/sdcard/darkos/darkos_custom.conf').read())
        exec(open('/sdcard/darkos/VKD3D.conf').read())
        os.system("clear")
        photo()
        print("winetrick verbs ready to use on chosen container. Select the desired one:")
        print("")
        print("1) apps")
        print("2) benchmarks")
        print("3) dlls")
        print("4) fonts")
        print("5) settings")
        print("Select verb:")
        winetricks_verb = input()
        while not 1 <= float(winetricks_verb) <= 5:
            print("Invalid option. Retry:")
            print("")
            print("1) apps")
            print("2) benchmarks")
            print("3) dlls")
            print("4) fonts")
            print("5) settings")
            print("Select verb:")
            winetricks_verb = input()
            pass
        if winetricks_verb == "1":
            winetricks_verb = "apps"
        elif winetricks_verb == "2":
            winetricks_verb = "benchmarks"
        elif winetricks_verb == "3":
            winetricks_verb = "dlls"
        elif winetricks_verb == "4":
            winetricks_verb = "fonts"
        else:
            winetricks_verb = "settings"
        os.system("clear")
        print("Enter package (enter 0 to go back, 1 to print all available packages):")
        winetricks_package = input()
        if winetricks_package == "1":
            print("Available packages/options:")
            print("")
            os.system(f"BOX64_LOG=0 LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/opt/box64_bash $PREFIX/bin/winetricks {winetricks_verb} list 2>/dev/null | grep -v 'Box64 with Dynarec'")
            print("Select package (enter 0 to go back):")
            winetricks_package = input()
            if winetricks_package == "0":
                print("backing to main menu")
                time.sleep(2)
                main_menu()
        elif winetricks_package == "0":
            print("backing to main menu")
            time.sleep(2)
            main_menu()
        os.system(f"BOX64_LOG=0 LD_PRELOAD= WINESERVER=$PREFIX/glibc/bin/wineserver WINE=$PREFIX/glibc/bin/wine64 $PREFIX/glibc/bin/box64 $PREFIX/glibc/opt/box64_bash $PREFIX/bin/winetricks {winetricks_verb} {winetricks_package} 2>/dev/null | grep -v 'Box64 with Dynarec'")
        print("")
        print("winetrick packages installed successfully...👍 ")
        print("backing to main menu..... 🔁")
        time.sleep(4)
        main_menu()
def start_container():
    start_darkos()
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    xrandr_output = os.popen('xrandr').read()
    current_resolution_match = re.search(r'current\s+(\d+) x (\d+)', xrandr_output)

    if current_resolution_match:
        current_resolution = f"{current_resolution_match.group(1)}x{current_resolution_match.group(2)}"
    else:
        current_resolution = "800x600"
    res = current_resolution
    os.system("taskset -c 4-7 box64 wine64 explorer /desktop=shell," + res + " $PREFIX/glibc/opt/apps/run.exe &>/dev/null &")
    os.system("am start -n com.termux.x11/com.termux.x11.MainActivity &>/dev/null")
    os.system("clear")
    os.system("python3 $PREFIX/bin/photo.py")
    print("exit 1️⃣")
    user_input = input("Enter 1 to stop: ")
    if user_input == "1":
        os.system("box64 wineserver -k")
        print("Exiting 👋")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        print("see you later")
        main_menu()
    main_menu()
        
def uninstall_wine():
    os.system("clear")
    photo()
    print("Are you sure you want to delete the wine version?")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print("1) Delete wine 1")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print("2) Delete wine 2")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print("3) Delete wine 3")
    print(" else) main menu ⬅️")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3":
        print("Incorrect or empty option!")
        main_menu()
    elif choice == "1" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/wine/bin"):
        print("Deleting wine 1, please wait")
        print("")
        uninstall_wine9()
    elif choice == "2" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/wine/bin"):
        print("Deleting wine 2, please wait")
        print("")
        uninstall_wine8()
    elif choice == "3" and os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        print("Deleting wine 3, please wait")
        print("")
        uninstall_wine7()
    main_menu()
def uninstall_wine9():
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin"):
        os.system("rm -r /data/data/com.termux/files/usr/glibc/opt/wine/1/wine")
        if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
            shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
def recreate_prefix_wineAZ():
    print("select version of wine you want to recreate prefix:")
    print("")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"):
        print(" 1) remove prefix on container 1")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine"):
        print(" 2) remove prefix on container 2 ")
    if os.path.exists("/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine"):
        print(" 3) remove prefix on container 3")
    print("")
    print(" else) back to settings menu")
    print("")
    user_input = input()
    os.system(f'rsync -a /data/data/com.termux/files/usr/glibc/opt/wine/{user_input}/.wine/drive_c/users/* /sdcard/darkos-savegames/users/ &>/dev/null')
    if user_input not in ["1", "2", "3"]:
        change_setting()
    elif user_input == "1":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine')
         print(f'done')
    elif user_input == "2":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/2/.wine')
         print(f'done')
    elif user_input == "3":
         shutil.rmtree('/data/data/com.termux/files/usr/glibc/opt/wine/3/.wine')
         print(f'done')
    main_menu()
def check_config_wine():
    config_folder = "/sdcard/darkos"
    exec(open('/sdcard/darkos/darkos_dynarec.conf').read())
def install_wine9(): 
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/wine-default.tar.xz")
    os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
    os.remove("wine-default.tar.xz")
def auto_start():
    os.system("clear")
    photo()
    print(" select what you refer:")
    print("")
    print(" 1) turn-on auto start os 👍")
    print("")
    print(" 2) turn-off auto start os 👎")
    print("")
    print( "else) back to settings menu")
    choice = input()
    if choice != "1" and choice != "2":
        change_setting()
    elif choice == "1":
        command = "darkos"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                for line in f:
                    if command in line:
                        command_exists = True
                        print(" auto start os already activated... ")
                        time.sleep(2)
                        change_setting()
        if not command_exists:
            with open(bashrc_path, 'a') as f:
                f.write(command + '\n')
            print(" auto start os activated successfully")
            time.sleep(2)
            change_setting()
    elif choice == "2":
        command = "darkos"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                lines = f.readlines()
            with open(bashrc_path, 'w') as f:
                for line in lines:
                    if command not in line:
                        f.write(line)
            print("Auto start os deactivated successfully")
            time.sleep(2)
            change_setting()
def autoclean_ram():
    os.system("clear")
    photo()
    print(" select what you refer:")
    print("")
    print(" 1) turn-on autoclean ram 👍")
    print("")
    print(" 2) turn-off autoclean ram 👎")
    print("")
    print( "else) back to settings menu")
    choice = input()
    if choice != "1" and choice != "2":
        change_setting()
    elif choice == "1":
        command = "</dev/zero head -c 4000m | pv | tail &>/dev/null \n"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                for line in f:
                    if command in line:
                        command_exists = True
                        print(" autoclean ram already activated... ")
                        time.sleep(2)
                        change_setting()
        if not command_exists:
            with open(bashrc_path, 'r') as f:
                lines = f.readlines()
            with open(bashrc_path, 'w') as f:
                f.write(command)
                for line in lines:
                    f.write(line)
            print(" autoclean ram activated successfully! Changes will be applied on the next boot")
            time.sleep(2)
            change_setting()
    elif choice == "2":
        command = "</dev/zero head -c 4000m | pv | tail &>/dev/null"
        bashrc_path = os.path.expanduser('~/.bashrc')
        command_exists = False
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                lines = f.readlines()
            with open(bashrc_path, 'w') as f:
                for line in lines:
                    if command not in line:
                        f.write(line)
            print("Autoclean ram deactivated successfully! Changes will be applied on the next boot")
            time.sleep(2)
            change_setting()
def change_setting():
    os.system("clear")
    photo()
    print("settings ⚙️")
    print("1) Update OS 👑")
    print("2) Repair DARKOS-lite files 🔧")
    print("3) winetricks ⛑️")
    print("4) Delete prefix 🪡")
    print("5) Change auto start setting 🖱️")
    print("6) Debug mode 🐞") 
    print("7) Boost cpu 🔥 (Root no longer needed!)")
    print("8) Autoclean RAM 🔥 (clean RAM on every DarkOS launch. EXPERIMENTAL)")
    print("9) Move Games to Termux Internal Filesystem")
    print("10) Build Box64")
    print("11) Enable external storage")
    
    print("else) Back 🔙")
    print("")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9" and choice != "10" and choice != "11":
        print("...........")
        main_menu()
    elif choice == "11":
      os.system("rm -rf $PREFIX/glibc/opt/wine/1/.wine/dosdevices/f: &>/dev/null")
      os.system("rm -rf $PREFIX/glibc/opt/wine/2/.wine/dosdevices/f: &>/dev/null")
      os.system("rm -rf $PREFIX/glibc/opt/wine/3/.wine/dosdevices/f: &>/dev/null")
      os.system("df | grep 'storage' | grep -v 'emulated' | awk '{print $NF}'")
      os.system(f"ln -sf $(df | grep 'storage' | grep -v 'emulated' | awk '{{print $NF}}' &>/dev/null) $PREFIX/glibc/opt/wine/1/.wine/dosdevices/f:")
      os.system(f"ln -sf $(df | grep 'storage' | grep -v 'emulated' | awk '{{print $NF}}' &>/dev/null) $PREFIX/glibc/opt/wine/2/.wine/dosdevices/f:")
      os.system(f"ln -sf $(df | grep 'storage' | grep -v 'emulated' | awk '{{print $NF}}' &>/dev/null) $PREFIX/glibc/opt/wine/3/.wine/dosdevices/f:")
      print("Now the external storage showld be connected to Drive F on DarkOS. Check with explorer! ")
      time.sleep(3)
      change_setting()
    elif choice == "2":
      print(" Do you really want to repair emu files ? This will delete all your files inside the drive C in container 1")
      print(" yes = y")
      print(" no = n")
      stop = input()
      if stop != "y" and choice != "n":
          print("wrong choice backing to main menu")
          time.sleep(1)
          change_setting()
      elif stop == "y":
          if internet_connected():
               uninstall_wine_lite()
               time.sleep(1)
               install_files()
               print("done....")
               time.sleep(1)
               change_setting()
          else:
               print("No internet connection available. Aborting operation.")
               time.sleep(2)
               change_setting()
      elif stop == "n":
          change_setting()

    elif choice == "1":
        print("")
        print("Shutdown OS....")
        print("")
        print("checking 🔎.....")
        time.sleep(1)
        response = urllib.request.urlopen(url)
        latest_version = response.read().decode('utf-8').strip()
        try:
            if latest_version > current_version:
                print("update available..... updating......📥")
                os.system("python3 $PREFIX/bin/update-darkos.py")
                time.sleep(3)
                change_setting()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                os.system("clear")
                print("no internet connection 😵 backing to the settings")
                time.sleep(3)
                change_setting()
        else:
            print("no update available ")
            time.sleep(3)
            change_setting()
    elif choice == "6":
        os.system("python3 $PREFIX/bin/debug-darkos.py")
    elif choice == "4":
        recreate_prefix_wineAZ()
    elif choice == "5":
        auto_start()
    elif choice == "8":
        autoclean_ram()
    elif choice == "9":
        move_games()
    elif choice == "3":
        winetricks()
    elif choice == "10":
        build_box64()
    elif choice == "7":
        os.system("clear")
        photo()
        print(" select what you refer:")
        print("")
        print(" 1) turn-on CPU BOOST 👍")
        print("")
        print(" 2) turn-off CPU BOOST 👎")
        print("")
        print( "else) back to settings menu")
        choice = input()
        if choice != "1" and choice != "2":
            change_setting()
        elif choice == "1":
            reload()
            print("installing python packages")
            os.system('pkg install python vulkan-tools python-pip coreutils -y &> /dev/null')
            print("")
            os.system('pip install aiofiles psutil blessings &> /dev/null')
            print("python packages.... 100%")
            command = "am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
            -a com.termux.RUN_COMMAND \
            --es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/python' \
            --esa com.termux.RUN_COMMAND_ARGUMENTS '/data/data/com.termux/files/usr/bin/cpu_boost.py' \
            --es com.termux.RUN_COMMAND_WORKDIR '/data/data/com.termux/files/home' \
            --ez com.termux.RUN_COMMAND_BACKGROUND 'false' \
            --es com.termux.RUN_COMMAND_SESSION_ACTION '1' &> /dev/null \n"
            bashrc_path = os.path.expanduser('~/.bashrc')
            command_exists = False
            if os.path.exists(bashrc_path):
                with open(bashrc_path, 'r') as f:
                    for line in f:
                        if command in line:
                            command_exists = True
                            print(" CPU BOOST already activated... ")
                            time.sleep(2)
                            change_setting()
            if not command_exists:
                with open(bashrc_path, 'r') as f:
                    lines = f.readlines()
                with open(bashrc_path, 'w') as f:
                    f.write(command)
                    for line in lines:
                        f.write(line)
                print(" CPU BOOSTER activated successfully! Changes will be applied on the next boot...")
                time.sleep(2)
                change_setting()
        elif choice == "2":
            command = "am startservice --user 0 -n com.termux/com.termux.app.RunCommandService \
            -a com.termux.RUN_COMMAND \
            --es com.termux.RUN_COMMAND_PATH '/data/data/com.termux/files/usr/bin/python' \
            --esa com.termux.RUN_COMMAND_ARGUMENTS '/data/data/com.termux/files/usr/bin/cpu_boost.py' \
            --es com.termux.RUN_COMMAND_WORKDIR '/data/data/com.termux/files/home' \
            --ez com.termux.RUN_COMMAND_BACKGROUND 'false' \
            --es com.termux.RUN_COMMAND_SESSION_ACTION '1' &> /dev/null "
            bashrc_path = os.path.expanduser('~/.bashrc')
            command_exists = False
            if os.path.exists(bashrc_path):
                with open(bashrc_path, 'r') as f:
                    lines = f.readlines()
                with open(bashrc_path, 'w') as f:
                    for line in lines:
                        if command not in line:
                            f.write(line)
                print("CPU BOOSTER deactivated successfully! Changes will be applied on the next boot...")
                time.sleep(2)
                change_setting()
def build_box64():
    print("")
    print("This will build an updated Box64 bin from ptitSeb github source")
    print("adding some new features that still not in the main builds available on TDB")
    print("THESE ARE NOT TESTED. So expect incompatibilities")
    print("")
    print("Select your desired option: ")
    print("1) Build Box64")
    print("2) Build Box64 with Box32 support (EXPERIMENTAL)")
    print("else) Back to main menu")
    print("")
    choice = input()
    if choice != "1" and choice != "2":
        change_setting()
    elif choice == "1":
        box32 = "0"
    elif choice == "2":
        box32 = "1"
    print("")
    print("Select wich version of Box64 will build: ")
    print("1) Build Box64 for SD845")
    print("2) Build Box64 for SD888")
    print("3) Build Box64 for SD8G2")
    print("else) Back to main menu")
    print("")
    sdchoice = input()
    if sdchoice != "1" and sdchoice != "2" and sdchoice != "3":
        change_setting()
    elif sdchoice == "1":
        sdver = "SD845"
    elif sdchoice == "2":
        sdver = "SD888"
    elif sdchoice == "3":
        sdver = "SD8G2"
    print("")
    print("Select your desired option: ")
    print("1) Activate BAD_SIGNAL")
    print("2) Deactivate BAD_SIGNAL")
    print("else) Back to main menu")
    print("")
    bschoice = input()
    if bschoice != "1" and bschoice != "2":
        change_setting()
    elif bschoice == "1":
        badsignal = "ON"
    elif bschoice == "2":
        badsignal = "OFF"
    print("")
    os.system("clear")
    os.system("apt install cmake-glibc make-glibc python-glibc -y")
    os.system("pkg install -y git")
    os.system("rm -rf ~/box64")
    os.system(rf"unset LD_PRELOAD; export GLIBC_PREFIX=$PREFIX/glibc; export PATH=$GLIBC_PREFIX/bin:$PATH; cd ~/; git clone https://github.com/ptitSeb/box64; cd ~/box64; sed -i 's/\/usr/\/data\/data\/com.termux\/files\/usr\/glibc/g' CMakeLists.txt; sed -i 's/\/etc/\/data\/data\/com.termux\/files\/usr\/glibc\/etc/g' CMakeLists.txt; mkdir build; cd build; cmake --install-prefix $PREFIX/glibc .. -DARM_DYNAREC=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBAD_SIGNAL={badsignal} -D{sdver}=ON -DBOX32={box32}; make -j8; make install")
    os.system("rm -rf ~/box64")
    change_setting()
def move_games():
    print("")
    print("This will move your games to Drive G, erasing them from their original path.")
    print("This way, some games will increase performance.")
    print("But remember to restore your games if you'll uninstall DarkOS Lite")
    print("Otherwise, you'll lose your games!")
    print("You need to have enough free space to keep 2 copies of the heaviest gamefile to be moved.")
    print("Otherwise, the proccess will fail.")
    print("")
    print("Select your desired option: ")
    print("1) Move games to Drive G")
    print("2) Restore games to the original path")
    print("else) Back to main menu")
    print("")
    choice = input()
    if choice != "1" and choice != "2":
        change_setting()
    elif choice == "1":
        os.system(f"file-selector")
        change_setting()
    elif choice == "2":
        os.system("rsync -r --info=progress2 --remove-source-files $PREFIX/glibc/opt/G_drive/* \"$GAMES_PATH\"")
        change_setting()
def reload():
    file_path = os.path.expanduser("~/.termux/termux.properties")
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith("# allow-external-apps = true"):
                line = line.replace("# ", "")
            file.write(line)
            #print(f"File updated: {file_path}")
    os.system("termux-reload-settings")
def main_menu():
    os.system("clear")
    photo()
    print("welcome to darkos-lite safe mode")
    print("")
    print("Select what you need to do:")
    print("1) START DARK OS lite IN SAFE MODE 🚑")
    print("2) SETTINGS ⚙️")
    print("3) EXIT SAFE MODE 🚪")
    print("4) KILL DARK OS lite AND EXIT TO TERMINAL 😭")
    print("")
    main()
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("wrong")
        main_menu()
    elif choice == "1":
        wine_container()
    elif choice == "2":
        change_setting()
    elif choice == "3":
        print("")
        os.system("clear")
        photo()
        print("")
        print(" Restarting.....")
        time.sleep(1)
        print("")
        subprocess.run(["bash", "darkos"])
    elif choice == "4":
        print("")
        os.system("clear")
        photo()
        print("")
        print("good bye 😭")
        os.system('pkill -f "app_process / com.termux.x11"')
        os.system('pkill -f pulseaudio')
        os._exit(0)
start_darkos()
main_menu()
