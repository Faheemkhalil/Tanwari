import os

def auto_update():
    os.system("git pull origin main")

if __name__ == "__main__":
    auto_update()
