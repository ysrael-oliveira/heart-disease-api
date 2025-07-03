from sqlalchemy import Column, String, Integer, Float, Boolean

from model import Base

class Paciente(Base):
    __tablename__ = 'paciente'
    
    id = Column("id",Integer, primary_key = True, autoincrement = True) # id do usuário
    age = Column("Idade", Integer)  # idade do paciente [anos]
    sex = Column("Sexo", String(1))  # sexo do paciente [M: Masculino, F: Feminino]
    chest_pain_type = Column("Tipo de dor no peito", String(3))  # tipo de dor no peito [TA: Angina Típica, ATA: Angina Atípica, NAP: Dor não-anginosa, ASY: Assintomático]
    resting_bp = Column("Pressão arterial em repouso (mm Hg)", Integer)  # pressão arterial em repouso [mm Hg]
    cholesterol = Column("Colesterol (mg/dl)", Integer)  # colesterol sérico [mg/dl]
    fasting_bs = Column("Glicemia em jejum?", Integer)  # glicemia em jejum > 120 mg/dl? 0 ou 1
    resting_ecg = Column("Eletrocardiograma em repouso", String(5))  # eletrocardiograma em repouso [Normal, ST, LVH]
    max_hr = Column("Frequência cardíaca máxima", Integer)  # frequência cardíaca máxima atingida
    exercise_angina = Column("Angina induzida?", String(1))  # angina induzida por exercício? [True: Sim, False: Não]
    oldpeak = Column("Depressão do Segmento ST", Float)  # depressão do segmento ST induzida por exercício em relação ao repouso (oldpeak)
    st_slope = Column("Inclinação do segmento ST", String(5))  # inclinação do segmento ST no pico do exercício [Up: ascendente, Flat: plana, Down: descendente]
    heart_disease = Column("Diagnóstico", Integer)  # diagnóstico final [True: presença de doença cardíaca, False: ausência]
    
    def __init__(self, age: int, sex: bool, chest_pain_type: str, resting_bp: int, cholesterol: int,
                 fasting_bs: bool, resting_ecg: str, max_hr: int, exercise_angina: bool, oldpeak: float,
                 st_slope: str, heart_disease: bool):
        """
        Adiciona um paciente ao banco de dados
        
        Argumentos:
            age:            idade do paciente [anos]
            sex:            sexo do paciente [M: Masculino, F: Feminino]
            chest_pain_type:tipo de dor no peito [TA: Angina Típica, ATA: Angina Atípica, NAP: Dor não-anginosa, ASY: Assintomático]
            resting_bp:     pressão arterial em repouso [mm Hg]
            cholesterol:    colesterol sérico [mg/dl]
            fasting_bs:     glicemia em jejum > 120 mg/dl? [True: Sim, False: Não]
            resting_ecg:    eletrocardiograma em repouso [Normal, ST, LVH]
            max_hr:         frequência cardíaca máxima atingida
            exercise_angina:angina induzida por exercício? [Y or N]
            oldpeak:        depressão do segmento ST induzida por exercício em relação ao repouso (oldpeak)
            st_slope:       inclinação do segmento ST no pico do exercício [Up: ascendente, Flat: plana, Down: descendente]
            heart_disease:  diagnóstico final [True: presença de doença cardíaca, False: ausência]
        """
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp = resting_bp
        self.cholesterol = cholesterol
        self.fasting_bs = fasting_bs
        self.resting_bp = resting_bp
        self.resting_ecg = resting_ecg
        self.max_hr = max_hr
        self.exercise_angina = exercise_angina
        self.oldpeak = oldpeak
        self.st_slope = st_slope
        self.heart_disease = heart_disease
    