# Electric Kitchens

Click [here](https://electric-kitchens-02035ecbc37c.herokuapp.com) for the live link.

## Purpose

The purpose of this site is to allow users to purchase electric kitchen appliances. It allows them to easily navigate the site to find what they are looking for and to feel safe about making a purchase. Registered users can save their delivery information, leave reviews on products and add products to their wishlist.

![Am I Responsive view of website](documentation/testing/other/am_i_responsive.png)

## Table of Contents

### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Target Audience](#target-audience)
* [New user](#new-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Agile Methodology](#agile-methodology-1)
* [Epics](#epics)
* [User Stories](#user-stories)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Typography](#typography)
* [Wireframes](#wireframes)
* [Database Scheme](#database-scheme)
### [Features](#features-1)
* [Security Features](#security-features)
* [Existing Features](#existing-features)
* [Future Features](#future-features)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Testing](#testing-1)
### [Deployment and Local developement](#deployment-and-local-development)
* [Heroku Deployment](#heroku-deployment)
* [Local Developement](#local-development)
* [ElephantSQL Database](#elephantsql-database)
### [References](#references-1)
* [Credits](#credits)
* [Acknowledgments](#acknowledgments)

## User Experience (UX)

### Project Goals

To allow users to:
* Book horse riding lessons.
* Create a personal account by signing up to the website.
* Set up a username and password for their account.
* Log in to their personal account.
* Choose a date and time for their lesson.
* Choose if they want their lesson indoor or outdoor.
* Choose their level of experience.
* Choose what horse they want for their lesson.
* Make changes to any bookings they have made.
* Delete a booking they made.
* See all the horses available with a picture of the horse and their height and color.
* See a list of available times for lessons.
* See the three most popular horses.
* Log out of their account.
* See a message confirming they are logged out.

### Target Audience
The website is designed to allow people to book horse riding lessons. They can choose the date and time for their lesson, whether they would like it indoor or outdoor, their level of experience and what horse they would like for their lesson. They also have the option to indicate if they are an adult or a child and to enter their height if they wish. With the CRUD (Create, Read, Update, Delete) functionality they can also view, edit and delete their bookings when they log into their account.

Each user has the ability to:

### New User
* View the lesson times available
* See the three most popular horses
* Access to the Horses page to see all available horses and their details
* Register their own personal account

### Registered User
* Login to their account
* Make a booking
* View their bookings
* Update their bookings
* Delete their bookings

### Admin User
* Make a booking
* View bookings for all users
* Update bookings for all users
* Delete bookings for all users
* Add new horses to the website
* Upload pictures of the horses
* View details of all horses
* Update details of all horses
* Delete horses from the website

[Back to Top](#electric-kitchens)

## Agile Methodology
* Agile Methodology was used for this project as it required a lot of planning.
* The Kanban Board was created using GitHub. The link to the board is [here](https://github.com/users/Soro82/projects/2).
* I used six milestones for the project, one for each Epic. 
* The milestones helped to track my progress through the project. 
* The User Stories were divided into three categories - must have, should have and could have. 
* I used labels to categorize the user stories.

### Epics

* Set up Project
* Deployment
* Navbar Links
* User Registration
* Book a Lesson
* Add a Horses Page

### User Stories

#### Epic: Set up Project

* Create the project and book_lesson app
* Create the database
* Build the models
* Create the views
* Create the templates

#### Epic: Deployment

* Open a new Heroku application
* Add required Config Vars
* Set up a Procfile
* Set DEBUG to False

#### Epic: Navbar Links

* Links in navbar to login, log out, sign up and make a booking
* Log out and make a booking are disabled when no user is logged in
* Logged in username displayed when a user is logged in
* Burger icon replaces navbar on smaller screens

#### Epic: User Registration

* Set up an account with a username, email and password
* Enter my age and height when registering
* See a message stating that I am logged in
* Have a logout button visible
* See a confirmation message when I logout

#### Epic: Book a Lesson

* Choose a date for a lesson
* Choose a time for a lesson
* Choose whether I want indoor or outdoor
* Choose my level of experience from a list of options
* See a list of possible lesson times
* See a confirmation message when I make a booking

#### Epic: Add a Horses Page

* See pictures of each horse on a page
* See details of each horse under their picture
* Have a "Book Now" button available under each horse on the Horses page

[Back to Top](#electric-kitchens)

## Design

### Color Scheme