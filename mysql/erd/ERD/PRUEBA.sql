/*SELECT list_price * 0.9 AS precio_con_descuento
FROM products
WHERE model_year = 2018;


SELECT list_price * 0.8 AS precio_con_descuento
FROM products
WHERE model_year = 2017;

SELECT list_price * 0.75 AS precio_con_descuento
FROM products
WHERE model_year = 2016;*/


SELECT product_id,product_name, brand_id, category_id, model_year, 
round(list_price,0),
       round(CASE
           WHEN model_year= 2018 THEN list_price * 0.9 -- 10% de descuento
           WHEN model_year= 2017 THEN list_price * 0.8 -- 20% de descuento
           WHEN model_year= 2016 THEN list_price * 0.75 -- 25% de descuento
           ELSE list_price
       END ,0) AS precio_con_descuento
FROM products;
