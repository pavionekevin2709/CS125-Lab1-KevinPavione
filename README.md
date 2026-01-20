Kevin Pavione - 84012 
Assignment 2 - Library Management System
A clean, PEP 8-compliant implementation of the Library Management System that should pass both the functional auto-grader and style checks:
Run python library_system.py"
List of Classes Implemented and Their Relationships

- **LibraryItem**  
  → Abstract/base class for all library items  
  → Defines common attributes and behavior for all types of library materials

- **Book**  
  → Inherits from **LibraryItem**  
  → Represents physical or digital books with author, ISBN, and page count

- **DVD**  
  → Inherits from **LibraryItem**  
  → Represents DVDs with director, runtime (in minutes), and content rating

- **Magazine**  
  → Inherits from **LibraryItem**  
  → Represents magazines with issue number and publication date

- **Library**  
  → Standalone management class (does **not** inherit from any other class)  
  → Manages a collection of **LibraryItem** objects (polymorphic list containing Books, DVDs, and Magazines)

Relationship summary (inheritance hierarchy):
