Knowledge Learning Documentation
================================

Welcome to the technical documentation of **Knowledge Learning**.

Knowledge Learning is a Django-based e-learning platform that allows users
to purchase online training courses and lessons, validate their progress,
and obtain certifications.

This documentation is automatically generated using **Sphinx**
from the Python docstrings of the project source code.

Main Features
-------------

- User registration with email activation
- Authentication and role management (admin / client)
- Course and lesson purchasing (sandbox logic)
- Lesson validation and automatic certification
- Administration back-office using Django Admin

Technical Stack
---------------

- Python 3
- Django 6
- SQLite (development database)
- Sphinx for documentation generation

Project Structure
-----------------

- users: user management, authentication, account activation
- courses: themes, courses, lessons, purchases and certifications
- config: global project configuration

This documentation demonstrates the use of a dedicated documentation tool
as required by the project evaluation criteria.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   code_overview

