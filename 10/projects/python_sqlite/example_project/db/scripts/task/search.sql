SELECT
    id,
    name,
    description,
    completed
FROM task
WHERE (name LIKE '%' || ? || '%') OR (description LIKE '%' || ? || '%');
