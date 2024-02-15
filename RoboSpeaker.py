import os
if __name__=='__main__':
    print("Robo Speaker : ")
    print("Enter text to be spoken Or enter 'zx' to quit")
    while True:
        txt=input("Enter what needs to be spoken : ")
        if txt=="zx":
            os.system("say 'goodbye,Have a good day'")
            break
        command=f"say {txt}"
        os.system(command)