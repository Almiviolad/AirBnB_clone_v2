USE hbnb_dev_db;
CREATE TABLE place (
  id INT AUTO_INCREMENT PRIMARY KEY,
  city_id INT,
  user_id INT,
  name VARCHAR(255),
  description TEXT,
  number_rooms INT,
  number_bathrooms INT,
  max_guest INT,
  price_by_night DECIMAL(10, 2),
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6),
  amenity_ids TEXT
);

