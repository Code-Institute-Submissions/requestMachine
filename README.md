# **Request Machine app**

A website to compare Software requirements to Laptop abilities. Both lists can be updated and then the laptop list can be narrowed down automatically by choosing one or more software with their requirements . The app works best on desktop machines, but can be used on tablets in landscape mode too.

## Table of content

## UX design

The design primarily focus on simplicity and usability to provide a good user experience while giving feedback to the user by colour changes on the navigation bar.

The goal was not to provide a cross platform tool to all devices, but to show, how to retrive data and combine with other data sets from mongo db, and give a possible start point to corporate request app, where the employee can request a laptop based on their needs. 

The split navigation bars show the main difference between the parts of the tool given to the administrators and the users.

### Initial design wire-frames / mock-ups:



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

The search was left to implement and during testing it was clear that the user is not aware of the selected software, so need more feedback to the user. This can be a list of selected software or colour scheme on the cards, disappearing Add/Remove based on activity.

Better layout to be able to make this selection on cross platform.

## Technologies Used



## Testing


## Deployment



## Credits

### Content

### Media


### Acknowledgement
