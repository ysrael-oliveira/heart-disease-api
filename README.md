# Heart Disease API

Projeto de aplicação full stack que consulta modelo de Machine Learning para previsão de insuficiência cardíaca, a partir de dados clínicos do paciente. Desenvolvido para a Pós-Graduação de Engenharia de Software da PUC-Rio.

## Índice

1. [Sobre]
2. [Execução]
3. [Tecnologias usadas]
4. [Autor]

## Sobre
Este projeto é uma API que visa prever se um determinado paciente possui insuficiência cardíaca ou não a partir dos seus dados clínicos. Para treinamento e teste do modelo, foi usado um dataset público do Kaggle, Heart Failure Prediction Dataset. O modelo foi então exportado e usado no backend do sistema.

## Execução
1. Abrir o diretório referente a pasta api
   ```
   $ cd api
   ```
2. É indicada a instalação de um ambiente virtual para instalação e uso nas versões adequadas dos pacotes necessários:
    Instalação:
    ```
    $ python -m venv venv_api 
    ```
    Ativação:
    ```
    $ .\venv_api\Scripts\activate      
    ```
3. Devem então ser instalados os pacotes presentes no arquivo requirements.txt
    ```
    (venv) $ pip install -r requirements.txt 
    ```
4. Executar a API
    ```
    (venv) $ flask run --host 0.0.0.0 --port 5000  
    ```
5. Abrir no navegador o arquivo index.html, presente na pasta 'front'.

Observação: Para garantir a qualidade da aplicação, foi adicionado um arquivo Pytest que visa garantir uma acurácia mínima de 80% em futuras atualizações do modelo. Para executar o teste, use o seguinte comando no terminal.
```
    (venv) $ pytest -v teste_modelo.py 
```

## Tecnologias usadas
Python
Flask
pydantic
SQLAlchemy
Skicit-Learn
Pandas
Matplotlib
Pytest
HTML
CSS
JS

## Autor
Ysrael Oliveira (ysraeldev@gmail.com)
