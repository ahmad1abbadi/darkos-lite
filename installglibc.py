import os, shutil, time, subprocess
def start_darkos():
    os.system("clear")
    if "LD_PRELOAD" in os.environ:
        del os.environ["LD_PRELOAD"]
    print("Starting")
    os.system("termux-x11 :0 &>/dev/null &")
    os.system('pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1 &>/dev/null')
    
def termux_pkg():
    print("This takes a few minutes it depends on your internet connection")
    os.system("pkg install glibc-repo x11-repo -y &>/dev/null")
    print("glibc-repo + x11-repo installed")
    os.system("pkg install rsync pulseaudio xkeyboard-config freetype fontconfig termux-x11-nightly termux-am which bash curl sed cabextract -y --no-install-recommends &>/dev/null")
    print("pulseaudio + termux-am +........... installed successfully ")
    os.system("pkg install wget libpng xorg-xrandr mesa -y --no-install-recommends &>/dev/null")
    print("wget+mesa........ installed successfully")
    os.system("apt install tur-repo &>/dev/null")
    os.system("apt install virglrenderer-android virglrenderer-mesa-zink -y &>/dev/null")
    print("vrigl server...... installed successfully")
    os.system("apt upgrade mangohud-glibc -y &>/dev/null")
    print("mangohud...... updated successfully")
    print("")
def install_glibc_AZ():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/glibc-darkos-lite.tar.xz")
    os.system("tar -xJf glibc-darkos-lite.tar.xz -C $PREFIX/")
def update():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/update.tar.xz")
    os.system("tar -xJf update.tar.xz")
    os.remove("update.tar.xz")
def mangohud():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/mangohud.tar.xz")
    os.system("tar -xJvf mangohud.tar.xz -C $PREFIX/glibc &>/dev/null")
    os.remove("mangohud.tar.xz")
def install_AZ():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/AZ-lite.tar.xz")
    os.system("tar -xJf AZ-lite.tar.xz -C $PREFIX/glibc/")
    os.remove("AZ-lite.tar.xz")
def install_box():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/box.tar.xz")
    os.system("tar -xJf box.tar.xz -C $PREFIX/glibc/bin")
    os.remove("box.tar.xz")
def install_conf():
    folder_path = "/sdcard/darkos"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/darkos.tar.xz")
    os.system("tar -xJf darkos.tar.xz -C /sdcard/")
    os.remove("darkos.tar.xz")
def edit_bashrc():
    command = "darkos"
    bashrc_path = os.path.expanduser('~/.bashrc')
    command_exists = False
    if os.path.exists(bashrc_path):
        with open(bashrc_path, 'r') as f:
            for line in f:
                if command in line:
                    command_exists = True
                    print("Welcome back again ☺️ ")
                    break
        if not command_exists:
            with open(bashrc_path, 'a') as f:
                f.write(command + '\n')
            print(" 📝")
    else:
        with open(bashrc_path, 'w') as f:
            f.write(command + '\n')
        print(" 📝")
def create_prefix():
    conf_path = f"/data/data/com.termux/files/usr/glibc/opt/wine/1/os.conf"
    wine_prefix = f"/data/data/com.termux/files/usr/glibc/opt/wine/1/.wine"
    if not os.path.exists(f"/data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64"):
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine $PREFIX/glibc/bin/wine64")
        os.system(f"ln -sf /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine $PREFIX/glibc/opt/wine/1/wine/bin/wine64")
    os.system("ln -s $PREFIX/glibc/opt/wine/1/wine/bin/wine $PREFIX/glibc/bin/wine &>/dev/null")
    os.system("ln -s $PREFIX/glibc/opt/wine/1/wine/bin/wine64 $PREFIX/glibc/bin/wine64 &>/dev/null")
    os.system("ln -s $PREFIX/glibc/opt/wine/1/wine/bin/wineserver $PREFIX/glibc/bin/wineserver &>/dev/null")
    os.system("ln -s $PREFIX/glibc/opt/wine/1/wine/bin/wineboot $PREFIX/glibc/bin/wineboot &>/dev/null")
    os.system("ln -s $PREFIX/glibc/opt/wine/1/wine/bin/winecfg $PREFIX/glibc/bin/winecfg &>/dev/null")
    os.system("chmod +x $PREFIX/glibc/bin/box64")
    os.system("chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine")
    os.system("chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wine64")
    os.system("chmod +x /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/bin/wineserver")
    exec(open(conf_path).read())
    os.environ.pop('LD_PRELOAD', None)
    print("Creating wine prefix 💫")
    os.system(f"tar -xJf $PREFIX/glibc/opt/darkos/XinputBridge.tar.xz -C /data/data/com.termux/files/usr/glibc/opt/wine/1/wine/lib/wine/ &>/dev/null")
    os.system(f'WINEUSERNAME="DARKOS" WINEDLLOVERRIDES="mscoree=disabled" box64 wine64 wineboot &>/dev/null')
    os.system(f'cp -r $PREFIX/glibc/opt/Startxmenu/* "{wine_prefix}/drive_c/ProgramData/Microsoft/Windows/Start Menu"')
    os.system(f'rm "{wine_prefix}/dosdevices/z:"')
    os.system(f'ln -s /sdcard/Download "{wine_prefix}/dosdevices/o:" &>/dev/null')
    os.system(f'ln -s /data/data/com.termux/files/usr/glibc/opt/G_drive "{wine_prefix}/dosdevices/g:" &>/dev/null')
    os.system(f'ln -s /sdcard/darkos "{wine_prefix}/dosdevices/e:" &>/dev/null')
    os.system(f'ln -s /data/data/com.termux/files "{wine_prefix}/dosdevices/z:"')
    print("Installing OS stuff...")
    os.system(f'wget https://github.com/ahmad1abbadi/extra/releases/download/update/mediafoundation-fix.zip -O $PREFIX/glibc/opt/apps/mf-fix.zip &>/dev/null')
    os.system(f'unzip -o $PREFIX/glibc/opt/apps/mf-fix.zip -d $PREFIX/glibc/opt/apps/mf-fix/ &>/dev/null')
    os.system(f'chmod -R 775 $PREFIX/glibc/opt/apps/mf-fix &>/dev/null')
    os.system(f'box64 wine64 "$PREFIX/glibc/opt/apps/Install OS stuff.bat" &>/dev/null')
    os.system(f'box64 wine64 "$PREFIX/glibc/opt/apps/mf-fix/install.bat" &>/dev/null')
    print("Searching and Recovering previous savegames...")
    if os.path.exists(f"/sdcard/darkos-savegames"):
        print("Previous savegames found! Recovering...")
        os.system(f'cd /sdcard/darkos-savegames/users/; if [ $(ls | grep "^u") != $(whoami) ]; then mv $(ls | grep "^u") $(whoami); fi;  cd -')
        os.system(f'rsync -a /sdcard/darkos-savegames/users/* {wine_prefix}/drive_c/users/ &>/dev/null')
        os.system(f'echo "1" > /sdcard/darkos/last_container_savegame')
    else:
        print("No previous savegames found. Skipping...")
    print("Done!")
    print("prefix done enjoy 🤪 ")
    time.sleep(3)
    os.system("box64 wineserver -k &>/dev/null")
    print(f'done')
    print("")
    print("starting DARK OS ")
    time.sleep(2)
    subprocess.run(["bash", "darkos"])
def install_mono():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/mono.tar.xz")
    os.system("tar -xJf mono.tar.xz")
    os.remove("mono.tar.xz")
def install_wine9():
    os.system("wget -q --show-progress https://github.com/ahmad1abbadi/darkos-lite/releases/download/lite/wine-default.tar.xz")
    os.system("tar -xJf wine-default.tar.xz -C $PREFIX/glibc/opt/wine/1")
    os.remove("wine-default.tar.xz")
    os.system("apt reinstall vulkan-icd-loader-glibc -y &>/dev/null")
def check_and_backup(file_paths):
    home_dir = os.path.expanduser("~")
    full_path = os.path.join(home_dir, file_paths)
    if os.path.exists(full_path):
        backup_path = f"{full_path}.bak"
        os.rename(full_path, backup_path)
def scripts():
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/update-darkos.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/debug-darkos.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/photo.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/darkos &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/run-darkos.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/darkos.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/cpu_boost.py &>/dev/null")
    os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos-lite/main/file-selector &>/dev/null")
    os.system("chmod +x darkos")
    os.system("chmod +x winetricks")
    os.system("chmod +x file-selector")
    os.system("mv darkos update-darkos.py darkos.py winetricks debug-darkos.py run-darkos.py cpu_boost.py photo.py file-selector $PREFIX/bin/")
    check_and_backup(".termux/colors.properties")
    os.system("wget -O $HOME/.termux/colors.properties https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/terminal_utility/colors.properties &>/dev/null")
    check_and_backup(os.getenv("PREFIX") + "/etc/motd-playstore")
    check_and_backup(os.getenv("PREFIX") + "/ect/motd")
    os.system("wget -O $PREFIX/etc/darkos-motd.sh https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/terminal_utility/darkos-motd.sh &>/dev/null")
    os.system(f'echo "bash {os.getenv("PREFIX")}/etc/darkos-motd.sh" >> {os.getenv("PREFIX")}/etc/termux-login.sh')
    check_and_backup(".termux/font.ttf")
    os.system("wget -O $HOME/.termux/font.ttf https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/terminal_utility/ubuntu-mono.ttf &>/dev/null")
def remove():
    os.system("rm glibc-darkos-lite.tar.xz install installglibc.py")
    os.system("clear")
os.system("clear")
print(" Darkos-lite installation is begining 😉")
print("")
edit_bashrc()
print("")
print("please wait .......")
termux_pkg()
print(" 👣")
install_glibc_AZ()
print(" 👣 👣 ")
mangohud()
print(" 👣 👣 👣")
install_conf()
print(" 👣 👣 👣 👣")
install_AZ()
print(" 👣 👣 👣 👣 👣")
install_mono()
print(" 👣 👣 👣 👣 👣 👣")
install_wine9()
print(" 👣 👣 👣 👣 👣 👣 👣")
install_box()
print(" 👣 👣 👣 👣 👣 👣 👣 👣")
update()
print(" 👣 👣 👣 👣 👣 👣 👣 👣 👣 ")
scripts()
print(" 👣 👣 👣 👣 👣 👣 👣 👣 👣 👣")
remove()
print("          Installation finished successfully ")
print("")
start_darkos()
create_prefix()
