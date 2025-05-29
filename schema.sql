CREATE TABLE IF NOT EXISTS pet 
( 
 ID INTEGER PRIMARY KEY,  
 nome TEXT NOT NULL,  
 sexo TEXT,  
 data_nascimento TEXT NOT NULL,  
 data_adocao TEXT NOT NULL,  
 raca TEXT NOT NULL DEFAULT 'vira-lata',  
 cor TEXT NOT NULL,  
 alergias TEXT,  
 idmedicamentos INTEGER,
 idhistorico_consultas INTEGER,
 idvacinas INTEGER,
 iddieta INTEGER,
 FOREIGN KEY(idmedicamentos) REFERENCES medicamentos(ID),
 FOREIGN KEY(idhistorico_consultas) REFERENCES historico_consultas(ID),
 FOREIGN KEY(idvacinas) REFERENCES vacinas(ID),
 FOREIGN KEY(iddieta) REFERENCES dieta(ID)
); 

CREATE TABLE usuario 
( 
 ID INTEGER PRIMARY KEY,  
 nome TEXT NOT NULL,  
 sobrenome TEXT NOT NULL,  
 email TEXT NOT NULL,  
 senha TEXT NOT NULL,  
 descricao TEXT  
); 

CREATE TABLE pet_usuario 
( 
 ID_pet_usuario INTEGER PRIMARY KEY,  
 idpet INTEGER,  
 idusuario INTEGER,
 FOREIGN KEY(idpet) REFERENCES pet(ID),
 FOREIGN KEY(idusuario) REFERENCES usuario(ID)
); 

CREATE TABLE historico_consultas 
( 
 ID INTEGER PRIMARY KEY,  
 data_consulta TEXT NOT NULL,  
 hora_consulta TEXT NOT NULL  
); 

CREATE TABLE vacinas 
( 
 ID INTEGER PRIMARY KEY,  
 nome TEXT,  
 data_vacina TEXT NOT NULL,  
 tipo_vacina TEXT NOT NULL,  
 observacao TEXT  
); 

CREATE TABLE medicamentos 
( 
 ID INTEGER PRIMARY KEY,  
 nome TEXT NOT NULL  
); 

CREATE TABLE agenda 
( 
 ID INTEGER PRIMARY KEY,  
 nome TEXT NOT NULL,  
 dia_atividade TEXT NOT NULL,  
 hora_atividade TEXT NOT NULL,  
 completado INTEGER NOT NULL DEFAULT 0,  
 observacao TEXT,  
 CHECK (completado IN (0, 1))
); 

CREATE TABLE agenda_pet_usuario 
( 
 ID INTEGER PRIMARY KEY,  
 idagenda INTEGER,  
 idpet_usuario INTEGER,
 FOREIGN KEY(idagenda) REFERENCES agenda(ID),
 FOREIGN KEY(idpet_usuario) REFERENCES pet_usuario(ID_pet_usuario)
); 

CREATE TABLE dieta 
( 
 ID INTEGER PRIMARY KEY,  
 nome_refeicao TEXT NOT NULL,  
 hora_refeicao TEXT NOT NULL,  
 alimentado INTEGER DEFAULT 0,  
 CHECK (alimentado IN (0, 1))
); 
