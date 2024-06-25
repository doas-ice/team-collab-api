# TeamCollab API
TeamCollab project management API allows teams to manage users, projects, tasks, and comments using the provided API endpoints. These endpoints can be used to integrate a front-end web or mobile application.

## Setting up the project
### Requirements
The following tools needs to be installed on the system
- Python (version 3.6 or higher)
- Git

### Steps to Set Up the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sayed-Nahid/team-collab-api.git
   ```
   
2. **Navigate to the Cloned Repository**
   ```bash
   cd team-collab-api
   ```

3. **Create a Python Virtual Environment**
   ```bash
   python -m venv venv
   ```

4. **Activate the Python Virtual Environment**
   - On Linux and OSX (`bash`, `zsh`):
     ```bash
     source venv/bin/activate
     ```
   - On Linux and OSX running `fish` shell
      ```bash
      source venv/bin/activate.fish
      ```
   - On Windows (cmd):
     ```bash
     venv\Scripts\activate
     ```
   - On Windows (PowerShell):
     ```bash
     venv\Scripts\Activate.ps1
     ```
     
5. **Install Required Python Packages**
   ```bash
   pip install -r requirements.txt
   ```

6. **Create Database Migrations**
   ```bash
   python manage.py makemigrations
   ```

7. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

8. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

   The development server will start running at `http://127.0.0.1:8000/`.

### Accessing the API

- **API Documentation**: Explore the API endpoints. API interface available at `http://127.0.0.1:8000/api/`. Check the API Documentation for more details.
