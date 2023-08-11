Use asignaciones;
select *
from usuarios;
INSERT INTO asignaciones.usuarios
(id,
first_name,
last_name,
email,
created_at,
updated_at)
VALUES
(4,
'ale',
'tamblay',
'ale@gmail.com',
now(),
now());

INSERT INTO asignaciones.usuarios
(id,
first_name,
last_name,
email,
created_at,
updated_at)0
VALUES
(5,
'catalina',
'rivas',
'cata@gmail',
now(),
now());

INSERT INTO asignaciones.usuarios
(id,
first_name,
last_name,
email,
created_at,
updated_at)
VALUES
(6,
'saygrid',
'martinez',
'say@gmail',
now(),
now());

SELECT * FROM usuarios
WHERE email = 'sofia@arias.cl';

SELECT * FROM usuarios
WHERE id = 10;

UPDATE usuarios SET last_name = "panqueques"
WHERE usuarios.id = 3;

DELETE FROM usuarios
WHERE usuarios.id = 2;

select *
from usuarios
order by first_name asc;

select *
from usuarios
order by first_name desc;

