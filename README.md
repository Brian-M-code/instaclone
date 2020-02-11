# PROJECT NAME
- le'Gram

## Author
- Brian Mutuma

## Description
This is a clone of Instagram. You can post, comment and view pictures posted on this App just like on Instagram.

### User Story
- Users need to Sign in to the application to start using.

- Users can view different photos.

- Users can click on a single photo to view it and also      view details of the photo.

- Users can search for different photos.

- Users can Upload their pictures to the application.

- Users can see their profile with all their picture.

- Users can view a picture and leave a comment on it.

## Installion and Setup instructions
- Clone this repo: git clone https://github.com/brian-m-code/instaclone.git.

- The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
On your terminal,Create database gallery using the command below.

#### CREATE DATABASE insta; 
**if you opt to use your own database name, replace instagram your preferred name, then also update settings.py variable DATABASES > NAME
Migrate the database using the command below

python3.6 manage.py migrate
Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver
Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
On your terminal,Create database gallery using the command below.

##### CREATE DATABASE insta; 
**if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME
Migrate the database using the command below

python3.6 manage.py migrate
Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver
Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

#### Running the tests
Use the command given below to run automated tests.

    python manage.py test insta
    
### TECHNOLOGIES Used
Django - web framework used
Javascript - For DOM(Document Object Manipulation) scripts
HTML - For building Mark Up pages/User Interface
CSS - For Styling User Interface

# Contacts
mutuma.brian@yahoo.com

# live link


# License
This project is licensed under the MIT License - see the LICENSE.md file for details