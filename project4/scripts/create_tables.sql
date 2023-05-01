USE project4database;

CREATE TABLE IF NOT EXISTS GolfCartData(
    GolfCartID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    price VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phoneNum VARCHAR(100) NOT NULL, 
    curr_condition VARCHAR(100) NOT NULL, 
    make_model VARCHAR(100) NOT NULL, 
    year_built VARCHAR(100) NOT NULL, 
    color VARCHAR(100) NOT NULL, 
    fuel_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (GolfCartID)
);

CREATE TABLE IF NOT EXISTS BikeData(
    BikeID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    price VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phoneNum VARCHAR(100) NOT NULL, 
    bike_type VARCHAR(100) NOT NULL, 
    color VARCHAR(100) NOT NULL, 
    PRIMARY KEY (BikeID)
);

CREATE TABLE IF NOT EXISTS BoatData(
    BoatID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    price VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phoneNum VARCHAR(100) NOT NULL, 
    boat_length VARCHAR(100) NOT NULL, 
    make_model VARCHAR(100) NOT NULL, 
    year_built VARCHAR(100) NOT NULL, 
    boat_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (BoatID)
);

CREATE TABLE IF NOT EXISTS CellPhoneData(
    CellPhoneID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    price VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phoneNum VARCHAR(100) NOT NULL, 
    manufacturer VARCHAR(100) NOT NULL, 
    model VARCHAR(100) NOT NULL, 
    memory VARCHAR(100) NOT NULL, 
    PRIMARY KEY (CellPhoneID)
);

CREATE TABLE IF NOT EXISTS FurnitureData (
    FurnitureID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    price VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phoneNum VARCHAR(100) NOT NULL, 
    brand VARCHAR(100) NOT NULL, 
    furniture_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (FurnitureID)
);