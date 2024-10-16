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

### Database Scheme

* [Draw.io](https://draw.io) was used to create the database scheme.

![Database Scheme](documentation/images/electric_kitchens_erd.png)

[Back to Top](#electric-kitchens)

## Features

### Security Features

#### User Authentication
* Django comes with a user authentication system called AllAuth. 
* It handles user accounts, groups, permissions and cookie-based user sessions.
* The Django authentication system handles both authentication and authorization. 
* Authentication verifies a user is who they claim to be, for example when a user is logging in to the website. 
* Authorization determines what an authenticated user is allowed to do, for example in the navbar in base.html we check if the user is logged in using this line of code: {% if user.is_authenticated %}.

#### CSRF (Cross Site Request Forgery)
* CSRF attacks allow a malicious user to execute actions using the credentials of another user without that user’s knowledge or consent.
* Django has built-in protection against most types of CSRF attacks.
* CSRF protection works by checking for a secret in each POST request. 
* This ensures that a malicious user cannot “replay” a form POST to your website and have another logged in user unwittingly submit that form. 
* The malicious user would have to know the secret, which is user specific (using a cookie).

#### The login_required Decorator
* The login_required decorator is on all views that require the user to be logged in.
* For this website it was used on the views in the products, profiles, reviews and wishlist apps. It ensures that only authenticated users can access these views.

#### Custom Error Pages
* The 404 and 500 Error Pages are used to allow the user to return to the website’s home page.
* They use the base.html to inform the user of their error in a friendly and helpful manner.

#### Form Validation
The review form and is validated to ensure:
* The date entered is today's date or a previous date.

[Back to Top](#electric-kitchens)

### Existing Features

#### Home Page

* The Home page has a background image of a mixture of different electric kitchen appliances.
* There is a Shop Now button which opens the All Products page.

![Home Page](documentation/screenshots/desktop/home_page_desktop.png)

#### Navbar

* The Navbar contains the website title which is also a link to the home page.
* There is a Search Bar to allow the user to search for particular products or keywords.
* The All Products dropdown menu has a link to the All Products page and links to allow the user to view the All Products page arranged by price, rating, wattage and ease of use.
There are links to view only all the kettles, washing machines, air fryers and coffee machines.
* There is a shopping cart icon which is a link to the Shopping Bag page.
* There is a person icon which opens the My Account dropdown menu.
* There is a banner informing customers of free delivery on all purhcases over $50.

##### Navbar(Logged Out)

* The My Account dropdown menu contains links to the login and register pages when the user is logged out.

![Navbar(Logged Out)](documentation/screenshots/desktop/navbar_logged_out.png)

##### Navbar(Logged In)

* The My Account dropdown menu contains links to the My Profile, My Reviews and Logout pages when the user is logged in.
* There is a link to My Wishlist beside the My Account dropdown menu when the user is logged in.

![Navbar(Logged In)](documentation/screenshots/desktop/navbar_logged_in.png)

##### Navbar(Admin Logged In)

* There is an extra link in the My Account dropdown menu called Product Management when admin users are logged in.

![Navbar(Logged In)](documentation/screenshots/desktop/navbar_logged_in_admin.png)

#### All Products Page

* All the products on the website are listed on the All Products page with the total number of products at the top left.
* There is a dropdown menu allowing the user to sort the products by price, rating, wattage, ease of use or capacity.
* Each product's image is displayed with the product's name, price, category, rating and capacity underneath.
* The user can click on the product's image to open the Product Detail page to view more details about the product.

![Popular Horses(Logged In)](documentation/screenshots/desktop/all_products_desktop.png)

#### Product Details Page(Logged Out)

* There is a large image of the product and all the details of the product on this page.
* The quantity box allows the user to choose the quantity of the product they wish to purchase.
* There is a plus and minus button on either side of the quantity box.
* The minus button is disabled when the quantity is on 1.
* The plus button is disabled when the quantity is 99.
* The Keep Shopping button allows the user to return to the All Products page.
* The Add to Bag button allows the user to add the product to their shopping bag.

![Popular Horses(Logged In)](documentation/screenshots/desktop/product_detail_logged_out.png)

#### Product Details Page(Logged In)

* When the user is logged in, there are 2 more buttons under the Add to Bag button.
* The Add to Wishlist button adds the product to the user's wishlist.
* The Add Review button opens the Add Review page allowing the user to add a review for that product.

![Popular Horses(Logged In)](documentation/screenshots/desktop/product_detail_desktop.png)

#### Product Details Page(Admin Logged In)

* When admin users are logged in, there are 2 extra buttons above the quantity box.
* The Edit button opens the Edit Product page.
* The Delete button will delete the product and all it's details from the website.

![Popular Horses(Logged In)](documentation/screenshots/desktop/product_detail_admin.png)

#### Shopping Bag Page(Admin Logged In)

* The Shopping Bag Page lists the all the products the user has added to their shopping bag.
* The page shows the image, product name, product price, quantity added and the subtotal for each product in the bag.
* There are two button under the quantity box for each item in the bag.
* The Update button allows the user to change the quantity for that item.
* When they click on the Update button the subtotal will also change.
* The Remove button allows the user to remove that item from their shopping bag.
* The bag total, delivery cost and grand total are displayed at the bottom of the page.
* The Keep Shopping button allows the user to return to the All Products page.
* The Secure Checkout button opens the Checkout page.

![Popular Horses(Logged In)](documentation/screenshots/desktop/shopping_bag_desktop.png)



#### Edit Booking Page

* The "Edit Booking Page" has a form similar to the "make booking" form.
* The user can change any of the six input field values and click on the "Update Booking" button.
* This will update the details of their booking in the database.
* The "Cancel" button allows the user to return to the "My Bookings Page".

![Edit Booking Page](documentation/screenshots/desktop/edit_booking.png)

#### Delete Booking Page

* A message is displayed to the user asking them if they are sure they want to delete this booking.
* Underneath are two buttons, "Confirm Delete" and "Cancel".
* The "Confirm Delete" button will delete the booking from the database.
* The "Cancel" button will return the user to the "My Bookings Page".

![Delete Booking Page](documentation/screenshots/desktop/delete_confirmation.png)

#### Signup, Login and Logout Pages

* The Signup Page contains a link to the "Login Page" to allow users who are already signed up to log in.
* The Login Page contains a link to the "Signup Page" to allow unregistered users to register an account.

![Signup Page](documentation/screenshots/mobile/register_mobile.png) ![Login Page](documentation/screenshots/mobile/login_mobile.png) ![Logout Page](documentation/screenshots/mobile/logout_mobile.png)


#### Footer

![Footer](documentation/screenshots/desktop/footer.png)

#### Feedback Messages

* Successfully Signed In

![Successfully Signed In Message](documentation/screenshots/desktop/messages/sign_in_success.png)

* Update Successful

![Update Successful Message](documentation/screenshots/desktop/messages/update_successful_bar.png)

* Booking Deleted Successfully

![Booking Deleted Successfully Message](documentation/screenshots/desktop/messages/delete_successful_bar.png)

* Horse Booked

![Horse Booked Message](documentation/screenshots/desktop/messages/horse_booked_bar.png)

* Lesson Time Booked

![Lesson Time Booked Message](documentation/screenshots/desktop/messages/lesson_time_booked_bar.png)

* Date Not Current

![Date Not Current Message](documentation/screenshots/desktop/messages/date_not_current_bar.png)

### Future Features
* Allow users to add reviews for each horse.
* Only allow lessons to be booked from Monday to Saturday.
* Allow instructors to login as admin users and assign horses to each booking.

[Back to Top](#electric-kitchens)

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