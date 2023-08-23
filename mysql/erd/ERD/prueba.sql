SELECT product_id,product_name, brand_id, category_id, model_year, 
round(list_price,0),
       round(CASE  /*redondea el precio*/
           WHEN model_year= 2018 THEN list_price * 0.9 -- 10% de descuento  
           WHEN model_year= 2017 THEN list_price * 0.8 -- 20% de descuento
           WHEN model_year= 2016 THEN list_price * 0.75 -- 25% de descuento
           ELSE list_price
       END ,0) AS precio_con_descuento
FROM products;

(select year(o.order_date) as periodo ,s.store_name, concat(s.street,' ', s.city,' ',s.state) as direccion, count(o.order_id) as cantidad_ventas,
/*Se seleccionan y se le cambian los nombres a las columnas*/
sum(oi.list_price * oi.quantity) as ventas_total, /*Se crea la columna ventas total que se conformada por la multiplicacion y la suma de oi.list_price con oi.quantity*/
avg(oi.list_price * oi.quantity) as promedio_ventas,/*se crea el promedio de ventas con los valores anteriores pero en vez de sumarlo se le aplica el avg*/
sum(oi.quantity) as total_productos/*se crea la columna total_productos*/
from order_items as oi/*se le asigna un alias a order_items que sera oi*/
left join orders as o on o.order_id = oi.order_id/*se concatena las columna o.order_id con orders y se le asigna el alias de oi.order_id*/
left join stores as s on s.store_id = o.store_id/*se concatena las columna stores con s.stores_id y se le asigna el alias de o.store_id*/
where year(order_date) =2017/*se consulta que el año sea 2017*/
group by s.store_id
order by ventas_total asc
limit 1)
/*Se selecciona el valor mayor de las ventas del 2017*/
union  /*Se unen las tablas*/
(select year(o.order_date) as periodo ,s.store_name, concat(s.street,' ', s.city,' ',s.state) as direccion, count(o.order_id) as cantidad_ventas,
sum(oi.list_price * oi.quantity) as ventas_total,
avg(oi.list_price * oi.quantity) as promedio_ventas,
sum(oi.quantity) as total_productos
from order_items as oi
left join orders as o on o.order_id = oi.order_id
left join stores as s on s.store_id = o.store_id
where year(order_date) =2017
group by s.store_id
order by ventas_total desc
limit 1)
/*Se selecciona el valor menor de las ventas del 2017*/




