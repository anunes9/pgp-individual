# Projeto pgp-individual

Este projeto tem como objetivo proporcionar ao aluno uma primeira experiência de planeamento e gestão de um projeto de software. Nesse sentido, a ênfase da execução do projeto deve ser colocada nas tarefas de planeamento e gestão, e não nas tarefas de desenvolvimento (ou seja, não se espera que o produto de software entregue no final do projeto apresente elevados níveis de eficácia e eficiência).

## Produto:

Pretende-se que o aluno desenvolva uma aplicação Web para registo de objetos emprestados pelo utilizador. No mínimo, a aplicação deve realizar as seguintes funcionalidades: 
- registar um empréstimo de um objeto a indicar, numa data a indicar, a uma pessoa a indicar; 
- registar a devolução de um objeto emprestado, numa data a indicar;
- ver uma lista de objetos emprestados atualmente. 

O aluno poderá acrescentar mais funcionalidades se assim o entender. A aplicação Web não deve fazer uso de uma base de dados externa. Deverá usar o conceito de local storage disponibilizado no HTML5.

## Processo e datas de entrega:

O trabalho é individual.

## 1ª fase 

Até ao dia 29 de setembro, o aluno deverá: 
1) analisar as necessidades tecnológicas para a implementação do produto; 
2) desenhar uma solução; 
3) planear o desenvolvimento da solução no prazo de uma semana (5 dias úteis). 
No dia 29 de setembro, o aluno deverá entregar o planeamento, indicando todas as tarefas necessárias, agrupadas em conjuntos lógicos de tarefas, com estimativas de tempo necessário para completar cada tarefa, e os dias em que as prevê desenvolver. O planeamento a entregar deve ser gerado pelo Microsoft Project, e exportado para formato PDF.

## 2ª fase

Até ao dia 6 de outubro, o aluno deverá implementar o projeto de acordo com o planeado. Durante a execução do projeto, o aluno deverá registar o tempo gasto em cada tarefa (sugere-se fortemente o uso de uma aplicação de registo de tempo - e.g., Toggl, grátis e disponível para todas as plataformas).
O aluno deve também registar todas os desvios ao planeamento (e.g., tarefas que demoraram mais ou menos tempo do que o previsto) e alterações ao planeamento (e.g., novas tarefas, ou tarefas que afinal não eram necessárias). 
No dia 6 de outubro, o aluno deverá entregar: 
1) o código da aplicação Web num ficheiro zip (que deverá incluir também um ficheiro de texto com as instruções para instalação da aplicação num servidor Web, caso seja necessário); 
2) uma timesheet com o registo de horas gastas em cada dia em cada tarefa; 
3) um relatório com os desvios e alterações ao planeamento e a sua justificação.

## Instalação

Para a utilização deste projeto é necessário ter o python3 e o flask instalado. O passo seguinte é navegar até a pasta do projeto e fazer "python3 app.py".

## Desenvolvimento

#### Tarefas planeadas:

- [x] Desenvolver base 
    - [x] Servidor Flask - 2 horas
    - [x] Página inicial (html + css) - 2 horas
    
- [x] Funcionalidade Registar Empréstimo
    - [x] html + css - 2 horas
    - [x] javascript - 2 horas
    - [x] ligação ao servidor - 2 horas

- [x] Funcionalidade Registar Devolução
    - [x] html + css - 2 horas
    - [x] javascript - 2 horas
    - [x] ligação ao servidor - 2 horas

- [x] Funcionalidade Listar Empréstimos
    - [x] html + css - 2 horas
    - [x] javascript - 2 horas
    - [x] ligação ao servidor - 2 horas
    
- [x] Finalizar
    - [x] Testes - 2 horas
    - [x] Documentação - 1 hora
    
    
#### Tabela de tempo de cada tarefa

| Tarefa          | Tempo Planeado (horas) | Tempo Usado (horas) |
| :---            |         :---:          |       :---:         |
| Servidor Flask  | 2                      | 0.96                |          
| Página incial   | 2                      | 1.33                |         
| Reg Emp (a)     | 2                      | 0.76                |        
| Reg Emp (b)     | 2                      | 0.86                |       
| Reg Emp (c)     | 2                      | 1.16                |      
| Reg Dev (a)     | 2                      | 0.53                |     
| Reg Dev (b)     | 2                      | 0.46                |    
| Reg Dev (c)     | 2                      | 1.53                |   
| Listar Emp (a)  | 2                      | 0.95                |  
| Listar Emp (b)  | 2                      | 0.50                | 
| Listar Emp (c)  | 2                      | 0.50                |
| Testes          | 2                      | 1.63                |
| Documentação    | 1                      | 0.93                |
| Total           | 25                     | 12.1                |