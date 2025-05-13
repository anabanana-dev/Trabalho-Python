
def gerar_anuncio_personalizado(gostos):
    gostos = [g.lower() for g in gostos]

    if any(palavra in gostos for palavra in ["moda", "roupa", "vestuário", "estilo", "look"]):
        if "sustentabilidade" in gostos or "eco" in gostos:
            return """
🌿 Moda com propósito 🌿

Você que ama estilo e também se importa com o planeta, vai adorar a nova coleção sustentável da nossa loja!

👗 Looks modernos, confortáveis e ecológicos  
♻️ Materiais recicláveis e produção consciente  
🚚 Frete rápido e embalagem eco-friendly  

Vista-se bem e faça a diferença!  
👉 Confira em www.sualoja.com

#ModaSustentável #FeitoPorVocê
            """
        else:
            return """
✨ Novidades em Moda Feminina ✨

Para quem vive a moda com atitude e ama looks incríveis todos os dias:  
A nova coleção chegou arrasando!

👗 Estilo casual, elegante ou ousado — você escolhe  
🛍 Descontos especiais para novas clientes  
💃 Vista-se com autenticidade!

➡️ www.sualoja.com

#EstiloÉTudo #ModaFeminina
            """

    elif any(palavra in gostos for palavra in ["fitness", "academia", "saúde", "esporte"]):
        return """
💪 Transforme seu estilo de vida agora! 💪

Se seu foco é saúde, bem-estar e alta performance, essa seleção é pra você!

🩳 Roupas fitness ultra confortáveis  
🏋️ Equipamentos e acessórios de treino  
🥗 Dicas de nutrição e e-books exclusivos

👉 Comece sua jornada: www.sualoja.com

#VidaSaudável #CorpoEmMovimento
        """

    elif any(palavra in gostos for palavra in ["tecnologia", "gadgets", "celular", "smart", "computador"]):
        return """
📱 Tecnologia que te entende 📱

Apaixonado por inovação? Temos os gadgets que você procura:

🔌 Smartwatches, fones bluetooth, celulares e mais  
⚡ Alta performance e preços que cabem no bolso  
🚚 Entrega expressa para todo o Brasil

🔍 Explore agora: www.sualoja.com

#TechLovers #SmartLife
        """

    elif any(palavra in gostos for palavra in ["livro", "leitura", "ficção", "romance", "autoconhecimento"]):
        return """
📚 Descubra mundos com um virar de página 📚

Se você ama histórias envolventes, emoção e aprendizado, chegou o seu momento!

📖 Lançamentos em romance, mistério e desenvolvimento pessoal  
🎁 Frete grátis acima de R$ 100  
⭐ Avaliações 5 estrelas dos leitores

📦 Visite: www.sualoja.com

#AmantesDeLivros #LeituraÉVida
        """

    else:
        # Gosto indefinido ou geral
        return """
🎯 Promoções especiais esperando por você! 🎯

Encontre produtos perfeitos para seu estilo de vida — seja ele qual for.

🛍 Diversas categorias com descontos imperdíveis  
📦 Entrega rápida e segura  
💳 Pagamento facilitado

👉 Acesse agora: www.sualoja.com

#CompreInteligente #OfertaPersonalizada
        """


# Exemplo de entrada do cliente
gostos_cliente = [
    "moda",
    "roupa",
    "vestuário",
    "estilo",
    "look",
]

# Geração do anúncio com base nos gostos
anuncio_final = gerar_anuncio_personalizado(gostos_cliente)

# Exibe o resultado
print(anuncio_final)
