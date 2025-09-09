from window import main as window
from shortcut import create_shortcut

def main():
    install(window())

def install(choice):
    import os
    import requests
    import tempfile
    import shutil
    import subprocess
    from pathlib import Path

    home = Path.home()

    if choice[0]:
        subprocess.run(
            ["cmd", "/c", "winget install --id 9PKL3H9LWMB7 --silent --accept-source-agreements --accept-package-agreements && exit"],
        )

        subprocess.run(
            ["cmd", "/c", "start shell:appsFolder\\29645FreeConnectedLimited.X-VPN-FreeUnlimitedVPNPr_qjvpctbgym0d0!App"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        link = "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe"      
    
    else:
        link = "https://cdn.fastly.steamstatic.com/client/installer/SteamSetup.exe"
        

    if os.path.exists(steampath) and os.path.isdir(steampath):
        shutil.rmtree(steampath)
    subprocess.run(["powershell", "-Command", "mkdir $HOME/steam"], creationflags=subprocess.CREATE_NO_WINDOW)
    steampath = home/"steam"
    
    with tempfile.TemporaryDirectory() as tempdir:
        local_filename = os.path.join(tempdir, "SteamSetup.exe")
    
        # Download and save the file
        response = requests.get(link)
        with open(local_filename, 'wb') as f:
            f.write(response.content)
    
        env = os.environ.copy() 
        env["__COMPAT_LAYER"] = "RunAsInvoker"
        proc = subprocess.Popen(local_filename, env=env, shell=True)
        proc.wait()

    if choice[1]:
        os.rename(f"{str(home)}\\steam\\Steam.exe", f"{str(home)}\\steam\\Stim.exe")
        ending = "Stim"
    else:
        ending = "Steam"

    if choice[0]:
        starter = home/"steam"/f"{ending}.bat"
        starter.write_text(f"start {str(home)}\\steam\\{ending}.exe\nstart shell:appsFolder\\29645FreeConnectedLimited.X-VPN-FreeUnlimitedVPNPr_qjvpctbgym0d0!App")
        if os.path.exists(f"{str(home)}\\Desktop\\Steam.lnk") and os.path.isfile(f"{str(home)}\\Desktop\\Steam.lnk"):
            os.remove(f"{str(home)}\\Desktop\\Steam.lnk")

        create_shortcut(f"{str(home)}\\steam\\{ending}.exe", f"{str(home)}\\Desktop\\Steam.lnk", f"{str(home)}\\steam\\{ending}.exe")

    else:
        if os.path.exists(f"{str(home)}\\Desktop\\Steam.lnk") and os.path.isfile(f"{str(home)}\\Desktop\\Steam.lnk"):
            os.remove(f"{str(home)}\\Desktop\\Steam.lnk")

        create_shortcut(f"{str(home)}\\steam\\{ending}.exe", f"{str(home)}\\Desktop\\Steam.lnk", f"{str(home)}\\steam\\{ending}.exe")

if __name__ == "__main__":
    main()
