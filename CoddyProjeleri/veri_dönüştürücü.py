def transform_dataset(data):
  qualified_students = {
      student["student_id"]: round(sum(student["grades"]) / len(student["grades"]), 2)
      for student in data 
      if all(grade > 70 for grade in student["grades"])
  }
  subject_summary = {}
  for student in data:
    if student["student_id"] in qualified_students:
        for subject in student["subjects"]:
            subject_summary[subject] = subject_summary.get(subject, 0) + 1
  return {
      "qualified_students": qualified_students,
      "subject_summary": subject_summary
  }