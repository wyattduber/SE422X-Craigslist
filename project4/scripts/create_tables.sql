USE project4database;

/* Community */

CREATE TABLE IF NOT EXISTS ActivitiesData(
    ActivityID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    age_group VARCHAR(100) NOT NULL, 
    time_date VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    capacity VARCHAR(100) NOT NULL, 
    PRIMARY KEY (ActivityID)
);

CREATE TABLE IF NOT EXISTS PerformersData(
    PerformerID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    performer_name VARCHAR(100) NOT NULL, 
    genre VARCHAR(100) NOT NULL, 
    show_time VARCHAR(100) NOT NULL, 
    age_rating VARCHAR(100) NOT NULL, 
    PRIMARY KEY (PerformerID)
);

CREATE TABLE IF NOT EXISTS ChildCareData(
    ChildCareID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    open_hours VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    childcare_name VARCHAR(100) NOT NULL, 
    capacity VARCHAR(100) NOT NULL, 
    PRIMARY KEY (ChildCareID)
);

CREATE TABLE IF NOT EXISTS RideshareData(
    RideshareID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    pickup_location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    date_time VARCHAR(100) NOT NULL, 
    dropoff_location VARCHAR(100) NOT NULL, 
    pay VARCHAR(100) NOT NULL, 
    people VARCHAR(100) NOT NULL, 
    PRIMARY KEY (RideshareID)
);

CREATE TABLE IF NOT EXISTS ClubsData(
    ClubID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    session_hours VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    club_name VARCHAR(100) NOT NULL, 
    capacity VARCHAR(100) NOT NULL, 
    PRIMARY KEY (ClubID)
);

/* For Sale */

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
    phone_num VARCHAR(100) NOT NULL, 
    brand VARCHAR(100) NOT NULL, 
    furniture_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (FurnitureID)
);

/* Housing */

CREATE TABLE IF NOT EXISTS ApartmentData (
    ApartmentID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    rent VARCHAR(100) NOT NULL, 
    square_feet VARCHAR(100) NOT NULL, 
    num_bathrooms VARCHAR(100) NOT NULL, 
    num_bedrooms VARCHAR(100) NOT NULL, 
    pets VARCHAR(100) NOT NULL,
    laundry VARCHAR(100) NOT NULL,
    PRIMARY KEY (ApartmentID)
);

CREATE TABLE IF NOT EXISTS OfficesData (
    OfficesID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    rent VARCHAR(100) NOT NULL, 
    square_feet VARCHAR(100) NOT NULL, 
    num_rooms VARCHAR(100) NOT NULL, 
    PRIMARY KEY (OfficesID)
);

CREATE TABLE IF NOT EXISTS RoomsData (
    RoomsID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    rent VARCHAR(100) NOT NULL, 
    square_feet VARCHAR(100) NOT NULL, 
    PRIMARY KEY (RoomsID)
);

CREATE TABLE IF NOT EXISTS RealEstateData (
    RealEstateID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    acreage VARCHAR(100) NOT NULL, 
    type VARCHAR(100) NOT NULL, 
    rooms VARCHAR(100) NOT NULL, 
    PRIMARY KEY (RealEstateID)
);

CREATE TABLE IF NOT EXISTS VacationData (
    VacationID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost_per_night VARCHAR(100) NOT NULL, 
    num_beds VARCHAR(100) NOT NULL, 
    pool VARCHAR(100) NOT NULL, 
    firepit VARCHAR(100) NOT NULL, 
    PRIMARY KEY (VacationID)
);

/* Jobs */

CREATE TABLE IF NOT EXISTS HealthcareData (
    HealthcareID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    salary VARCHAR(100) NOT NULL, 
    experience VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    employer VARCHAR(100) NOT NULL, 
    PRIMARY KEY (HealthcareID)
);

CREATE TABLE IF NOT EXISTS EngineeringData (
    EngineeringID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    salary VARCHAR(100) NOT NULL, 
    experience VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    employer VARCHAR(100) NOT NULL, 
    PRIMARY KEY (EngineeringID)
);

CREATE TABLE IF NOT EXISTS EducationData (
    EducationID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    salary VARCHAR(100) NOT NULL, 
    experience VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    employer VARCHAR(100) NOT NULL, 
    PRIMARY KEY (EducationID)
);

CREATE TABLE IF NOT EXISTS TransportationData (
    TransportationID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    salary VARCHAR(100) NOT NULL, 
    experience VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    employer VARCHAR(100) NOT NULL, 
    PRIMARY KEY (TransportationID)
);

CREATE TABLE IF NOT EXISTS FinanceData (
    FinanceID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    salary VARCHAR(100) NOT NULL, 
    experience VARCHAR(100) NOT NULL, 
    title VARCHAR(100) NOT NULL, 
    employer VARCHAR(100) NOT NULL, 
    PRIMARY KEY (FinanceID)
);

/* Services */

CREATE TABLE IF NOT EXISTS LawnData (
    LawnID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    operating_hours VARCHAR(100) NOT NULL, 
    company_name VARCHAR(100) NOT NULL, 
    service_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (LawnID)
);

CREATE TABLE IF NOT EXISTS PhoneData (
    PhoneID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    operating_hours VARCHAR(100) NOT NULL, 
    company_name VARCHAR(100) NOT NULL, 
    repair_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (PhoneID)
);

CREATE TABLE IF NOT EXISTS PlumbingData (
    PlumbingID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    operating_hours VARCHAR(100) NOT NULL, 
    company_name VARCHAR(100) NOT NULL, 
    repair_type VARCHAR(100) NOT NULL, 
    PRIMARY KEY (PlumbingID)
);

CREATE TABLE IF NOT EXISTS InternetData (
    InternetID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    operating_hours VARCHAR(100) NOT NULL, 
    company_name VARCHAR(100) NOT NULL, 
    speed VARCHAR(100) NOT NULL, 
    PRIMARY KEY (InternetID)
);

CREATE TABLE IF NOT EXISTS PaintingData (
    PaintingID MEDIUMINT NOT NULL AUTO_INCREMENT, 
    creation_time VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL, 
    phone_num VARCHAR(100) NOT NULL, 
    cost VARCHAR(100) NOT NULL, 
    operating_hours VARCHAR(100) NOT NULL, 
    company_name VARCHAR(100) NOT NULL, 
    color VARCHAR(100) NOT NULL, 
    PRIMARY KEY (PaintingID)
);