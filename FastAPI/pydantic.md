# Pydantic Notes

### Overview of Pydantic

What is Pydantic?
* A community-driven, open-source framework designed for data validation and settings management in Python applications.
* Provides tools and libraries to write reusable, modular, and reliable code.
* Particularly useful for building scalable and maintainable software systems, such as APIs and microservices.

### Key Features
#### 1. Dynamic Typing Problem
Example: Catching Errors Early
```
from pydantic import BaseModel, ValidationError

class Student(BaseModel):
    name: str
    age: int

try:
    student = Student(name="Alice", age="20")  # Incorrect type: age should be an int
except ValidationError as e:
    print(e)  # This will raise a ValidationError
```
* **Explanation**: Pydantic raises a `ValidationError` if the provided data types do not match the expected types, allowing you to catch errors early in the development process.

#### 2. Data Validation
Example: Validating Data Types and Constraints
```
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=1, le=120)  # Age must be between 1 and 120

# Valid data
student = Student(name="John", age=17)  # This is valid

# Invalid data
try:
    student = Student(name="John", age=150)  # Age is out of bounds
except ValidationError as e:
    print(e)  # Raises ValidationError
```
* **Explanation**: The `Field` function allows you to set constraints like minimum (`ge`) and maximum (`le`) values, ensuring that the data adheres to defined rules.

#### 3. JSON Serialization
Example: Serializing and Deserializing Data

```
class Student(BaseModel):
    name: str
    age: int
    class_name: str

student = Student(name="Alice", age=20, class_name="Year 12")

# Serialize to JSON
student_json = student.json()
print(student_json)  # Output: {"name": "Alice", "age": 20, "class_name": "Year 12"}

# Deserialize from JSON
new_student = Student.parse_raw(student_json)
print(new_student)  # Output: name='Alice' age=20 class_name='Year 12'
```
* **Explanation**: Pydantic provides built-in methods for converting models to JSON and vice versa, simplifying the process of working with JSON data.


#### 4. Custom Field Validation
Example: Implementing Custom Validation Logic
```
from pydantic import BaseModel, validator

class Student(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, value):
        if value < 1:
            raise ValueError('Age must be greater than 0')
        return value

# Valid data
student = Student(name="Alice", age=20)

# Invalid data
try:
    student = Student(name="Alice", age=-5)  # Invalid age
except ValidationError as e:
    print(e)  # Raises ValidationError with custom message
```
* **Explanation**: The `@validator` decorator allows you to define custom validation rules. Here, it checks that the age is greater than zero.

#### 5. Comparison with Dataclasses
Example: Using Pydantic vs. Dataclass

```
from dataclasses import dataclass

@dataclass
class StudentDataClass:
    name: str
    age: int

# Using Dataclass
student_dc = StudentDataClass(name="Alice", age="20")  # No validation

# Using Pydantic
student_pd = Student(name="Alice", age=20)  # Valid

try:
    student_pd = Student(name="Alice", age="20")  # Raises ValidationError
except ValidationError as e:
    print(e)  # Age must be an int
```
* **Explanation**: Unlike dataclasses, which do not enforce type checking, Pydantic models automatically validate types and raise errors for invalid data, making Pydantic a better choice for applications where data integrity is critical.

<hr>


### Using Pydantic
#### Defining a Pydantic Model
```
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=1, le=120, example=17)  # Age must be between 1 and 120
    class_name: str = Field(..., example="Year 12")
```
* Field: Use Field to add metadata like examples and constraints.
#### Validating Data
* Automatic type validation on model instantiation:
```
student = Student(name="Alice", age=20, class_name="Year 12")  # Valid
```
* Raise errors for invalid data:
```
student = Student(name="Alice", age=150, class_name="Year 12")  # Raises ValueError
```
### Custom Field Validation
```
from pydantic import validator

class Student(BaseModel):
    name: str
    age: int

    @validator('age')
    def check_age(cls, v):
        if v < 1:
            raise ValueError('Age must be greater than 0')
        return v
```
* Use `@validator` to enforce additional rules for specific fields.

#### JSON Serialization
* Convert Pydantic models to JSON easily:
```
student = Student(name="Alice", age=20, class_name="Year 12")
student_json = student.json()  # Returns JSON representation
```
#### Error Handling
* Pydantic raises ValidationError for invalid data:
```
from pydantic import ValidationError

try:
    student = Student(name="Alice", age="invalid_age")  # Invalid
except ValidationError as e:
    print(e.json())  # Display validation errors in JSON format
```

## Additional Resources
- **Official Documentation**: [Pydantic Docs](https://docs.pydantic.dev/latest/)
- **API Reference**: [BaseModel API](https://docs.pydantic.dev/latest/api/base_model/)
- **Concepts**: [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)


## Use Cases
* Ideal for applications requiring robust data validation and serialization, such as:
    * APIs (e.g., FastAPI)
    * Configuration management
    * Data models in microservices
    * Any scenario where data integrity is critical