# Electric Kitchens

Click [here](https://electric-kitchens-02035ecbc37c.herokuapp.com) for the live link.

## Purpose

The purpose of this site is to allow users to purchase electric kitchen appliances. It allows them to easily navigate the site to find what they are looking for and to feel safe about making a purchase. Registered users can save their delivery information, leave reviews on products and add products to their wishlist.

![Am I Responsive view of website](documentation/testing/other/am-i-responsive.png)

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
* View the products available for purchase.
* View the details of a product.
* See their total purchase price at any time in the navbar.
* Register for an account.
* Log in to their personal account.
* Log out of their account.
* Recover their password if they forget their password.
* Receive an email confirmation when they register for an account.
* View their profile page when logged in.
* Save their delivery information.
* View their delivery information on their profile page.
* View their order history on their profile page.
* Sort products by category.
* Sort products by price, rating, wattage, ease of use or capacity.
* Search for products in the search bar.
* Select a quantity of an individual product to purchase.
* Add a product to their shopping bag.
* View their shopping bag at any time.
* Update the quantity of an item in their shopping bag.
* Remove a product from their shopping bag.
* Enter their payment information.
* Feel safe and secure when entering their payment information.
* View a confirmation of their order.
* Receive a confirmation email for each order submitted.
* Review a product.
* View the reviews they have made.
* Remove a review that they made.
* Add a product to their personal wishlist.
* View their wishlist.
* Remove a product from their wishlist.

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
* The Kanban Board was created using GitHub. The link to the board is [here](https://github.com/users/Soro82/projects/3).
* I used six milestones for the project, one for each Epic. 
* The milestones helped to track my progress through the project. 
* The User Stories were divided into three categories - must have, should have and could have. 
* I used labels to categorize the user stories.
* I changed the "Approve Reviews" user story from "should have" to "won't have" as it was not required to complete the project.

### Epics

* Viewing and Navigation
* Registration and User Accounts
* Sorting and Searching
* Purchasing and Checkout
* Admin and Store Management
* Reviews and Wishlist

### User Stories

#### Epic: Viewing and Navigation

* View Products
* View Product Details
* Identify Deals
* View my Total

#### Epic: Registration and User Accounts

* Register an Account
* Login/Logout
* Recover Password
* Email Confirmation
* User Profile

#### Epic: Sorting and Searching

* Sort Products
* Sort by Category
* Sort Multiple Categories
* Search for Products
* View Search Results

#### Epic: Purchasing and Checkout

* Select Quantity
* View Bag
* Adjust Bag
* Enter Payment Information
* Feel Safe and Secure
* View Order Confirmation
* Receive Email Confirmation

#### Epic: Admin and Store Management

* Add a Product
* Edit/Update a Product
* Delete a Product
* Approve Reviews

#### Epic: Reviews and Wishlist

* Review a Product
* Remove Reviews
* Add to Wishlist
* View Wishlist
* Update Wishlist

[Back to Top](#electric-kitchens)

## Design

### Color Scheme

### Wireframes
<details>
<summary>Home Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/home_page.png)

</details>

<details>
<summary>All Products Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/products_page.png)

</details>

<details>
<summary>Product Details Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/product_detail_page.png)

</details>

<details>
<summary>Shopping Bag Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/bag_page.png)

</details>

<details>
<summary>Checkout Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/checkout_page.png)

</details>

<details>
<summary>My Profile Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/profile_page.png)

</details>

<details>
<summary>My Reviews Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/reviews_page.png)

</details>

<details>
<summary>My Wishlist Page</summary>

![Home Page Mobile Wireframe](documentation/wireframes/wishlist_page.png)

</details>

## Technologies Used

### Languages Used
* HTML5
* CSS
* JavaScript
* Python

### Frameworks Used
* Django - https://www.djangoproject.com
* Bootstrap v4.1 - https://getbootstrap.com

### Programs Used
* GitHub - to host the source code.
* GitPod - IDE used to develop the website.
* Heroku - to deploy the project.
* W3C Markup Validation Service - to validate the HTML code.
* W3C CSS Validation Service - to validate the CSS code.
* JSHint - to validate the JavaScript code.
* CI Pep8 Python Validator - to validate the Python code.
* Am I Responsive - to test the website's responsiveness.


[Back to Top](#electric-kitchens)

## Testing

Click [here](TESTING.md) to open the Testing section.

## Deployment and Local Development

### Heroku Deployment

The website was deployed using [Heroku](https://www.heroku.com/) through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. To add a config var:
   * In the "KEY" field - enter the KEY name in all capital letters.
   * In the "VALUE" field - enter the actual key and click "Add".
8. Scroll to the "Buildpacks" section and click "Add buildpack".
9. Select Python and save changes.
12. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
13. Select "GitHub" as the deployment method and click "Connect to GitHub".
14. Search for the GitHub repository name in the search bar.
15. Click on "connect" to link the repository to Heroku.
16. Scroll down and click on "Deploy Branch".
17. Once the app is deployed, Heroku will notify you and provide a button to view the app.

Click [here](https://electric-kitchens-02035ecbc37c.herokuapp.com) for the live link.

### Local Development

#### Forking

Forking is a way to make a copy of the original repository on your GitHub account to view and change without affecting the original repository.

* Log in to GitHub and locate your GitHub Repository.
* At the top of the Repository(under the main navigation) locate the "Fork" button.
* Now you should have a copy of the original repository in your GitHub account.

#### Cloning

* Log in to GitHub and locate the GitHub Repository.
* Under the repository name click "Clone or download".
* Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
* Open Git Bash.
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone and then paste The URL copied in step 3.
* Press Enter and your local clone will be created.