import typer
from unity import UNITY_PATH, UNITY_VERSION


# Opening Message
def greeting():
    print("W3D TRANSLATOR")
    print(f"Unity Version:\t {UNITY_VERSION}")
    print(f'Please ensure Unity is installed at {UNITY_PATH}\n')  

if __name__ == '__main__':
    greeting()