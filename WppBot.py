import time

from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class WppBot:

    def __init__(self):
        self.driver = self.__define_driver()
        self.link, self.mensagem, self.contatos = self.__reune_informacoes()

    def __define_driver(self):
        return webdriver.Chrome(ChromeDriverManager().install())

    def __reune_informacoes(self):
        return config('LINK_SEL'), config('MESSAGE'), config('CONTACTS_SEL').split(', ')

    def __abre_site_wpp(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(10)

    def __fecha_navegador(self):
        self.driver.close()

    def __busca_contato(self, ctt):
        input_ctt = self.driver.find_element_by_xpath('//div[contains(@class,"_1awRl copyable-text selectable-text")]')
        input_ctt.click()
        input_ctt.send_keys(ctt)
        input_ctt.send_keys(Keys.ENTER)

    def __envia_mensagem(self):
        input_msg = self.driver.find_elements_by_xpath('//div[contains(@class,"_1awRl copyable-text selectable-text")]')[1]
        input_msg.click()
        input_msg.send_keys(self.mensagem)
        input_msg.send_keys(Keys.ENTER)

    def executa(self):
        self.__abre_site_wpp()

        for contato in self.contatos:
            self.__busca_contato(contato)
            time.sleep(1)
            self.__envia_mensagem()

        time.sleep(1)
        self.__fecha_navegador()


if(__name__ == '__main__'):
    bot = WppBot()
    bot.executa()
