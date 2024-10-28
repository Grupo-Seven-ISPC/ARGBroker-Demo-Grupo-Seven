-- INSERTAR USUARIOS EJEMPLO
INSERT INTO Usuarios (cuit, nombre, apellido, email, perfil, contraseña) 
VALUES ('20-12345678-9', 'Juan', 'Pérez', 'juan.perez@example.com', 'medio', 'contraseña123');
INSERT INTO Usuarios (cuit, nombre, apellido, email, perfil, contraseña) 
VALUES 
('20-98765432-1', 'Ana', 'Gómez', 'ana.gomez@example.com', 'agresivo', 'contraseña456'),
('20-11223344-5', 'Carlos', 'Lopez', 'carlos.lopez@example.com', 'conservador', 'contraseña789'),
('20-22334455-2', 'María', 'Fernández', 'maria.fernandez@example.com', 'medio', 'contraseña321'),
('20-33445566-3', 'Pedro', 'Martínez', 'pedro.martinez@example.com', 'agresivo', 'contraseña654');

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

INSERT INTO Estado (estado) VALUES ("Operado");
INSERT INTO Estado (estado) VALUES ("Cancelado");
INSERT INTO Estado (estado) VALUES ("Pendiente");

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-15', 1, 1, 3, 85, 'compra', 54.73);
UPDATE Accion SET cantidad = cantidad - 85 WHERE id_accion = 3;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-10', 1, 1, 7, 142, 'compra', 88.29);
UPDATE Accion SET cantidad = cantidad - 142 WHERE id_accion = 7;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-28', 1, 1, 10, 69, 'compra', 77.14);
UPDATE Accion SET cantidad = cantidad - 69 WHERE id_accion = 10;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-05', 1, 1, 1, 52, 'compra', 22.39);
UPDATE Accion SET cantidad = cantidad - 52 WHERE id_accion = 1;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-20', 1, 1, 5, 94, 'compra', 43.59);
UPDATE Accion SET cantidad = cantidad - 94 WHERE id_accion = 5;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-18', 1, 1, 12, 117, 'compra', 64.51);
UPDATE Accion SET cantidad = cantidad - 117 WHERE id_accion = 12;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-03', 1, 1, 14, 76, 'compra', 58.24);
UPDATE Accion SET cantidad = cantidad - 76 WHERE id_accion = 14;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-24', 1, 1, 8, 100, 'compra', 32.67);
UPDATE Accion SET cantidad = cantidad - 100 WHERE id_accion = 8;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-30', 1, 1, 2, 33, 'compra', 44.88);
UPDATE Accion SET cantidad = cantidad - 33 WHERE id_accion = 2;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-25', 1, 1, 11, 97, 'compra', 52.19);
UPDATE Accion SET cantidad = cantidad - 97 WHERE id_accion = 11;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-12', 1, 1, 4, 47, 'compra', 88.65);
UPDATE Accion SET cantidad = cantidad - 47 WHERE id_accion = 4;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-27', 1, 1, 9, 115, 'compra', 72.34);
UPDATE Accion SET cantidad = cantidad - 115 WHERE id_accion = 9;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-10', 1, 1, 6, 58, 'compra', 89.12);
UPDATE Accion SET cantidad = cantidad - 58 WHERE id_accion = 6;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-22', 1, 1, 15, 25, 'compra', 63.11);
UPDATE Accion SET cantidad = cantidad - 25 WHERE id_accion = 15;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-15', 1, 1, 3, 79, 'compra', 37.75);
UPDATE Accion SET cantidad = cantidad - 79 WHERE id_accion = 3;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-13', 1, 1, 13, 112, 'compra', 90.67);
UPDATE Accion SET cantidad = cantidad - 112 WHERE id_accion = 13;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-20', 1, 1, 1, 38, 'compra', 24.20);
UPDATE Accion SET cantidad = cantidad - 38 WHERE id_accion = 1;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-15', 1, 1, 5, 44, 'compra', 59.00);
UPDATE Accion SET cantidad = cantidad - 44 WHERE id_accion = 5;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-08', 1, 1, 14, 67, 'compra', 41.73);
UPDATE Accion SET cantidad = cantidad - 67 WHERE id_accion = 14;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-28', 1, 1, 10, 52, 'compra', 29.88);
UPDATE Accion SET cantidad = cantidad - 52 WHERE id_accion = 10;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-17', 1, 1, 2, 33, 'compra', 74.43);
UPDATE Accion SET cantidad = cantidad - 33 WHERE id_accion = 2;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-31', 1, 1, 8, 78, 'compra', 11.90);
UPDATE Accion SET cantidad = cantidad - 78 WHERE id_accion = 8;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-23', 1, 1, 4, 111, 'compra', 56.33);
UPDATE Accion SET cantidad = cantidad - 111 WHERE id_accion = 4;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-12', 1, 1, 7, 63, 'compra', 67.54);
UPDATE Accion SET cantidad = cantidad - 63 WHERE id_accion = 7;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-05', 1, 1, 3, 90, 'compra', 48.36);
UPDATE Accion SET cantidad = cantidad - 90 WHERE id_accion = 3;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-11', 1, 1, 6, 35, 'compra', 30.20);
UPDATE Accion SET cantidad = cantidad - 35 WHERE id_accion = 6;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-21', 1, 1, 9, 55, 'compra', 79.81);
UPDATE Accion SET cantidad = cantidad - 55 WHERE id_accion = 9;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-04', 1, 1, 11, 112, 'compra', 23.75);
UPDATE Accion SET cantidad = cantidad - 112 WHERE id_accion = 11;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-24', 1, 1, 12, 66, 'compra', 95.88);
UPDATE Accion SET cantidad = cantidad - 66 WHERE id_accion = 12;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-17', 1, 1, 2, 41, 'compra', 16.65);
UPDATE Accion SET cantidad = cantidad - 41 WHERE id_accion = 2;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-29', 1, 1, 8, 95, 'compra', 25.01);
UPDATE Accion SET cantidad = cantidad - 95 WHERE id_accion = 8;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-08', 1, 1, 15, 57, 'compra', 82.44);
UPDATE Accion SET cantidad = cantidad - 57 WHERE id_accion = 15;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-07', 1, 1, 1, 45, 'compra', 45.01);
UPDATE Accion SET cantidad = cantidad - 45 WHERE id_accion = 1;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-19', 1, 1, 10, 88, 'compra', 74.25);
UPDATE Accion SET cantidad = cantidad - 88 WHERE id_accion = 10;

-- Operaciones de venta

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-20', 1, 1, 2, 75, 'venta', 59.73);
UPDATE Accion SET cantidad = cantidad + 75 WHERE id_accion = 2;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-22', 1, 1, 6, 98, 'venta', 48.29);
UPDATE Accion SET cantidad = cantidad + 98 WHERE id_accion = 6;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-16', 1, 1, 9, 123, 'venta', 37.14);
UPDATE Accion SET cantidad = cantidad + 123 WHERE id_accion = 9;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-29', 1, 1, 11, 54, 'venta', 89.39);
UPDATE Accion SET cantidad = cantidad + 54 WHERE id_accion = 11;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-11', 1, 1, 3, 66, 'venta', 44.59);
UPDATE Accion SET cantidad = cantidad + 66 WHERE id_accion = 3;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-05', 1, 1, 10, 34, 'venta', 61.72);
UPDATE Accion SET cantidad = cantidad + 34 WHERE id_accion = 10;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-14', 1, 1, 14, 91, 'venta', 79.17);
UPDATE Accion SET cantidad = cantidad + 91 WHERE id_accion = 14;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-22', 1, 1, 8, 64, 'venta', 53.11);
UPDATE Accion SET cantidad = cantidad + 64 WHERE id_accion = 8;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-18', 1, 1, 1, 88, 'venta', 78.34);
UPDATE Accion SET cantidad = cantidad + 88 WHERE id_accion = 1;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-26', 1, 1, 4, 45, 'venta', 67.53);
UPDATE Accion SET cantidad = cantidad + 45 WHERE id_accion = 4;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-09', 1, 1, 12, 60, 'venta', 90.25);
UPDATE Accion SET cantidad = cantidad + 60 WHERE id_accion = 12;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-01', 1, 1, 15, 50, 'venta', 12.18);
UPDATE Accion SET cantidad = cantidad + 50 WHERE id_accion = 15;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-03', 1, 1, 5, 47, 'venta', 29.88);
UPDATE Accion SET cantidad = cantidad + 47 WHERE id_accion = 5;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-07', 1, 1, 7, 112, 'venta', 82.56);
UPDATE Accion SET cantidad = cantidad + 112 WHERE id_accion = 7;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-30', 1, 1, 2, 71, 'venta', 68.49);
UPDATE Accion SET cantidad = cantidad + 71 WHERE id_accion = 2;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-01', 1, 1, 11, 59, 'venta', 21.39);
UPDATE Accion SET cantidad = cantidad + 59 WHERE id_accion = 11;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-25', 1, 1, 3, 102, 'venta', 39.19);
UPDATE Accion SET cantidad = cantidad + 102 WHERE id_accion = 3;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-10', 1, 1, 9, 85, 'venta', 11.50);
UPDATE Accion SET cantidad = cantidad + 85 WHERE id_accion = 9;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-03-09', 1, 1, 6, 38, 'venta', 44.21);
UPDATE Accion SET cantidad = cantidad + 38 WHERE id_accion = 6;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-17', 1, 1, 8, 24, 'venta', 52.78);
UPDATE Accion SET cantidad = cantidad + 24 WHERE id_accion = 8;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-02-19', 1, 1, 1, 33, 'venta', 77.29);
UPDATE Accion SET cantidad = cantidad + 33 WHERE id_accion = 1;

INSERT INTO Operacion (fecha, id_estado, id_usuario, id_accion, cantidad, tipo, precio_unit) VALUES ('2024-01-26', 1, 1, 4, 66, 'venta', 30.59);
UPDATE Accion SET cantidad = cantidad + 66 WHERE id_accion = 4;