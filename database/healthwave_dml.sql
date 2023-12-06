-- Inserting data into `doctors` table
INSERT INTO doctors (doctor_id, doctor_name, hospital)
VALUES 
('D001', 'Dr. Rick', 'General Hospital'),
('D002', 'Dr. Garfield', 'City Hospital');

-- Inserting data into `user` table
INSERT INTO user (user_id, full_name, blood_group, gender, age, allergies, health_insurance, medical_history, treatment_plan, doctor_1, doctor_2, doctor_3)
VALUES 
('U001', 'ruby', 'A+', 'Male', 35, 'Peanuts', 'Health Ins Co.', 'No significant history', 'Ongoing treatment plan', 'D001', 'D002', NULL),
('U002', 'sapphire', 'B-', 'Female', 28, 'None', 'MediCare', 'Allergic to penicillin', 'Regular checkups', 'D001', NULL, NULL),
('U003', 'jasper', 'A+', 'Male', 30, 'None', 'Ins Co.', 'No significant history', 'Ongoing treatment plan', 'D001', NULL, NULL);

-- Inserting data into `medications` table
INSERT INTO medications (user_id, full_name, medication_id, medication, time_1, time_2, time_3)
VALUES
('U001', 'ruby', 1, 'Panadol', '09:00', NULL, '18:00'),
('U002', 'sapphire', 2, 'Tramadol', '08:00', '14:00', '20:00'),
('U002', 'sapphire', 3, 'Xanax', '08:00', '14:00', '20:00'),
('U002', 'sapphire', 4, 'Cyanide', NULL, NULL, '20:00'),
('U003', 'jasper', 5, 'Adol', '08:00', '14:00', '20:00'),
('U003', 'jasper', 6, 'Steroids', '08:00', NULL, NULL);

-- Inserting data into `user_health_logger` table
INSERT INTO user_health_logger (user_id, heart_rate, blood_pressure, body_temperature, date)
VALUES
('U001', 75.5, '120/80', 98.6, '2023-11-14'),
('U002', 82.0, '118/75', 99.2, '2023-11-14');


-- Inserting data into `doctor_booking_schedule` table
INSERT INTO doctor_booking_schedule (doctor_id, date, slot_9, slot_10, slot_11, slot_12, slot_13, slot_14, slot_15, slot_16, slot_17)
VALUES 
('D001', '2023-11-15', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE'),
('D002', '2023-11-15', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE', 'FREE');

INSERT INTO doctor_appointments (appointment_id, date, time, user_full_name, user_id)
VALUES 
('B001', '2023-11-25', '11:00:00', 'ruby', 'U001'),
('B002', '2023-11-28', '09:30:00', 'sapphire', 'U002');

-- Inserting data into `user_illness` table
INSERT INTO user_illness (user_id, illness_name, illness_id)
VALUES
('U001', 'Muscle Strain', 7),
('U001', 'Sprained Ankle', 8),
('U002', 'Depression', 3),
('U002', 'Anxiety', 2),
('U002', 'Diabetes', 9),
('U002', 'Asthma', 10),
('U002', 'Hypertension', 11),
('U002', 'Obesity', 12),
('U003', 'Arthritis', 13),
('U003', 'Osteoporosis', 14),
('U003', 'Vision Impairment', 15);

INSERT INTO user_health_recommendations (illness_id, illness_name, health_recommendations)
VALUES
(7, 'Muscle Strain', 'Rest, ice, compression, elevation (RICE) method. Avoid strenuous activities.'),
(8, 'Sprained Ankle', 'Use ice packs, elevate the injured area, avoid putting weight on the ankle.'),
(3, 'Depression', 'Therapy sessions, medication as prescribed by a psychiatrist, regular exercise.'),
(2, 'Anxiety', 'Counseling, stress management techniques, mindfulness practices.'),
(9, 'Diabetes', 'Balanced diet, regular exercise, blood sugar monitoring.'),
(10, 'Asthma', 'Avoid triggers, use inhalers as prescribed.'),
(11, 'Hypertension', 'Maintain a healthy diet, exercise regularly, monitor blood pressure.'),
(12, 'Obesity', 'Balanced diet, portion control, regular exercise.'),
(13, 'Arthritis', 'Low-impact exercises, pain management, joint protection.'),
(14, 'Osteoporosis', 'Calcium and vitamin D supplements, weight-bearing exercises.'),
(15, 'Vision Impairment', 'Regular eye check-ups, use prescribed corrective measures.');