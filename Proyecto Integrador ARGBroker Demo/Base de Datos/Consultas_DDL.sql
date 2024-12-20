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
    CONSTRAINT UC_cuil UNIQUE (cuil),
    CONSTRAINT UC_email UNIQUE (email),
    perfil ENUM('conservador', 'medio', 'agresivo') NOT NULL  -- Modificado a perfil
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

-- AGREGAR CONTRASEÑA A LA TABLA USUARIOS
ALTER TABLE Usuarios ADD COLUMN contraseña VARCHAR(20);