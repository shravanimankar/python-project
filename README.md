Django Python Machine Test

This repository contains a Django-based project for implementing REST APIs to manage Users, Clients, and Projects. The system is designed to perform the following tasks:

1.  Register Clients : Create new client entries in the system.
2.  Fetch Client Information : Retrieve detailed information about clients, including associated projects and their statuses.
3.  Edit/Delete Client Information : Update or remove client records as needed.
4.  Manage Projects : Add new projects for clients and assign users to these projects.
5.  Retrieve Assigned Projects : List projects assigned to the logged-in users.

The project uses Django's default admin template for user management and provides REST APIs for handling clients and projects. The API endpoints support operations such as listing all clients, creating and updating client details, and managing project assignments. 

The system is built to accommodate a large number of users, clients, and projects, with support for multiple projects per client and multiple users per project.
