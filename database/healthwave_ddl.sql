CREATE TABLE doctors (
    doctor_id VARCHAR(10) PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    hospital VARCHAR(100)
);

CREATE TABLE user (
    user_id VARCHAR(10) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    blood_group VARCHAR(5),
    gender ENUM('Male', 'Female', 'Other'),
    age INT,
    allergies TEXT,
    health_insurance VARCHAR(50),
    medical_history TEXT,
    treatment_plan TEXT,
    doctor_1 VARCHAR(10),
    doctor_2 VARCHAR(10),
    doctor_3 VARCHAR(10),
    FOREIGN KEY (doctor_1) REFERENCES doctors(doctor_id),
    FOREIGN KEY (doctor_2) REFERENCES doctors(doctor_id),
    FOREIGN KEY (doctor_3) REFERENCES doctors(doctor_id)
);

CREATE TABLE medications (
    user_id VARCHAR(10),
    full_name VARCHAR(100),
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    medication VARCHAR(100),
    time_1 VARCHAR(50),
    time_2 VARCHAR(50),
    time_3 VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE user_health_logger (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(10),
    heart_rate DECIMAL(5,2),
    blood_pressure VARCHAR(20),
    body_temperature DECIMAL(5,2),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE doctor_booking_schedule (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id VARCHAR(10),
    date DATE,
    slot_9am ENUM('FREE', 'BOOKED'),
    slot_10am ENUM('FREE', 'BOOKED'),
    slot_11am ENUM('FREE', 'BOOKED'),
    slot_12pm ENUM('FREE', 'BOOKED'),
    slot_1pm ENUM('FREE', 'BOOKED'),
    slot_2pm ENUM('FREE', 'BOOKED'),
    slot_3pm ENUM('FREE', 'BOOKED'),
    slot_4pm ENUM('FREE', 'BOOKED'),
    slot_5pm ENUM('FREE', 'BOOKED'),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE doctor_appointments (
    appointment_id VARCHAR(10) PRIMARY KEY,
    date DATE,
    time TIME,
    user_full_name VARCHAR(100),
    user_id VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE user_appointments (
    appointment_id VARCHAR(10) PRIMARY KEY,
    user_ID VARCHAR(10),
    date DATE,
    time TIME,
    doctor_full_name VARCHAR(100),
    doctor_id VARCHAR(10),
    FOREIGN KEY (user_ID) REFERENCES user(user_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);
