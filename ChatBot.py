def responder(pergunta):
    pergunta = pergunta.lower()

    respostas = {
        "horário de atendimento": "Nosso horário de atendimento é das 8h às 18h, de segunda a sexta-feira.",
        "formas de pagamento": "Aceitamos cartão de crédito, débito, Pix e boleto bancário.",
        "prazo de entrega": "O prazo de entrega varia de 3 a 7 dias úteis, dependendo da sua região.",
        "cancelamento": "Para cancelar seu pedido, entre em contato com o suporte pelo e-mail suporte@empresa.com.",
        "troca ou devolução": "Você pode solicitar a troca ou devolução em até 7 dias após o recebimento.",
        "contato": "Você pode nos chamar pelo WhatsApp (11) 99999-9999 ou enviar um e-mail para contato@empresa.com.",
        "obrigado": "De nada! Se precisar de algo mais, é só perguntar :)"
    }

    for chave in respostas:
        if chave in pergunta:
            return respostas[chave]

    return "Desculpe, não entendi sua pergunta. Pode reformular ou falar com um atendente?"

# Simulador de uso
print("Olá! Sou o assistente virtual. Como posso te ajudar? (Digite 'sair' para encerrar)\n")
while True:
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("Chatbot: Obrigado por conversar. Até logo!")
        break
    resposta = responder(entrada)
    print("Chatbot:", resposta)
