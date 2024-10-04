import pyautogui
import time
import pyperclip
import subprocess
import requests

# Função para clicar e copiar o texto de um campo específico
def copiar_texto(x, y):
    pyautogui.click(x=x, y=y)  # Clica no campo específico
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')  # Seleciona o texto
    pyautogui.hotkey('ctrl', 'c')  # Copia o texto para a área de transferência
    time.sleep(1)


# Função para consultar um funcionário no sistema legado
def consultar_no_sistema_legado(id_funcionario):
    # Abrir o aplicativo legado
    caminho_do_script = r'F:\Documents\EmployeeList\EmployeeList.exe'
    subprocess.Popen(caminho_do_script)  # Abre o aplicativo
    time.sleep(5)  # Esperar o aplicativo abrir completamente

    # Clica na posição para buscar o funcionário (coordenadas para o campo de ID)
    pyautogui.click(x=2171, y=127)  # Clique no campo de ID para focar

    # Esperar para garantir que o campo foi focado
    time.sleep(1)

    # Apagar qualquer texto existente no campo (caso necessário)
    pyautogui.hotkey('ctrl', 'a')  # Seleciona o texto atual
    pyautogui.press('backspace')  # Apaga o texto selecionado

    # Inserir o ID do funcionário
    pyautogui.write(id_funcionario)  # Digita o ID do funcionário
    time.sleep(1)  # Espera um pouco para garantir que o texto foi inserido

    # Clica no botão "Search" (ajustar as coordenadas do botão)
    pyautogui.click(x=596, y=259)  # Coordenadas do botão "Search"
    time.sleep(3)  # Espera o carregamento dos dados

    # Capturar os dados de cada campo específico
    first_name = copiar_texto(x=373, y=357)  # Coordenadas para o campo First Name
    last_name = copiar_texto(x=387, y=401)  # Coordenadas para o campo Last Name
    department = copiar_texto(x=689, y=395)  # Coordenadas para o campo Department
    city = copiar_texto(x=402, y=491)  # Coordenadas para o campo City
    state = copiar_texto(x=749, y=491)  # Coordenadas para o campo State
    manager = copiar_texto(x=736, y=450)  # Coordenadas para o campo Manager
    email_id = copiar_texto(x=425, y=444)  # Coordenadas para o campo Email ID
    job_title = copiar_texto(x=808, y=347)  # Coordenadas para o campo Job Title
    zip_code = copiar_texto(x=411, y=539)  # Coordenadas para o campo Zip

    # Retorna os dados capturados do sistema legado
    dados_legado = {
        "first_name": first_name,
        "last_name": last_name,
        "department": department,
        "city": city,
        "state": state,
        "manager": manager,
        "email_id": email_id,
        "job_title": job_title,
        "zip": zip_code
    }

    return dados_legado

# Função para consultar um funcionário na API
def consultar_na_api(id_funcionario):
    url = f"https://botgames-employee-data-migration-vwsrh7tyda-uc.a.run.app/employees?id={id_funcionario}"
    headers = {
        "Authorization": " ",  # Insira seu token de API
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dados_api = response.json()  # Converte a resposta para JSON
        # Retorna os dados relevantes da API
        return {
            "phone_number": dados_api.get("phoneNumber"),
            "start_date": dados_api.get("startDate")
        }
    else:
        print(f"Erro ao consultar funcionário {id_funcionario}: {response.status_code}")
        return None

# Função para combinar dados da API e do sistema legado
def combinar_dados(id_funcionario):
    # Consultar os dados no sistema legado
    dados_legado = consultar_no_sistema_legado(id_funcionario)

    # Consultar os dados na API
    dados_api = consultar_na_api(id_funcionario)

    if dados_api:
        # Combinar os dados das duas fontes
        dados_completos = {**dados_legado, **dados_api}
        return dados_completos
    else:
        print(f"Erro ao obter dados da API para o funcionário {id_funcionario}")
        return dados_legado  # Retorna apenas os dados do legado caso a API falhe

# Exemplo de uso
id_funcionario = "1006"  # ID do funcionário que você quer consultar
dados_completos = combinar_dados(id_funcionario)

# Exibir os dados combinados
print(dados_completos)
