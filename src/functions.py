from datetime import datetime
from pywhatkit import sendwhatmsg

def get_time() -> tuple:
    """
    Funcao para pegar a hora
    do local em que voce esta
    :return:
    """
    currentDateAndTime = datetime.now()

    currentTime_hours = currentDateAndTime.strftime("%H")
    currentTime_minutes = currentDateAndTime.strftime("%M")

    return currentTime_hours, currentTime_minutes

def wpp(celular:str, msg:str) -> None:
    """
    Funcao para enviar msg no wpp,
    Quando for colocar o numero precisa do codigo
    do pais +55
    :param celular: numero de celular que deseja enviar a msg
    :param msg: mensagem para enviar via WPP
    :return:
    """
    print('Em alguns segundos WhatsApp vai abrir e em 15 segundos enviar sua msg!')
    hora, minuto = get_time()
    sendwhatmsg(celular, msg, int(hora), int(minuto)+2, tab_closeTrue)

    return
