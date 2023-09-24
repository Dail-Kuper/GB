import pyasn1_modules.rfc6031
from django.shortcuts import render

# Create your views here.

# Я хорошо знаю SQL но не знаю как обвернуть требуемые запросы в питоне
# 1)

SELECT u.id, u.first_name, u.last_name. p.name, l.name, l.video_duration_in_sec, u_l_v.watched_seconds, u_l_v.status FROM user AS u
JOIN product_user_access AS p_u_a ON p_u_a.user_id = u.id
JOIN products AS p ON p_u_a.user_id = u.id AND p_u_a.prod_id = p.id
JOIN product_lesson AS p_l ON p_u_a.user_id = u.id AND p_u_a.prod_id = p_l.prod_id
JOIN lessons AS l ON p_u_a.user_id = u.id AND p_u_a.prod_id = p_l.prod_id AND p_l.less_id = l.id
JOIN user_lesson_views AS u_l_v ON p_u_a.user_id = u.id AND p_u_a.prod_id = p_l.prod_id AND p_l.less_id = l.id AND l.id = u_l_v.less_id
WHERE user.id = 1
ORDER BY product.name

# 2)

SELECT p.name, u.first_name, u.last_name, l.name, l.video_duration_in_sec, u_l_v.u_l_v.watched_seconds, u_l_v.status, u_l_v.date_last_update FROM products AS p
JOIN product_user_access AS p_u_a ON p_u_a.prod_id = p.id
JOIN user As u ON p_u_a ON p_u_a.prod_id = p.id AND p_u_a.user_id = u.id
JOIN product_lesson AS p_l ON p_l.prod_id = p.id
JOIN lesson AS l ON p_l.prod_id = p.id AND p_l.less_id = l.id
JOIN user_lesson_views AS u_l_v ON p_l.prod_id = p.id AND p_l.less_id = l.id AND l.id = u_l_v.less_id

WHERE products.id = 1 AND user.id = 1
ORDER BY lesson.name

# 3)

SELECT p.name, COUNT(p_l_v.status) AS times_viewed, SUM(u_l_v_2.watched_seconds) / 3600 AS hours_viewed, COUNT(p_u_a.user_id) AS users_amount, COUNT(p_u_a.user_id) / SUM(COUNT(p_u_a.user_id)) OVER() AS purchase_% FROM products AS p
JOIN product_lesson AS p_l ON p_l.prod_id = p.id
JOIN user_lesson_views AS u_l_v ON p_l.prod_id = p.id AND u_l_v.less_id = p_l.less_id AND u_l_v.status = True
JOIN user_lesson_views AS u_l_v_2 ON p_l.prod_id = p.id AND u_l_v_2.less_id = p_l.less_id
JOIN product_user_access AS p_u_a ON p_u_a.prod_id = p.id

GROUP BY p.name
ORDER BY purchase_%
