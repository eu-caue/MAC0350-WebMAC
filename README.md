# Problem Set Builder

## Descrição

Problem Set Builder é uma aplicação web simples para organizar e gerenciar coleções de problemas ou exercícios.

A aplicação permite cadastrar, categorizar, visualizar e gerenciar problemas de diferentes áreas do conhecimento. O sistema foi projetado de forma genérica, podendo ser utilizado para organizar exercícios de áreas como matemática, física, economia ou outras disciplinas.

Embora o sistema seja genérico, exemplos utilizados ao longo do projeto incluem problemas de **programação competitiva** e **entrevistas técnicas**.

O objetivo do projeto é aplicar os conceitos estudados na disciplina de desenvolvimento web, incluindo criação de interfaces responsivas, uso de banco de dados e implementação de operações CRUD em uma aplicação web simples.

---

## Funcionalidades

A aplicação permite ao usuário:

* cadastrar novos problemas
* organizar problemas por categorias
* definir níveis de dificuldade
* visualizar a lista de problemas cadastrados
* filtrar problemas por título, categoria ou dificuldade
* atualizar informações de um problema
* remover problemas do banco de dados

Essas operações são implementadas utilizando **HTMX**, permitindo atualizar partes da interface sem recarregar toda a página.

---

## Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias:

* **HTML**
* **FastAPI** para o backend da aplicação
* **HTMX** para comunicação dinâmica entre frontend e backend
* **SQLModel (SQLite)** para persistência de dados

---

## Modelos de Dados

A aplicação utiliza dois modelos principais no banco de dados.

### Categoria

Representa um tema ou área à qual os problemas pertencem.

Exemplos de categorias incluem:

* Strings
* Grafos
* Programação Dinâmica
* Matemática
* Macroeconomia

Cada categoria pode possuir vários problemas associados.

---

### Problema

Representa um exercício ou problema específico.

Cada problema possui as seguintes informações:

* título
* enunciado
* nível de dificuldade
* categoria associada

A relação entre os modelos é:

Categoria (1) -> (N) Problemas

Ou seja, uma categoria pode possuir vários problemas, mas cada problema pertence a apenas uma categoria.

---

## Telas da Aplicação

A aplicação possui duas interfaces principais.

### Lista de Problemas

Tela responsável por exibir todos os problemas cadastrados.

Nela o usuário pode:

* visualizar problemas
* aplicar filtros por título, categoria e dificuldade
* editar problemas existentes
* remover problemas do sistema

---

### Cadastro/Edição de Problemas

Interface utilizada tanto para adicionar novos problemas quanto para editar problemas existentes.

O usuário pode informar:

* título
* categoria
* dificuldade
* enunciado do problema

---

## Operações CRUD

As operações básicas sobre os dados são implementadas utilizando **HTMX**.

As principais operações incluem:

* criação de problemas
* consulta de problemas
* atualização de informações
* remoção de problemas

Essas operações correspondem aos métodos HTTP padrão:

* **POST** para criação
* **GET** para leitura
* **PUT** para atualização
* **DELETE** para remoção

---

## Interface Responsiva

A interface da aplicação foi desenvolvida para funcionar tanto em **computadores** quanto em **dispositivos móveis**.

---

## Uso de Inteligência Artificial

Durante o desenvolvimento do projeto, ferramentas de IA foram utilizadas de forma pontual como apoio.

No frontend, foi criado um template inicial em HTML manualmente, e ferramentas de IA foram utilizadas para:

* auxiliar na integração com HTMX
* ajustar o comportamento dinâmico da interface
* melhorar a responsividade para dispositivos móveis
* resolver detalhes específicos de implementação

No backend, o desenvolvimento foi baseado majoritariamente no conteúdo apresentado em aula (FastAPI e SQLModel). O uso de IA foi restrito a:

* esclarecimento de dúvidas pontuais
* auxílio na depuração de erros específicos

---

## Possíveis Extensões

Algumas funcionalidades que poderiam ser adicionadas em versões futuras incluem:

* criação de listas de exercícios (problem sets) compostas por múltiplos problemas
* possibilidade de um mesmo problema aparecer em diferentes listas
* exportação de listas de exercícios
* suporte a formatação em Markdown para enunciados
* estatísticas por categoria ou nível de dificuldade

---

## Objetivo do Projeto

Este projeto foi desenvolvido como parte de uma atividade individual da disciplina MAC0350 - Introdução ao Desenvolvimento de Sistemas de Software, com o objetivo de aplicar na prática os conceitos apresentados em WebMAC.

---

## Como Executar

1. Instale as dependências:

pip install -r requirements.txt

2. Execute o servidor:

uvicorn main:app --reload

3. Acesse no navegador:

http://127.0.0.1:8000

---

## Autor

Cauê Fornielles da Costa  
NUSP: 14564489