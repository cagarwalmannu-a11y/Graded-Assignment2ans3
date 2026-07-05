# System Design

## Task 2.1 - Requirements and Architecture Choice
### Functional Requirements
1.  User authentication and authorization
2.  Student portal for viewing marks and enrolling in courses
3.  Admin panel for managing students, courses, and faculty

### Non-Functional Requirements
1.  **Scalability**: The system should handle 50,000 concurrent users during peak load.
2.  **Availability**: The system should be available 99.99% of the time.
3.  **Security**: The system should protect user data and prevent unauthorized access.

### Architecture Comparison

| Dimension | Monolithic Architecture | Microservices Architecture |
| --- | --- | --- |
| Independent Deployment | Difficult | Easy |
| Fault Isolation | Poor | Good |
| Management Complexity | Low | High |

Recommended Architecture: Microservices Architecture
Reason: Microservices architecture allows for independent deployment, fault isolation, and scalability, making it suitable for handling 50,000 concurrent users.

## Task 2.2 - High-Level Design
### Components
1.  **Authentication Service**: Handles user authentication and authorization (REST API)
2.  **Student Portal Service**: Provides student portal functionality (REST API)
3.  **Admin Panel Service**: Provides admin panel functionality (REST API)
4.  **Database**: Stores user data and other relevant information (Database query interface)

### Layered Architecture for Student Portal
1.  **Presentation Layer**: Handles user requests and responses (REST API)
    *   Receives: HTTP requests
    *   Passes on: Request data to Business Layer
2.  **Business Layer**: Handles business logic
    *   Receives: Request data from Presentation Layer
    *   Passes on: Data to Data Access Layer
3.  **Data Access Layer**: Handles database operations
    *   Receives: Data from Business Layer
    *   Passes on: Results to Business Layer

### Scaling
*   Horizontal scaling for web servers
*   Load balancing using Round-Robin algorithm

### Elasticity
*   Scale up during peak load and scale down during off-peak periods to reduce costs

### Session Routing Problem
*   Problem: Session inconsistency when requests are routed to different servers
*   Solution 1: Sticky sessions (load balancer routes requests to the same server)
    *   Trade-off: Poor fault tolerance
*   Solution 2: Centralized session store (e.g., Redis)
    *   Trade-off: Increased latency and cost

## Task 2.3 - Low-Level Design
### Student and Enrollment Classes
```python
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_student_id(self):
        return self.student_id

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    def get_enrollment_id(self):
        return self.enrollment_id
