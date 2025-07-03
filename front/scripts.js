
// Função para consultar lista existente de pacientes por meio de requisição GET
const consultarItens = async() => {
    let url = 'http://127.0.0.1:5000/pacientes'
    fetch(url, {
        method: 'get'
      })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            data.pacientes.forEach((item) => inserirLinha(item.id, item.age, item.sex, item.chest_pain_type, item.resting_bp, 
                item.cholesterol, item.fasting_bs, item.resting_ecg, item.max_hr, item.exercise_angina, item.oldpeak, 
                item.st_slope, item.heart_disease));
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

consultarItens();

// Função para adicionar um novo paciente no banco de dados via POST
const postarItem = async (age, sex, chest_pain_type, resting_bp, cholesterol,fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope) => {
    const formData = new FormData();
    formData.append('age', age);
    formData.append('sex', sex);
    formData.append('chest_pain_type', chest_pain_type);
    formData.append('resting_bp', resting_bp);
    formData.append('cholesterol', cholesterol);
    formData.append('fasting_bs', fasting_bs);
    formData.append('resting_ecg', resting_ecg);
    formData.append('max_hr', max_hr);
    formData.append('exercise_angina', exercise_angina);
    formData.append('oldpeak', oldpeak);
    formData.append('st_slope', st_slope);

    // debugar para ver se dados estao preenchidos corretamente
    for (var pair of formData.entries()) {
        console.log(pair[0]+ ', ' + pair[1]); 
    }

    let url = 'http://127.0.0.1:5000/paciente'
    try{
        const response = await fetch(url, {
            method: 'post',
            body: formData
          })
        
        const data = await response.json();
        return {
            "diagnostico": data.heart_disease,
            "id": data.id
        }
    }
    catch(error) {
        console.error('Error:', error);
    };
}

// Função chamada quando um novo item é adicionado
const novoItem = async (event) => {
    event.preventDefault()
    let inputAge = document.getElementById("age").value;
    let inputSex = document.getElementById("sex").value;
    let inputChestPainType = document.getElementById("chest_pain_type").value;
    let inputRestingBp = document.getElementById("resting_bp").value;
    let inputCholesterol = document.getElementById("cholesterol").value;
    let inputFastingBs = document.getElementById("fasting_bs").value;
    let inputRestingEcg = document.getElementById("resting_ecg").value;
    let inputMaxHr = document.getElementById("max_hr").value;
    let inputExerciseAngina = document.getElementById("exercise_angina").value;
    let inputOldpeak = document.getElementById("oldpeak").value;
    let inputStSlope = document.getElementById("st_slope").value;

    if(!inputAge || !inputSex || !inputChestPainType || !inputRestingBp || !inputCholesterol || !inputFastingBs || 
    !inputRestingEcg || !inputMaxHr || !inputExerciseAngina || !inputOldpeak || !inputStSlope ){
        alert('Todos os campos são obrigatórios!');
    }
    else{
        const resultado = await postarItem(inputAge, inputSex, inputChestPainType, inputRestingBp, inputCholesterol, inputFastingBs,
            inputRestingEcg, inputMaxHr, inputExerciseAngina, inputOldpeak, inputStSlope
        );
        let resultadoDisplay;

        if(resultado.diagnostico == 0){
            resultadoDisplay = "O resultado é negativo :) Paciente em condições normais";
        }
        else if(resultado.diagnostico == 1){
            resultadoDisplay = "O resultado é positivo :( Paciente com doença cardíaca"
        }
        else{
            resultadoDisplay = "Erro no sistema!"; // caso não esteja ligado ao servidor
        }
        
        inserirLinha(resultado.id, inputAge, inputSex, inputChestPainType, inputRestingBp, inputCholesterol, inputFastingBs,
            inputRestingEcg, inputMaxHr, inputExerciseAngina, inputOldpeak, inputStSlope, resultado.diagnostico);
        alert(resultadoDisplay);  
        
    }

}

// Função para inserir paciente na tabela
const inserirLinha = (id, age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope, heart_disease) =>{
    var item = [id, age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope, heart_disease]
    var tabela = document.getElementById("tabelaPacientes");
    var linha = tabela.insertRow();

    //loop para preencher a linha com os dados fornecidos
    var i = 0
    while(i < item.length){
        var dado = linha.insertCell(i);
        dado.textContent = item[i];
        i++;
    }

            //reseta os campos de input para uma nova inserção
        document.getElementById("age").value = "";
        document.getElementById("sex").value = "F";
        document.getElementById("chest_pain_type").value = "TA";
        document.getElementById("resting_bp").value = "";
        document.getElementById("cholesterol").value = "";
        document.getElementById("fasting_bs").value = "0";
        document.getElementById("resting_ecg").value = "Normal";
        document.getElementById("max_hr").value = "";
        document.getElementById("exercise_angina").value = "N";
        document.getElementById("oldpeak").value = "";
        document.getElementById("st_slope").value = "Up";
}
