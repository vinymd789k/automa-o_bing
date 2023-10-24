import pyautogui as pa
import time

#Define quantas pesquisas realizar
qtd_pesquisas = int(input("Quantas pesquisas realizar."))
#armazena a previsão de pontos farmados
qtd_de_pontos = qtd_pesquisas*3
#variáveis para exibir no relatório.
pesquisas_realizadas = 0
pontos_adquiridos = 0
#exibe a previsão de pontos.
print(f"Serão farmados {qtd_de_pontos}")

def farm_de_pontos (qtd_pesquisas, pesquisas_realizadas, pontos_adquiridos):
    
    #delay entre as funções pyautogui
    pa.PAUSE = 0.3
    
    #abrir o navegador.
    pa.press("win")
    pa.write("opera")#aqui pode ser colocado qualquer navegador no lugar de opera.
    pa.press("enter")

    #abre uma nova aba e digita bing.
    pa.hotkey("ctrl", "n")
    pa.write("bing")
    pa.press("enter")

    time.sleep(2)

    #farmando pontos
    for i in range(qtd_pesquisas):
        
        #faz a escrita e confirma
        pa.write(str(i))
        pa.press("enter")

        #armazena os resultados
        pesquisas_realizadas += 1
        pontos_adquiridos += 3

        #retorna a caixa de texto em uma resolução 1920x1280
        pa.click(x = 712, y = 168, button = "left", duration = 1)

        time.sleep(1.5)

    pa.click(x = 1701, y = 178, button = "left", duration = 1)
    
    #define quantos tab a serem loopados
    loop_tab = 7
    #conta quantos tabs foram pressionados
    contador_tab = 0
    #lista com todas as posições de loop_tab a serem puladas.
    pular_loop_tab = [10, 11, 12, 15]
    #variável de continuidade loop while
    while_infinite = 1

    #loop de tab e enter
    while while_infinite == 1:

        #faz loop de tab para 
        while contador_tab < loop_tab:
        
            pa.press("tab")
            contador_tab += 1
    
        #ser os tabs foram pressionados o suficiente, faça a presquisa e retorne a seleção de tab.
        if contador_tab == loop_tab and loop_tab not in pular_loop_tab:
            
            pa.press("enter")
            time.sleep(1.5)
            pa.click(x = 1701, y = 178, button = "left", duration = 1)

            #zerar o contador e garante que haverá mais um tab para acessar o próximo artigo.
            contador_tab = 0
            loop_tab += 1 
            
            #se foram realizados tabs o suficiente para acessar todos os sites, pare o loop e gere o relatório
            if loop_tab == 15:
                break 

        #reconhece se foram pressionados tabs o suficiente para chegar ao site que pode estragar o processo.
        elif loop_tab in pular_loop_tab:
            
            pa.press("tab")
            loop_tab += 1

    #relatório

    return print(f"foram realizadas {pesquisas_realizadas} de pesquisas e farmados {pontos_adquiridos+100} de pontos")

farm_de_pontos(qtd_pesquisas, pesquisas_realizadas, pontos_adquiridos)