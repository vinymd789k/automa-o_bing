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

    time.sleep(5)

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

    #relatório
    return print(f"foram realizadas {pesquisas_realizadas} de pesquisas e farmados {pontos_adquiridos} de pontos")

farm_de_pontos(qtd_pesquisas, pesquisas_realizadas, pontos_adquiridos)