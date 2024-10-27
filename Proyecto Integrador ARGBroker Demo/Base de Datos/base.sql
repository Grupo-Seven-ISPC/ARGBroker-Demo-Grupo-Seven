-- Crear la base de datos argbroker
CREATE DATABASE argbroker;

-- Usar la base de datos argbroker
USE argbroker;

-- Tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    cuil VARCHAR(20),
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100),
    CONSTRAINT UC_cuit UNIQUE (cuit),
    CONSTRAINT UC_email UNIQUE (email)
    perfil ENUM('conservador', 'medio', 'agresivo') NOT NULL,  -- Modificado a perfil
);

-- Tabla Accion
CREATE TABLE Accion (
    id_accion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    simbolo VARCHAR(10) NOT NULL,
    cantidad INT DEFAULT 500,
    CONSTRAINT UC_simbolo UNIQUE (simbolo)
);

-- Tabla Estado
CREATE TABLE Estado (
    id_estado INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(50) NOT NULL
);

-- Tabla Operacion
CREATE TABLE Operacion (
    id_operacion INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    id_estado INT NOT NULL,  -- Referencia a la tabla Estado
    id_usuario INT NOT NULL,
    id_accion INT NOT NULL,
    cantidad INT NOT NULL,
    tipo ENUM('compra', 'venta') NOT NULL,
    precio_unit DECIMAL(10, 2),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion),
    FOREIGN KEY (id_estado) REFERENCES Estado(id_estado)
);

-- Tabla Movimiento
CREATE TABLE Movimiento (
    ID_movimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(15, 2) CHECK (monto <> 0),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);



-- IMPLEMENTAR VER SALDO ACTUAL
INSERT INTO Movimiento (id_usuario, fecha, monto) VALUES (1,'2024-10-13', 1000000);
INSERT INTO Movimiento (id_usuario, fecha, monto) VALUES (1,'2024-10-13', -100445);

SELECT COALESCE(SUM(m.monto),0) + COALESCE(SUM(CASE WHEN o.tipo = 'compra' THEN -o.cantidad * o.precio_unit WHEN o.tipo = 'venta' THEN o.cantidad * o.precio_unit END) ,0) AS BalanceTotal
FROM Movimiento m 
LEFT JOIN Operacion o 
ON m.id_usuario = o.id_usuario 
WHERE m.id_usuario = 1 
GROUP BY m.id_usuario

ALTER TABLE Usuarios ADD COLUMN contraseña VARCHAR(20)

SELECT NOW();

SELECT COALESCE(SUM(m.monto),0) + COALESCE(SUM(CASE WHEN o.tipo = 'compra' THEN -o.cantidad * o.precio_unit WHEN o.tipo = 'venta' THEN o.cantidad * o.precio_unit END) ,0) AS BalanceTotal
            FROM Movimiento m 
            LEFT JOIN Operacion o 
            ON m.id_usuario = o.id_usuario 
            WHERE m.id_usuario = 4
            GROUP BY m.id_usuario;

UPDATE Usuarios SET contraseña = "Argentina123" WHERE id_usuario = 1 ;
UPDATE Usuarios SET contraseña = "Banquito123" WHERE ID_USUARIO = 2
UPDATE Usuarios SET email = "lalalamail@gmail.com" WHERE id_usuario = 3

CREATE table Cotizaciones (
id_accion INT NOT NULL,
dia DATE,
precio_compra INT NOT NULL,
precio_venta INT NOT NULL,
FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);

INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Aluar", "ALUA", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("BBVA", "BBAR", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Banco Macro","BMA", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Bolsas y Mercados Argentinos S.A","BYMA", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Central Puerto S.A", "CEPU", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Sociedad Comercial del Plata", "COME", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Cresud", "CRES", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Cablevision Holding S.A", "CVH", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Edenor", "EDN", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Grupo Financiero Galicia S.A", "GGAL", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Holcim Argentina", "HARG", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Loma Negra Compañia Industrial Argentina S.A", "LOMA", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Mirgor", "MIRG", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Pampa Energía", "PAMP", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Grupo Supervielle S.A", "SUPV", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Telecom Argentina", "TECO2", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Transportadora Gas del Norte", "TGN04", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Transportadora Gas del Sur", "TGSU2", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Transener", "TRAN", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Ternium Argentina S.A", "TXAR", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("Banco de Valores S.A", "VALO", 50000);
INSERT INTO Accion (nombre, simbolo, cantidad) VALUES ("YPF", "YPFD", 50000);


INSERT INTO Estado (estado) VALUES ("Operado")
INSERT INTO Estado (estado) VALUES ("Cancelado")
INSERT INTO Estado (estado) VALUES ("Pendiente")
