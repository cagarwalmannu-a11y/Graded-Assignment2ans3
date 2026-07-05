# System Design and Implementation

## Architecture
The system is designed using a microservices architecture, with separate services for authentication, student portal, and admin panel.

## SOLID Principles
The system follows SOLID principles, with separate classes for Student and Enrollment, and an interface for EnrollmentRepository.

## Observer Pattern
The system uses the observer pattern to notify email and audit log services when a student's marks are updated.

## Redundancy
The system uses synchronous primary-replica replication to ensure data consistency and availability.
