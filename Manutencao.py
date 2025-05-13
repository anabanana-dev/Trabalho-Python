from datetime import datetime, timedelta


equipamentos = [
    {
        "nome": "Compressor de Ar",
        "ultima_manutencao": "2024-12-10",
        "frequencia_dias": 30
    },
    {
        "nome": "Esteira Transportadora",
        "ultima_manutencao": "2025-03-01",
        "frequencia_dias": 45
    },
    {
        "nome": "Torno Mecânico",
        "ultima_manutencao": "2025-04-05",
        "frequencia_dias": 60
    }
]


def planejar_manutencoes(equipamentos):
    hoje = datetime.today().date()
    print(f"\n📅 Data atual: {hoje.strftime('%d/%m/%Y')}")
    print("\n🔧 PLANEJAMENTO DE MANUTENÇÃO PREDITIVA\n")

    for eq in equipamentos:
        nome = eq["nome"]
        ultima = datetime.strptime(eq["ultima_manutencao"], "%Y-%m-%d").date()
        frequencia = timedelta(days=eq["frequencia_dias"])
        proxima = ultima + frequencia

        status = ""
        if proxima <= hoje:
            status = "⚠️ MANUTENÇÃO URGENTE!"
        elif (proxima - hoje).days <= 5:
            status = "🟡 Agendar em breve"
        else:
            status = "🟢 Dentro do prazo"

        print(f"• Equipamento: {nome}")
        print(f"  Última manutenção: {ultima.strftime('%d/%m/%Y')}")
        print(f"  Próxima prevista: {proxima.strftime('%d/%m/%Y')}")
        print(f"  Status: {status}\n")

planejar_manutencoes(equipamentos)
