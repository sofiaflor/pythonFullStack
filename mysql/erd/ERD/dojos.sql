use asignaciones;
select *
from dojos;

INSERT INTO asignaciones.dojos
(id,
name,
created_at,
updated_at)
VALUES
(1,
'vale',
now(),
now());

INSERT INTO asignaciones.dojos
(id,
name,
created_at,
updated_at)
VALUES
(2,
'sofi',
now(),
now());
INSERT INTO asignaciones.dojos
(id,
name,
created_at,
updated_at)
VALUES
(3,
'say',
now(),
now());

DELETE FROM asignaciones.dojos
WHERE dojos.id= 1;

DELETE FROM asignaciones.dojos
WHERE dojos.id= 2;

DELETE FROM asignaciones.dojos
WHERE dojos.id= 3;

INSERT INTO asignaciones.dojos
(id,
name,
created_at,
updated_at)
VALUES
(1,'vale',now(),now()),
(2,'sofi',now(),now()),
(3,'say',now(),now());
 
select * from ninjas;
INSERT INTO asignaciones.ninjas
(id,
first_name,
last_name,
age,
dojos_id,
created_at,
updated_at)
VALUES
(1,'tuki','monroy', 150, 1 , now(), now()),
(2,'pocky','monroy', 250, 1 , now(), now()),
(3,'brocky','monroy', 10, 1 , now(), now());

INSERT INTO asignaciones.ninjas
(id,
first_name,
last_name,
age,
dojos_id,
created_at,
updated_at)

VALUES
(4,'tilin','castillo', 6, 2 , now(), now()),
(5,'pocoyo','castillo',15, 2 , now(), now()),
(6,'lucas','castillo', 60, 2 , now(), now());

INSERT INTO asignaciones.ninjas
(id,
first_name,
last_name,
age,
dojos_id,
created_at,
updated_at)

VALUES
(7,'carlitos','castillo', 3, 3 , now(), now()),
(8,'toby','castillo', 15, 3 , now(), now()),
(9,'angelica','castillo', 10, 3, now(), now());

SELECT * FROM dojos
WHERE id = 1;


