
from sklearn.tree import DecisionTreeClassifier  #
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

dados = pd.DataFrame({
    "peso": [100, 105, 110, 95, 130, 102, 98, 200, 85, 300],
    "tamanho": [10, 10.5, 11, 9.5, 13, 10.2, 9.8, 20, 8, 30],
    "cor": [1, 1, 1, 1, 1, 2, 2, 3, 2, 3],  # Suponha: 1 = padrão, 2 = fora do padrão, 3 = falha grave
    "resultado": [1, 1, 1, 1, 1, 0, 1, 0, 0, 0]  # 1 = aprovado, 0 = reprovado
})

X = dados[["peso", "tamanho", "cor"]]
y = dados["resultado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
print("🎯 Acurácia do modelo:", accuracy_score(y_test, previsoes))


novos_produtos = pd.DataFrame({
    "peso": [101, 150, 89],
    "tamanho": [10.1, 12, 9.0],
    "cor": [1, 2, 3]
})

resultados = modelo.predict(novos_produtos)

for i, r in enumerate(resultados):
    status = "🟢 Aprovado" if r == 1 else "🔴 Reprovado"
    print(f"Produto {i+1}: {status}")
