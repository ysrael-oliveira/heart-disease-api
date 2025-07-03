import pandas as pd

from sklearn.metrics import accuracy_score

class SuporteTeste:
    
    def __init__(self):
        """ Inicializa a classe de suporte ao teste"""
        pass
    
    def carrega_dados(self, url_csv, colunas):
        df = pd.read_csv(url_csv, names=colunas, header=0, skiprows=0, delimiter=',')
        X = df.drop("target", axis=1)
        y = df["target"]
        return X, y
    
    def get_accuracy_score(self, modelo, dados_teste):
        X, y = dados_teste
        y_pred = modelo.predict(X.values)
        return accuracy_score(y, y_pred)
    