from src.functions import wpp
from pywhatkit import sendwhatmsg_instantly, open_web
import time

def main():

    lista_num = ["+551198", '+5514996']
    
    for num in lista_num:
    
        sendwhatmsg_instantly(
            phone_no=num,
            message="Venha para o meu casamento seu corno!",
            wait_time= 10,
            tab_close=True,
            close_time=3
        )

        print(f"Mensagem enviada para {num} com sucesso!")
        time.sleep(4)
    
    return

if __name__ == "__main__":
    main()
    
