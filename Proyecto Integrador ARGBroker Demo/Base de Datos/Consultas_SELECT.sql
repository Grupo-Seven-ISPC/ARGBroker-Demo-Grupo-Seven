-- Consultas tipo SELECT
-- 1.Seleccionar simbolo y cantidad de acciones
SELECT simbolo, cantidad FROM Accion;

-- 2.Mostrar apellido y nombre de los usuarios
SELECT apellido, nombre FROM Usuarios;

-- 3.Mostrar símbolo de las 3 acciones con menor cantidad en stock
SELECT simbolo FROM Accion 
ORDER BY cantidad ASC LIMIT 3;

-- 4.Mostrar primeras 10 operaciones realizadas
SELECT * FROM Operacion
ORDER BY fecha ASC LIMIT 10;

-- 5.Mostrar las operaciones con volúmenes operados menores a 10 acciones
SELECT * FROM Operacion
WHERE cantidad < 10;
