# HOSPITAL MANAGEMENT SYSTEM
Hospital Management system is a system that provide a platform for basic hospital activities to be automated via the internet, it allows hospital workflow to become for active, interactive and efficient. It handles different direction of hospital workflow; it enables smooth healthcare performance. It service that unifies and simplifies the work of healthcare professionals as well as interaction with patients. It is essentially created for group of users such as *Patient users*, *hospital receptionist user*, *doctor user* and the *overall manager* of the hospital.  The purpose of the hospital management system is to manage the employees and patient activities remotely with immediate access for authorized users. When the patient wants to have an appointment, he might choose among a few options, he may find the data about visiting hours on the medical specialists’ profiles and book a convenient time. As for the medical specialists, the healthcare record management system that contains the patient information in one place enables more efficient work of the staff and safe keeping of patient records. Automation speeds up the process of patient registration and filling out all the necessary records. The doctors have the ability to check the disease history, test results, as well as add new data to the patient file i.e creating medical records on a patient. The job of the doctor that previously involved too much paperwork can be completely computerized. Doctors spend more time on patients treatment rather than documentation.  Patient that have to visit hospital stay on a long queue and eventually when the patient gets to where he books an appointment he wastes lots time before his information is gotten form the pile of files then he finally queues to meet with a doctor again,  With an application these problems are been solved and automated to make it faster, easier and efficient.

# SCOPE OF THE SYSTEM
* Digital medical records:
    It provides a data store the is electronic which to some extent provides a level of security and ease access to the data from anywhere. Patients records can be kept online to allow doctors access at any time and keep track of the patient and be able to keep a check on the patient. It allows accuracy and reduces the risk of any mistake.


* Patients self-services:
    Patients have their own system accounts where the list of various actions can be performed. They are able to make online requests or reservation, receive the test results, receive the consultation of the medical specialists and many more.


* Patient management:
    It is used to control patient flow. It can be used to register them, get the data of the patients’ health condition, view the treatment and check the medical history and reports.


* Staff management:
Staff management module provides the human resources administration. It updates the job description of employees, updates the hospital structure, tracks the recruiting records.


* Appointment management:
    Appointment module in hospital management arranges the schedule of doctors due to the patients’ application. It helps to organize the availability of medical specialists at any convenient time. Some hospital can even offer remote visits when you need immediate assistance.


* Record management:
    Helps in managing a detailed and secure records of registered patients. Gets the patients record anytime needed, delete when required and updated when needed.


# Application Navigations
The app provides an index page where anonymous users can visit without any authentication. The index page provides basic information about the app for first time users. On the Navbar of the index page are links;
Home: the home page provides access to the index page

About: This link is linked to the page where the details of the activates of the hospital is explained

Login: This link provides access to the login for form where various group of users can login in except the admin (super user which is the admin)

Register: This is linked to the registration page for patients who want to register to gain access to the activities of the app. 

Patient user: When patients are registered they only gain access to their profile with their username and password where their details are displayed and they can book an appointment with a doctor. Patients are added to the Patients group during registration.

Staff user: A staff user is just like the receptionist who has some level access in the app, he can manage patients like add, edit details and list, can manage staff like add, edit details and list, he can add doctors and also list and finally can add and list appointments with doctors. Staff is added by the admin and can access its work space with username and password. use *USERNAME: affez* *PASSWORD: 123456789* to login into staff's workspace.

Doctor user: A doctor user has access to confidential information of patients where he can add medical records for a specific patient, retrieve the records and can also list all medical records of the hospital. Doctor users can also see the list of available patients in the hospital and can also see the list of appointment made by patients. Doctor is added to the doctors group during registration. use *USERNAME: ola* *PASSWORD: 123456789* to login into doctor's workspace.

Super user: This user has the highest level of access in the app, can do everything within the app as long as he is within djando admin site. The super user makes use of Django inbuilt admin for it operations and be access via the admin url which is http://all-care.herokuapp.com/admin. He adds a staff and assign him to the group of staff where he has access to the receptionist app. Super user Username ‘olalekan’ password “jimolanite”, note when logging in as an admin on a browser, ensure that you're logged out before trying to logging any other user in one main site.The login as a staff are; username:afeez, password:123456789. The login for doctor are; username: ola, password: jimolanite.
Application Link is (http://all-care.herokuapp.com)


