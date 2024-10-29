import pyautogui
import time

def open_edge():
    pyautogui.PAUSE = 0.5
    edge = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/edge.png')
    if edge is not None:
        pyautogui.center(edge)
        pyautogui.moveTo(edge, duration=0.3)
        pyautogui.click(button='right')
        pyautogui.moveTo(467,646, duration=0.3)
        pyautogui.click()
        maximeze_screen = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/edge_max.png')
        if maximeze_screen is not None:
            pyautogui.center(maximeze_screen)
            pyautogui.moveTo(maximeze_screen, duration=0.3)
            pyautogui.click()

def new_aba():
    pyautogui.PAUSE = 0.5
    new_aba = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/aba.png')   
    if new_aba is not None:
        pyautogui.center(new_aba)
        pyautogui.moveTo(new_aba, duration=0.3)
        pyautogui.click()
        # Mover um pouco para a direita, por exemplo, 20 pixels
        # offset_y = 40
        # pyautogui.moveTo(center_x, center_y + offset_y, duration=0.3)

def link_google():
    pyautogui.PAUSE = 0.5
    pyautogui.write('https://www.google.com.br')
    pyautogui.press('enter')

def search_link():
    pyautogui.PAUSE = 0.5

    while True:
        link = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/search.png')
        if link is not None:
            pyautogui.center(link)
            pyautogui.moveTo(link, duration=0.3)
            pyautogui.click()
            break

def google_icon_search():
    pyautogui.PAUSE = 0.5
    google = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/search_google.png')
    if google is not None:
        pyautogui.center(google)
        pyautogui.moveTo(google, duration=0.3)
        pyautogui.click()

def google_site_carmais():
    search_link()
    link_google()
    time.sleep(1)
    google_icon_search()
    pyautogui.write('carmais')
    pyautogui.press('enter')
    time.sleep(2)
    while True:
        time.sleep(1)
        pyautogui.PAUSE = 0.5
        pyautogui.scroll(-100)
        site_carmais = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/site_carmais.png')
        if site_carmais is not None:
            pyautogui.center(site_carmais)
            pyautogui.moveTo(site_carmais, duration=0.3)
            pyautogui.click()
            break

    time.sleep(2)

    while True:
        time.sleep(1)
        pyautogui.PAUSE = 0.5
        pyautogui.scroll(-200)
        fim_site = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/fim_site.png')
        if fim_site is not None:
            pyautogui.scroll(-300)
            break

    while True:
        time.sleep(1)
        pyautogui.PAUSE = 0.5
        pyautogui.scroll(200)
        comeco_site = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/comeco_site.png')
        if comeco_site is not None:
            pyautogui.scroll(300)
            break
    
    time.sleep(2)

def maps_carmais():
    new_aba()
    search_link()
    link_google()
    time.sleep(2)

    menu_google = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/menu_google.png')
    if menu_google is not None:
        pyautogui.center(menu_google)
        pyautogui.moveTo(menu_google, duration=0.3)
        pyautogui.click()

    maps = pyautogui.locateOnScreen('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/maps.png')
    if maps is not None:
        pyautogui.center(maps)
        pyautogui.moveTo(maps, duration=0.3)
        pyautogui.click()

if __name__ == '__main__':
    open_edge()
    google_site_carmais()
    maps_carmais()