-- stocks
-- wildberries_timescale_stocks
-- size_items
-- goods
-- wildberries_sales
CREATE TABLE goods (
    id int4 PRIMARY KEY,
    wildberries_sku int8 NOT NULL
);

CREATE SCHEMA _test;

CREATE TABLE _test.target (id int4, wildberries_sku int8);