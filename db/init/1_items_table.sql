DROP TABLE IF EXISTS items;
CREATE TABLE items (
  id int NOT NULL AUTO_INCREMENT,
  item_name varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  item_count int unsigned NOT NULL,
  PRIMARY KEY (id)
)
