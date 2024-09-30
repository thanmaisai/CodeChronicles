from fastapi import FastAPI, Path, HTTPException
from typing import Optional

# Initialize the FastAPI app
app = FastAPI()

# Sample data for students (this could be replaced with a database in a real-world app)
students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "class": "year 11"
    },
}

# Root endpoint: returns a welcome message
@app.get("/")
def index():
    """
    This is the root endpoint. When accessed, it returns a simple dictionary.
    """
    return {"message": "Welcome to the student API!"}

# GET request to fetch a student by ID - (Path Parameters)
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", ge=1)):
    """
    Fetch a student from the dictionary using their ID.
    - student_id: the ID of the student (must be an integer and greater than or equal to 1)
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")  # Raises an error if the student ID doesn't exist
    return students[student_id]  # Returns the student's details if found

# GET request to fetch a student by name (Query Parameter)
@app.get("/get-student-by-name/")
def get_student(name: str):
    """
    Fetch a student by their name using a query parameter.
    - name: the name of the student
    """
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]  # Return the student if found
    return {"data": "Student not found"}  # Return an error message if not found

# GET request to fetch a student by ID and optionally by name (Query + Path Parameters)
@app.get("/get-student-by-name/{student_id}")
def get_student_by_name(student_id: int, name: Optional[str] = None):
    """
    Fetch a student by ID and optionally by name.
    - student_id: the ID of the student (must be an integer and greater than or equal to 1)
    - name: the name of the student (optional)
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")  # Error if ID is not found

    student = students[student_id]  # Get student details
    
    if name and student["name"] != name:
        return {"data": "Student name does not match"}  # Check if the name matches the ID
    
    return student  # Return the student details

# POST request to add a new student
@app.post("/add-student/{student_id}")
def add_student(student_id: int, name: str, age: int, class_name: str):
    """
    Add a new student to the dictionary.
    - student_id: the ID to assign to the new student
    - name: student's name
    - age: student's age
    - class_name: class of the student
    """
    if student_id in students:
        raise HTTPException(status_code=400, detail="Student with this ID already exists.")  # Error if ID already exists
    
    students[student_id] = {"name": name, "age": age, "class": class_name}  # Add student details
    return {"message": f"Student {name} added successfully", "student": students[student_id]}  # Confirmation message
 
# PUT request to update an existing student's details
@app.put("/update-student/{student_id}")
def update_student(student_id: int, name: Optional[str] = None, age: Optional[int] = None, class_name: Optional[str] = None):
    """
    Update the details of an existing student.
    - student_id: the ID of the student to update
    - name: new name of the student (optional)
    - age: new age of the student (optional)
    - class_name: new class of the student (optional)
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found.")  # Error if ID is not found
    
    # Update student details if provided
    if name:
        students[student_id]["name"] = name
    if age:
        students[student_id]["age"] = age
    if class_name:
        students[student_id]["class"] = class_name
    
    return {"message": f"Student {student_id} updated successfully", "student": students[student_id]}  # Confirmation message

# DELETE request to remove a student from the dictionary
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    """
    Delete a student from the dictionary.
    - student_id: the ID of the student to delete
    """
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found.")  # Error if ID is not found
    
    del students[student_id]  # Remove the student
    return {"message": f"Student {student_id} deleted successfully"}  # Confirmation message
