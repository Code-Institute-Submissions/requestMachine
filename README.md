# **Request Machine app**

A website to compare Software requirements to Laptop abilities. Both lists can be updated and then the laptop list can be narrowed down automatically by choosing one or more software with their requirements . The app works best on desktop machines, but can be used on tablets in landscape mode too.

## Table of content

## UX design

The design primarily focus on simplicity and usability to provide a good user experience while giving feedback to the user by colour changes on the navigation bar.

The goal was not to provide a cross platform tool to all devices, but to show, how to retrive data and combine with other data sets from mongo db, and give a possible start point to corporate request app, where the employee can request a laptop based on their needs. 

The split navigation bars show the main difference between the parts of the tool given to the administrators and the users.

### Database structure

The database name: requestMachineDB

Collections: laptops, softwares

laptops documents contains the following fields with description and type:

(_id) the object id -string

(model_name) the model name -string

(model_number) the model number -string

(proc_gen) what generation the processor is -integer

(proc_cores) how many processors in the CPU -integer

(proc_max) what is the max frequency the CPU capable of -double

(ram_size) the installed ram -double

(hard_drive) the installed hard drive -double

(gpu_ram) the installed graphics memory -double

(img) the image link -string

(in_basket) shows if the laptop is in the basket so it is capable to run the chosen software -boolean



The softwares documents contains the following fields with description and type:

(_id) the object id -string

(software_name) the name of the software -string

(produced_by) the publisher of the software -string

(proc_gen) what generation the processor is needed -integer

(proc_cores) how many processors in the CPU needed-integer

(proc_min) what is the min frequency the CPU need to be capable of to run-double

(ram_size) the size of ram needed -double

(hard_drive) the size of hard drive needed -double

(gpu_ram) the installed graphics memory needed -double

(img) the image link -string

(chosen) shows if the software is chosen to be considered running on the machines -boolean



### User stories
Later on the features it is going to be discussed, that the application has an administrator and a enduser part, those are not restricted at this point, however the user stories going to give an overview to the options as the user parts. The admin tools will be showed in the administrator part, the catalogue and software choosing part will be discussed in the everyday user part, as the administrator would use the catalogue part as an everyday user.
#### User stories as an administrator
The application does not provide saved selection or state, so every time the user wants to see the catalogue, he/she will do this as a new user.

User A wants to add a new software/laptop to the catalogue. He/she can do this by clicking on the top navigation bar to the edit software/laptop  list. This will bring the user to a simplified list of softwares/laptops with name and producer/model name and model number of the software/laptop. User can click on the add new software/laptop button, and this will bring the user to a form where the user can add the software's/laptop's details. If the user is happy with the form to be submitted, the user needs to click on the add button. This will submit the form and add the new software/laptop to the catalogue.

User A is not happy with the form to be submitted, in this case user needs to click on any buttons except the submit button, so the form not going to be submitted, a cancel button located next to the add button.

User B wants to delete from the catalogue. He/she can click on the edit list buttons and on the next page where the list of product shows, the user can click on the delete button located next to the edit button. This will delete the product from the list.

User C wants to update a product. He/she can do this by clicking on the edit list button and then click on the edit button located next to the product short description. This will bring the user to the form page where the user amend the information. User can click on update to update the product information or any other buttons to cancel this operation.


#### User stories as a everyday user

User A wants to findt the configuration for his/her software selection. The site navigates to this section by default. If the user navigates to either the software or laptop catalogue, he/she can navigate back to the selection by clicking the find best config link located at the top left corner or the best config link on the middle of the navigation bar.

User B can quickly add and remove as many softwares ans he/she wants from the selection, by clicking on the add/remove button located on every software's info card.

After selecting even one software, the laptop list on the right side going to be updated regarding the minimum requirements of the software and the ability of the laptop to run it. This gives the user a real time update and the ability to make decision based onselecting or deselcting just one software.

## Features

### Existing Features
The application is capable to Create, Read, Update, and Delete from mongo DB, giving the user a clear and easy to use user interface.
Every form gives feedback to the user as every field is mandatory to fill in, and the type of fields give the user the only option e.g if the field is a number, the user can not give a string. 

The pictures are located on different servers depending on which user where and what can find to add to the form, as the user is only asked to provide a link to the picture on a server. This gives the user an easy way to quickly find it and present on the data form. (However, The user or the site owner does not own the pictures so any pictures trademarks presented on the site is solely used as a bulk practice and to represent the aim and shows the way the developer wants the site to be used.)

When the user wants to update an existing record, the placeholder of the form is the already given information and the user can only amend as less fields as he/she wants, and see the full datasheet as it will be after the update.

By clicking on the Add/Remove buttons, the software datasheets are checked against the laptops information to calculate which laptop is capable to run the selected software, and the site shows the updated list so the user only sees after any selection the laptops are capable to run the selected software.

#### Future ideas

In the future there would be a login page for authentication and to be able to save selections for users. In this way the restrictions for editing the lists would be easely implemented as the buttons would not be seen if the user has no access to these options(also need to have only read access to the db).

Compare products based on more information. The aim was to give an idea how it would happen and not to give precise decision at the moment.

To give the option to select the laptop and to communicate this in any way, such as email to the user or to others with a premade form to show the software selection and laptop options

### Features left to implement

The search option was left to implement and during testing it was clear that the user is not aware of the selected software, so need more feedback to the user. This can be a list of selected software or colour scheme on the cards, disappearing Add/Remove based on activity.

Better UI both layout and to be available on mobile. 

## Technologies Used

[Html](https://whatwg.org/) : To display the document in the web browser

[CSS](https://www.w3.org/Style/CSS/Overview.en.html) : To customise the document layout.

[Git](https://git-scm.com/) : For version control.

[Github](https://github.com/) : To publish the website's source code

[VsCode](https://code.visualstudio.com/) : For code editing.

[Libreoffice](https://www.libreoffice.org/): For creating initial planes.

[Typora](https://typora.io/): To edit the markdown files.

[python](https://www.python.org/) Main coding and data handling language

[pymongo](https://api.mongodb.com/python/current/) To communicate to the database

[Flask]([WSGI](https://wsgi.readthedocs.io/) ) Web application framework

[MongoDB](https://www.mongodb.com/) Database

[Heroku](https://www.heroku.com/) To Deploy the application

## Testing

Tests ran by users to find any problems or to suggests improvements. 

After the tests, it turned out, that the previous user's selection kept in the db and to fix this, every time the user reaches the find config or find best config pages, the db reset the chosen attribute to all software.

To test connection and CRUD, python shell and print function have been used and checked against the db. 

## Deployment

The project has been deployed and hosted on [Heroku](https://best-config.herokuapp.com/) in the following way:

Git was used for version control, and the source code is located on a Github [repository](https://github.com/varroz56/requestMachine). 

On Heroku dashboard a new app has been created called best-config. The [tutorial](https://devcenter.heroku.com/articles/creating-apps#creating-a-named-app) shows how to create an app. Europe server delivers the hosting. 

Heroku offers the option to being integrated to a Github repository, so after authorisation and linked in the the development repository, the application was ready to be deployed with one click. 

After deployment, Heroku offers a [link](https://best-config.herokuapp.com/) to the hosted website.



Lastly the MONGO_URI have been taken out and set on the local machine .bashrc file and used os.getenv to access it from the app, unfortunately after deployment had error message and could not start the app as it did not access the uri. On local WSGI server the app was running with the uri hidden. Because of this the username and password has been reinstated into the code.

 

## Credits

### Content

Any images or written information used on the site is linked or published by other websites and any pictures have been used is only for development purposes and to show an easy option to fill in the form. No information or media is owned by the developer, and is not responsible to the uploaded content.