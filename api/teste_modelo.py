from model import *
import pickle

# To run: pytest -v teste_modelo.py

# Parâmetros de teste   
url_dados = "./MachineLearning/data/test_heart_disease.csv"
colunas =  ['age', 'sex', 'resting_bp', 'cholesterol', 'fasting_bs', 'max_hr', 'oldpeak',
                    'chest_pain_type_ATA', 'chest_pain_type_NAP', 'chest_pain_type_TA',
                    'resting_ecg_Normal', 'resting_ecg_ST',
                    'exercise_angina_Y',
                    'st_slope_Flat', 'st_slope_Up', 'target']

suporte_teste = SuporteTeste()

# Carga dos dados
dataset_teste = suporte_teste.carrega_dados(url_dados, colunas)

# Método para testar modelo NB
def test_nb():
    # Importa modelo NB
    nb_path = './MachineLearning/model/heart_disease_kb.pkl'
    with open(nb_path, 'rb') as f:
        modelo_nb = pickle.load(f)

    # Obtém as métricas do NB
    acuracia_nb = suporte_teste.get_accuracy_score(modelo_nb, dataset_teste)
    print(f'Acurácia do modelo: {acuracia_nb:.2%}')
    
    # Teste da acurácia do NB
    assert acuracia_nb >= 0.80 