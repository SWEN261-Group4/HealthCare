-- Inserting data into `doctors` table
INSERT INTO doctors (doctor_id, doctor_name, hospital)
VALUES 
('D001', 'Dr. Rick', 'General Hospital'),
('D002', 'Dr. Garfield', 'City Hospital');

-- Inserting data into `user` table
INSERT INTO user (user_id, full_name, blood_group, gender, age, allergies, health_insurance, medical_history, treatment_plan, doctor_1, doctor_2, doctor_3)
VALUES 
('U001', 'John Doe', 'A+', 'Male', 35, 'Peanuts', 'Health Ins Co.', 'No significant history', 'Ongoing treatment plan', 'D001', 'D002', NULL),
('U002', 'Alice Smith', 'B-', 'Female', 28, 'None', 'MediCare', 'Allergic to penicillin', 'Regular checkups', 'D001', NULL, NULL);

-- Inserting data into `medications` table
INSERT INTO medications (user_id, full_name, medication_1, medication_2, medication_3, medication_4, medication_5)
VALUES 
('U001', 'Steven Universe', 'Ibuprofen', 'Panadol', NULL, NULL, NULL),
('U002', 'Mark Grayson', 'Tramadol', 'Paracetamol', 'Adol', NULL, NULL);

-- Inserting data into `user_health_logger` table
INSERT INTO user_health_logger (user_id, heart_rate, blood_pressure, body_temperature, date)
VALUES
('U001', 75.5, '120/80', 98.6, '2023-11-14'),
('U002', 82.0, '118/75', 99.2, '2023-11-14');


-- Inserting data into `doctor_booking_schedule` table
INSERT INTO doctor_booking_schedule (doctor_id, date, slot_9am, slot_10am, slot_11am, slot_12pm, slot_1pm, slot_2pm, slot_3pm, slot_4pm, slot_5pm)
VALUES 
('D001', '2023-11-15', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE'),
('D002', '2023-11-15', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE');

INSERT INTO user_appointments (appointment_id, date, time, doctor_full_name, doctor_id)
VALUES 
('A001', '2023-11-20', '10:00:00', 'Dr. Rick', 'D001'),
('A002', '2023-11-22', '14:30:00', 'Dr. Garfield', 'D002');

INSERT INTO doctor_appointments (appointment_id, date, time, user_full_name, user_id)
VALUES 
('B001', '2023-11-25', '11:00:00', 'Steven Universe', 'U001'),
('B002', '2023-11-28', '09:30:00', 'Mark Grayson', 'U002');