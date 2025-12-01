-- estudiantes.sql
-- Script para crear la tabla Estudiantes e insertar datos de ejemplo.

DROP TABLE IF EXISTS Estudiantes;

CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar datos de ejemplo
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Juan', 20, 'Bogotá');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Ana', 22, 'Medellín');
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES ('Luis', 19, 'Cali');

-- Consultas básicas
-- 1) Mostrar todos los registros
SELECT * FROM Estudiantes;

-- 2) Filtrar por ciudad (ejemplo: Medellín)
SELECT * FROM Estudiantes WHERE ciudad = 'Medellín';

-- 3) Consultar estudiantes mayores de 20 años
SELECT * FROM Estudiantes WHERE edad > 20;
