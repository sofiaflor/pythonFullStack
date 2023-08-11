INSERT INTO twitter.users
(id,
first_name,
last_name,
handle,
birthday,
created_at,
updated_at)
VALUES
(<{id: }>,
<{first_name: }>,
<{last_name: }>,
<{handle: }>,
<{birthday: }>,
<{created_at: }>,
<{updated_at: }>);


UPDATE twitter.users
SET
id = <{id: }>,
first_name = <{first_name: }>,
last_name = <{last_name: }>,
handle = <{handle: }>,
birthday = <{birthday: }>,
created_at = <{created_at: }>,
updated_at = <{updated_at: }>
WHERE id = <{expr}>;

DELETE FROM twitter.users
WHERE <{where_expression}>;



SELECT users.id,
    users.first_name,
    users.last_name,
    users.handle,
    users.birthday,
    users.created_at,
    users.updated_at
FROM twitter.users;



