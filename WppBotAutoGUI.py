import time
import webbrowser

import pyautogui as gui
from decouple import config


class WppBotAutoGUI:

    def __init__(self):
        self.__link, self.__mensagem, self.__contatos = self.__reune_informacoes()

    def __reune_informacoes(self):
        return config('LINK_SEL'), config('MESSAGE'), config('CONTACTS_SEL').split(', ')

    def __abre_site_wpp(self):
        webbrowser.open(self.__link)

    def __move_e_clica_botao_esquerdo(self, x, y):
        gui.moveTo(x=x, y=y, duration=0.20)
        gui.click(x=x, y=y, button='left', duration=0.20)

    def __formata_link(self, ctt):
        self.__link = self.__link + f'phone={ctt}&text={self.__mensagem}'

    def __fecha_aba(self):
        gui.hotkey('ctrl', 'w')

    def __envia_mensagem(self):
        self.__abre_site_wpp()
        time.sleep(3)

        self.__move_e_clica_botao_esquerdo(921, 346)
        time.sleep(1)

        self.__move_e_clica_botao_esquerdo(924, 425)
        time.sleep(8)

        self.__move_e_clica_botao_esquerdo(1595, 1029)
        time.sleep(1)

        self.__fecha_aba()

    def executa(self):
        for contato in self.__contatos:
            self.__formata_link(contato)
            self.__envia_mensagem()


if (__name__ == '__main__'):
    bot = WppBotAutoGUI()
    bot.executa()
