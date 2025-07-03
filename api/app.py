from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente
from model.preprocessador import PreProcessador
from schemas.paciente import PacienteSchema, ListaPacientesSchema, PacienteViewSchema, apresenta_paciente, apresenta_pacientes
from schemas.error import ErrorSchema
from flask_cors import CORS

import pickle

info = Info(title="Heart Failure Diagnosys API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definir tags
home_tag = Tag(name="Documentação", description="Direciona para Swagger")
paciente_tag = Tag(name="Paciente", description="Inserção, consulta e deleção de pacientes da base")

# define tela de início
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para openapi, para documentação como Swagger.
    """
    return redirect('/openapi')

# adicionar um novo paciente
@app.post("/paciente", tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_roupa(form: PacienteSchema):
    """
    Adiciona um novo paciente à base de dados.
    """
    # Carrega modelo
    with open('./MachineLearning/model/heart_disease_kb.pkl', 'rb') as f:
        modelo = pickle.load(f)
        
    preProcessador = PreProcessador()
    
    entrada_processada = preProcessador.preprocessa_dados(form)
    
    saida = modelo.predict(entrada_processada.values)
    
    
    paciente = Paciente(
        age = form.age,
        sex = form.sex,
        chest_pain_type = form.chest_pain_type,
        resting_bp = form.resting_bp,
        cholesterol = form.cholesterol,
        fasting_bs = form.fasting_bs,
        resting_ecg = form.resting_ecg,
        max_hr = form.max_hr,
        exercise_angina = form.exercise_angina,
        oldpeak = form.oldpeak,
        st_slope = form.st_slope,
        heart_disease = int(saida)
    )
    try:
        session = Session()
        session.add(paciente)
        session.commit()
        return apresenta_paciente(paciente), 200
    
    except Exception as exc:
        msg_erro = "Erro ao adicionar este item!"
        return({"message": msg_erro}, 400)
    
    
# recupera todos os pacientes
@app.get("/pacientes", tags=[paciente_tag],
          responses={"200": ListaPacientesSchema, "400": ErrorSchema})
def get_pacientes():
    """
    Busca todas os pacientes presentes no banco de dados
    """
    session = Session()
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        return {"pacientes": []}, 200
    else:
        return apresenta_pacientes(pacientes), 200