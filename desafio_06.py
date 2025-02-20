# 6 - Escreva uma consulta SQL para obter o nome de todos os clientes que possuam idade igual ou superior a 22 anos. 
# O resultado deverá estar ordenado pela idade de forma crescente.
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

SELECT NOME FROM CLIENTES WHERE IDADE >= 22 ORDER BY IDADE ASC;