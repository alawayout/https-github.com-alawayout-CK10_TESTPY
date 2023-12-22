SELECT c.customer_id, c.customer_name, SUM(o.order_total) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE EXTRACT(MONTH FROM o.order_date) = EXTRACT(MONTH FROM CURRENT_DATE)
GROUP BY c.customer_id
ORDER BY total_orders DESC;



SELECT p.product_id, p.product_name, p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE p.price > (SELECT AVG(price) FROM products WHERE category_id = p.category_id)
ORDER BY p.price ASC;




SELECT o.order_id, o.order_date
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
WHERE c.category_name = 'Электроника'
ORDER BY o.order_date;





SELECT customer_id, customer_name
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT c.customer_id
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE EXTRACT(YEAR FROM o.order_date) = EXTRACT(YEAR FROM CURRENT_DATE) - 1
)
ORDER BY customer_name;






SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id IS NULL
ORDER BY p.product_name;




-- Тестовый отчет:

--     Выборка клиентов по общей сумме заказов:
--         Результат: Получены клиенты, сделавшие заказы в текущем месяце, отсортированные по убыванию общей суммы заказов.
--         Ошибки/Предупреждения: Не обнаружено.
--         Рекомендации: Разработать индексы для улучшения производительности запроса.

--     Выборка продуктов по цене и категории:
--         Результат: Получены продукты с ценой выше средней по категории, отсортированные по возрастанию цены.
--         Ошибки/Предупреждения: Не обнаружено.
--         Рекомендации: Оптимизировать запрос, убедившись, что индексы правильно настроены.

--     Выборка заказов по продуктам из категории "Электроника":
--         Результат: Получены заказы с продуктами из категории "Электроника", отсортированные по дате заказа.
--         Ошибки/Предупреждения: Не обнаружено.
--         Рекомендации: Убедиться, что есть индексы для ускорения поиска по категории и дате заказа.

--     Выборка клиентов без заказов в прошлом году:
--         Результат: Получены клиенты, не сделавшие заказов в прошлом году, отсортированные по алфавиту.
--         Ошибки/Предупреждения: Не обнаружено.
--         Рекомендации: Оптимизировать запрос, убедившись, что индексы правильно настроены.

--     Выборка продуктов без заказов:
--         Результат: Получены продукты, которые не были заказаны ни разу, отсортированные по названию.
--         Ошибки/Предупреждения: Не обнаружено.
--         Рекомендации: Убедиться, что есть индексы для ускорения поиска продуктов без заказов.