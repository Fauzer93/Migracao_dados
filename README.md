Fluxo de Execução
  O script abre o aplicativo legado e pesquisa o funcionário pelo ID.
  Ele captura os dados diretamente da interface do usuário (via coordenadas X e Y) usando o PyAutoGUI.
  Em seguida, o script consulta a API para obter os dados faltantes, como data de início e número de telefone.
  Os dados de ambos os sistemas são combinados e exibidos como saída.

Certifique-se de que o aplicativo legado esteja acessível: O caminho para o executável do aplicativo legado está definido na variável caminho_do_script dentro da função consultar_no_sistema_legado. Atualize esse caminho conforme o local onde o arquivo está no seu sistema:

caminho_do_script = r'F:\Documents\EmployeeList\EmployeeList.exe'
Execute o Script:

Substitua o id_funcionario com o ID do funcionário que você deseja consultar:

id_funcionario = "1006"

Execute o script:
python script.py
Saída: Os dados completos do funcionário serão exibidos no terminal, combinando as informações do aplicativo legado e da API de integração de RH.

Exemplo de Saída

{
  "first_name": "John",
  "last_name": "Doe",
  "department": "IT",
  "city": "Campo Grande",
  "state": "MS",
  "manager": "Jane Doe",
  "email_id": "john.doe@example.com",
  "job_title": "Software Engineer",
  "zip": "12345",
  "phone_number": "67984113418",
  "start_date": "2020-01-15"
}
