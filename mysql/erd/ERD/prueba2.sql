select sum(round((oi.quantity * oi.list_price) * oi.discount , 0) ) as total,
s.store_name
from orders as o
left join order_items as oi
on oi.order_id = o.order_id
left join stores as s
on s.store_id = o.store_id
where
year(o.order_date) =  2018
and month(o.order_date) = 4
group by s.store_name
order by total desc;

select * from brands limit 5;
select * from categories limit 5;
select * from customers limit 5;
select * from order_items limit 5;
select * from orders limit 5;
select * from products limit 5;
select * from staffs limit 5;
select * from stocks limit 5;
select * from stores limit 5;