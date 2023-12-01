UPDATE user SET full_name = 'ruby' WHERE user_id = 'U001';
UPDATE user SET full_name = 'sapphire' WHERE user_id = 'U002';
INSERT INTO user (user_id, full_name, blood_group, gender, age, allergies, health_insurance, medical_history, treatment_plan, doctor_1, doctor_2, doctor_3)
VALUES 
('U003', 'jasper', 'A+', 'Other', 30, 'None', 'Ins Co.', 'No significant history', 'Ongoing treatment plan', 'D001', NULL, NULL);