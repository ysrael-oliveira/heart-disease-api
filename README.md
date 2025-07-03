# Babyzar

Babyzar combina Baby (Bebê) + Bazar e visa simplificar o controle de roupas dos bebês, que facilmente se perdem. Os pais poderão então registrar qual valor de compra e já sugerir um valor de venda, facilitando o uso sustentável de roupas e permitindo a geração de uma renda extra para que os pais possam comprar fraldas.

## Índice

1. [Sobre]
2. [Execução]
3. [Tecnologias usadas]
4. [Autor]

## Sobre
Este projeto é uma API que visa controlar as roupas de um bebê, podendo ser usada por pais para ter o estoque de roupas e desde já planejar a venda das mesmas. Ela permite adicionar, remover e consultar as roupas que estão no banco de dados

## Execução
1. Abrir o diretório referente a pasta babyzar_api
   ```
   $ cd babyzar_api
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
## Tecnologias usadas
Python
Flask
pydantic
SQLAlchemy

## Autor
Ysrael Oliveira (ysraeldev@gmail.com)
