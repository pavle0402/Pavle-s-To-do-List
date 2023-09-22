<h1>To-Do List App</h1>
<h3>Table of Contents:</h3> 

 
Description

Installation 

Challenges

Screenshots preview

Technologies used 

Contributing 

Creation process 

License

---
<h3>Description:</h3> 

Welcome to the To-Do List App, a user-friendly and efficient task management application meticulously crafted to assist you in organizing and optimizing your daily activities.


 ---


<h3>Installation:</h3> 

 

To run gym management system, follow these steps: 

 

Clone the repository on your machine: 

 
	git clone https://github.com/pavle0402/Pavle-s-To-do-List.git

 

Navigate to the project directory: 

cd your-path-to-gymmanagementsystem 

 

3. Create a virtual environment (optional but recommended) and activate it: 

python –m venv venv 

 

 

4. Activate your virtual environment: 

On windows: 

venv/Scripts/activate 

 

On macOS/Linux: 

Source venv/bin/activate 

 

5. Install project dependencies: 
	pip install –r requirements.txt 

 

6. Configure database connections in settings.py. 

 

7. Apply database migrations: 

py manage.py migrate 

 

8. Create superuser(staff) account: 

py manage.py createsuperuser(then you will be asked to provide 	username, email and password) - creating staff user

Or just register as a regular user through the app.

9. Start a development server: 

py manage.py runserver 

 

Application should now be running on: http://localhost:8000. 

 

 
---
<h3>Key Features:</h3> 

### User Authentication

- **Registration**: Create a new account to get started.
- **Login**: Access your account securely to manage your tasks.
- **Logout**: Sign out when you're done.

### Task Management

- **To-Do List**: The heart of the app, where you can add, view, and manage your tasks.
- **Task Details**: Each task includes the following information:
  - Title
  - Due Time
  - Priority (Pin/Unpin)
  - Completion Status (Checkbox)
- **Pin/Unpin Tasks**: Highlight important tasks by pinning them to the top of the list. Unpin tasks when they are no longer a priority.
- **Delete Tasks**: Remove tasks you no longer need.
- **Mark as Completed**: Easily check off completed tasks.
- **Bulk Unpin**: Unpin all pinned tasks with a single click.

### About and Contact Pages

- **About Page**: Learn more about the app and its features.
- **Contact Page**: While the contact feature is not currently functional(because the app is not hosted), you can still access it for future enhancements.

## Challenges

During the development of this app, I faced challenges in implementing the checkbox for task completion. This challenge was particularly related to the JavaScript portion of the code. While I've since improved my skills, I've chosen to maintain the original implementation as a representation of my knowledge at the time of completing this project.

 
 ---

<h3>Screenshots:</h3> 

Main page:

<img src="tdl_screenshots/Screenshot 2023-09-22 122820.png" width=450 height=350>


 As there are many screenshots for this project, i won't attach them here. You can check all the other pictures in "tdl_screenshots/" folder inside this repository.
 ---

<h3>Technologies used</h3> 

- Frontend: HTML, CSS, JavaScript
- Backend: Django
- Database: SQLite(django's default)
- Other technologies and libraries
 

  ---


<h3>Contributing</h3> 

Contributions to the project are welcome! If you would like to contribute, please follow these guidelines: 

Fork the repository. 

Create a new branch for your feature or bug fix. 

Make your changes and commit them with descriptive messages. 

Push your branch to your fork. 

Submit a pull request with a clear explanation of your changes. 

 
 ---

<h3>Creation Process:</h3>
<p1 style="text-align:center;">

**Project Overview**

Welcome to the To-Do List App, a project driven by the goal of providing a simple yet effective task management solution. 
This app emerged as a testament to my commitment to crafting original and efficient software applications.
Unlike following step-by-step tutorials, this project was conceived and developed entirely from scratch.
Which was my goal from start when making projects for portfolio that will showcase my skills.

**Challenges and Learning**

Throughout the development journey, I encountered a range of challenges, notably in the implementation of the task completion checkbox, which required delving into JavaScript, an area where I was less experienced at the time.
However, in the spirit of showcasing my growth as a developer, I have chosen not to make adjustments to this aspect of the project and to leave it as it was when i finished this project.
Of course i have expanded my knowledge now, but i will not fix this.

**Project Philosophy**

The To-Do List App has evolved into a feature-rich platform akin to popular task management tools. 
It all began with the aspiration to create something distinctive, moving beyond the confines of conventional to-do list applications.
My aim was to demonstrate originality and my evolving skills as a developer.
Although this project is unique, i got some ideas from Microsoft's to-do list since i use that almost every day.

Sharing this project serves as a testament to my ability to conceive, develop, and refine software applications. It also highlights my readiness to tackle challenges and craft innovative solutions, making it a valuable addition to my portfolio.
</p1>

 
---

## License

This project operates under the [MIT License](LICENSE).

---

Thank you for checking out the To-Do List App. Feel free to explore and use it for your task management needs.

For any questions or inquiries, contact me at your.email@example.com.

