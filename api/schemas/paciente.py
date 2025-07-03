from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente

class PacienteSchema(BaseModel):
    """ Define como um novo paciente deve ser adicionado
    """
    age:            int = 78
    sex:            str = "M"
    chest_pain_type:str = "ATA"
    resting_bp:     int = 120
    cholesterol:    int = 200
    fasting_bs:     int = 1 
    resting_ecg:    str = "Normal"
    max_hr:         int = 140
    exercise_angina: str = "Y"
    oldpeak:        float = 1.5 
    st_slope:       str = "Up"
    
class PacienteViewSchema(BaseModel):
    """ Define como um novo paciente deve ser adicionado
    """
    id:             int = 1
    age:            int = 78
    sex:            str = "M"
    chest_pain_type:str = "ATA"
    resting_bp:     int = 120
    cholesterol:    int = 200
    fasting_bs:     int = 0 
    resting_ecg:    str = "Normal"
    max_hr:         int = 140
    exercise_angina:str = "Y"
    oldpeak:        float = 1.5 
    st_slope:       str = "Up"
    heart_disease:  int = 0
    
class ListaPacientesSchema(BaseModel):
    """ Define como a lista de pacientes deve ser retornada
    """
    pacientes: List[PacienteViewSchema]
    
def apresenta_paciente(paciente:Paciente):
    """ Retorna os dados de um paciente
    """
    return {
        "id": paciente.id,
        "age":  paciente.age,
        "sex":  paciente.sex,
        "chest_pain_type": paciente.chest_pain_type,
        "resting_bp": paciente.resting_bp,
        "cholesterol": paciente.cholesterol,
        "fasting_bs": paciente.fasting_bs,
        "resting_ecg": paciente.resting_ecg,
        "max_hr": paciente.max_hr,
        "exercise_angina": paciente.exercise_angina,
        "oldpeak": paciente.oldpeak,
        "st_slope": paciente.st_slope,
        "heart_disease": paciente.heart_disease
    }
    
def apresenta_pacientes(pacientes:List[Paciente]):
    """ Retorna lista de pacientes
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "age":  paciente.age,
            "sex":  paciente.sex,
            "chest_pain_type": paciente.chest_pain_type,
            "resting_bp": paciente.resting_bp,
            "cholesterol": paciente.cholesterol,
            "fasting_bs": paciente.fasting_bs,
            "resting_ecg": paciente.resting_ecg,
            "max_hr": paciente.max_hr,
            "exercise_angina": paciente.exercise_angina,
            "oldpeak": paciente.oldpeak,
            "st_slope": paciente.st_slope,
            "heart_disease": paciente.heart_disease
        })
    return {"pacientes": result}
    