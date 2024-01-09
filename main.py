import pyautogui as bot
import time
import pandas as pd
bot.PAUSE = 1
tabela = pd.read_csv("produtos.csv")

#primeiro passo: entrar no google
bot.press('win')        #pressiona a tecla windows
bot.write("google")     #escreve google na barra de pesquisa do windows 
bot.press('enter')      #pressiona o enter

#segundo passo: entrar no site
bot.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")        #cola esse link na barra de pesquisa do google
bot.press('enter')      #pressiona o enter

#terceiro passo: login
bot.click(x=752, y=374) #leva o mouse até o ponto e clica uma vez
bot.write("pedroh.geforce@gmail.com")       #escreve este email no login
bot.press('tab')                            #pressiona o tab
bot.write("123")                            #escreve a senha                     
bot.press('enter')                          #pressiona o enter

#quarto passo: preencher a tabela
bot.press('tab')

for linha in tabela.index:      #le cada linha da tabela

    bot.write(str(tabela.loc[linha, "codigo"]))
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "marca"]))
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "tipo"]))
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "categoria"])) 
    bot.press('tab')

    bot.write(str(tabela.loc[linha, "preco_unitario"])) 
    bot.press('tab')
    
    bot.write(str(tabela.loc[linha, "custo"])) 
    bot.press('tab')

    if pd.isna(tabela.loc[linha,"obs"]):        #verifica se ha algo escrito em obs
        bot.write(str(tabela.loc[linha, "obs"]))
    
    bot.press('tab')    
    bot.press('enter')
    bot.scroll(1000)
    bot.click(x=765, y=256)



