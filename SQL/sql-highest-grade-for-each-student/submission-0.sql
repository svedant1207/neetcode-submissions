SELECT student_id, MAX(score) as max_score
FROM exam_results
GROUP BY student_id;