-- Consultas multitablas
-- 1.Se solicita mostrar los usuarios (id, nombre y apellido) que realizaron operaciones con Mirgor

SELECT u.id_usuario, u.nombre, u.apellido 
FROM Usuarios u 
JOIN (
    SELECT a.nombre, o.id_usuario, o.fecha, o.cantidad, o.tipo, o.precio_unit
    FROM Operacion o
    JOIN Accion a ON o.id_accion = a.id_accion
    WHERE a.nombre = 'Mirgor'
) sc ON u.id_usuario = sc.id_usuario;

-- 2.Se solicita mostrar los usuarios (nombre y apellido) con operaciones pendientes

SELECT u.nombre, u.apellido 
FROM Usuarios u 
JOIN (
    SELECT o.id_usuario, e.estado 
    FROM Operacion o 
    JOIN Estado e ON o.id_estado = e.id_estado 
    WHERE e.estado = 'pendiente'
) sc ON u.id_usuario = sc.id_usuario;

-- 3.Se solicita mostrar las 3 acciones (símbolo y total de operaciones) con más operaciones

SELECT a.simbolo, COUNT(o.id_operacion) AS total_operaciones
FROM Operacion o
JOIN Accion a ON o.id_accion = a.id_accion
GROUP BY a.simbolo
ORDER BY total_operaciones DESC
LIMIT 3;

