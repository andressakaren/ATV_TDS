import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
# Carrega os dados
df = pd.read_csv('heart.csv')

# Separa as variáveis
X = df.drop('output', axis=1)
y = df['output']


# Normaliza os dados (muito importante para o LinearSVC)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divide treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Treina o modelo LinearSVC
svc = LinearSVC(max_iter=10000)
svc.fit(X_train, y_train)

# Faz previsões
y_pred = svc.predict(X_test)

# Mostra os resultados
print('Acurácia:', accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))