from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o token do Slack das variáveis de ambiente
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
if not SLACK_TOKEN:
    raise ValueError("SLACK_TOKEN não encontrado nas variáveis de ambiente. Configure o arquivo .env com seu token.")

client = WebClient(token=SLACK_TOKEN)

# Lista de usuários (IDs do Slack) que receberão a mensagem
# Você precisará substituir estes IDs pelos IDs reais dos usuários
USUARIOS = [
    "U08H4584143", #wata
    "U07PQDPF0R1", #anderson
    "U08EQ57ELGY", #marcão
    "U05B1GVFNMA", #caue
    "U05BL7Y9KUH", #koba
    "U05B7JMAP34", #pedro
    "U08M0E654AH", #livia
    "U07T72RA80H", #marcolino
    "U06F1B2JVJ8", #diego
    "U05B43T4K33", #marcos
    "U05GX327MDK" #pk
]

def enviar_lembretes():
    mensagem = ("Salve! Este é um lembrete amigável para emitir sua Nota Fiscal (NF) "
               "referente ao mês atual. Por favor, emita sua NF para garantir que seu "
               "pagamento seja processado dentro do prazo. Obrigado!")
    
    for usuario_id in USUARIOS:
        try:
            # Envia mensagem direta para cada usuário
            resultado = client.chat_postMessage(
                channel=usuario_id,
                text=mensagem
            )
            print(f"Mensagem enviada com sucesso para o usuário {usuario_id}")
        
        except SlackApiError as e:
            print(f"Erro ao enviar mensagem para {usuario_id}: {e.response['error']}")

def verificar_e_enviar():
    # Verifica se é dia 25
    if datetime.now().day == 25:
        enviar_lembretes()

def testar_envio():
    print("Iniciando teste de envio...")
    enviar_lembretes()
    print("Teste de envio concluído!")

def main():
    # Se quiser testar o envio imediatamente, descomente a linha abaixo:
    testar_envio()
    
    # Comentando temporariamente o agendamento para teste
    # schedule.every().day.at("10:00").do(verificar_e_enviar)
    # print("Bot iniciado! Aguardando horário programado...")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # Espera 1 minuto antes de verificar novamente

if __name__ == "__main__":
    main() 