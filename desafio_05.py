# 5 - Escreva o script necessário para a criação de uma tabela chamada CLIENTES e 
# outra chamada TELEFONES. A tabela CLIENTES deverá possuir os seguintes campos: NOME, CPF e IDADE sendo o 
# CPF a chave primária.
# A tabela TELEFONES deverá possuir três campos, sendo eles: CPF_CLIENTE, DDD e TELEFONE, para esta tabela 
# o campo CPF_CLIENTE deverá ser a chave primária e estrangeira (referenciando o campo CPF da tabela CLIENTES)

CREATE TABLE CLIENTES (
    CPF CHAR(11) PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    IDADE INT NOT NULL
);

CREATE TABLE TELEFONES (
    CPF_CLIENTE CHAR(11),
    DDD CHAR(2) NOT NULL,
    TELEFONE VARCHAR(9) NOT NULL,
    PRIMARY KEY (CPF_CLIENTE, TELEFONE),
    FOREIGN KEY (CPF_CLIENTE) REFERENCES CLIENTES(CPF) ON DELETE CASCADE
);

