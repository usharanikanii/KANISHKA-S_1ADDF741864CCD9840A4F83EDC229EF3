class Student:
  def __init__(self, name: str, roll_number: str, cgpa: float) -> None:
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list: list[Student]) -> list[Student]:
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students = [
  Student("Alice", "S123", 3.7),
  Student("Bob", "S124", 3.9),
  Student("Charlie", "S125", 3.5),
  Student("David", "S126", 3.8)
]

sorted_students = sort_students(students)

# Print the sorted list of students by CGPA in descending order
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

                                                     


