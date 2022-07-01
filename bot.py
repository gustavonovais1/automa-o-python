from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class RoboYoutube():

    def busca(self, busca, paginas): 
        self.webdriver1 = webdriver.Chrome(executable_path='chromedriver.exe')
        videos = []
        pagina = 1

        url = 'https://www.youtube.com/results?search_query=%s' % busca
        self.webdriver1.get(url)
        while pagina <= paginas:
            titulos = self.webdriver1.find_elements(By.XPATH,'//a[@id="video-title"]')
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Video encontrado:%s" % titulo.text)
                    videos.append(titulo.text)
            self.proximaPagina(pagina)
            pagina += 1

    def proximaPagina(self, pagina):
        print('Mudando para a proxima pagina%s' % (pagina + 1))
        Button = pagina * 10000
        self.webdriver1.execute_script("window.scrollTo(0, %s);" % Button)
        time.sleep(5)

bot = RoboYoutube()
bot.busca("Linkedin", 5)


