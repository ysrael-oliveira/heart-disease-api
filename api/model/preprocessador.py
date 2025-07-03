import pandas as pd
from sklearn.preprocessing import LabelEncoder

class PreProcessador:
    
    def __init__(self):
        """ Inicializa o pre-processador"""
        pass
    
    def preprocessa_dados(self, form):
        
        expected_columns = ['age', 'sex', 'resting_bp', 'cholesterol', 'fasting_bs', 'max_hr', 'oldpeak',
                    'chest_pain_type_ATA', 'chest_pain_type_NAP', 'chest_pain_type_TA',
                    'resting_ecg_Normal', 'resting_ecg_ST',
                    'exercise_angina_Y',
                    'st_slope_Flat', 'st_slope_Up']
        
        pacienteJSON = {
            "age": form.age,
            "sex": form.sex,
            "resting_bp": form.resting_bp,
            "cholesterol": form.cholesterol,
            "fasting_bs": form.fasting_bs,
            "max_hr": form.max_hr,
            "oldpeak": form.oldpeak,
            "chest_pain_type": form.chest_pain_type,
            "resting_ecg": form.resting_ecg,
            "exercise_angina": form.exercise_angina,
            "st_slope": form.st_slope
        }
    
        df = pd.DataFrame([pacienteJSON])
        
        # trata coluna binária Sex
        le = LabelEncoder()
        le.fit(["F", "M"])
        df["sex"] = le.transform(df["sex"])
        
        # trata colunas categóricas
        categorical_columns = ['chest_pain_type', 'resting_ecg', 'exercise_angina', 'st_slope']
        
        for col in categorical_columns: #garante que são string
            df[col] = df[col].astype(str).str.strip()
            
        df = pd.get_dummies(df, columns= categorical_columns, drop_first=False)
        
        # adicionar colunas faltantes
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0

        df = df[expected_columns]
        
        return df