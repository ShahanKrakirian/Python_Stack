USE Friendships;

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Chris', 'Baker', NOW(),NOW()), ('Diana', 'Smith', NOW(),NOW()), ('James', 'Johnson', NOW(),NOW()), ('Jessica', 'Davidson', NOW(),NOW());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (7, 10, NOW(),NOW()), (7, 9, NOW(),NOW()), (7, 8, NOW(),NOW());

INSERT INTO friendships(user_id, friend_id, created_at, updated_at)
VALUES (8, 7, NOW(),NOW()), (9, 7, NOW(),NOW()), (10, 7, NOW(), NOW());

SELECT user2.first_name AS first_name, user2.last_name AS last_name, users.first_name AS friend_first_name, users.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.friend_id
LEFT JOIN users as user2 ON user2.id = friendships.user_id
ORDER BY user2.id;
