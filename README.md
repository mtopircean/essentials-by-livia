# Essentials by Livia
The website was create to support users interested in alternative medicine, more specifically in Essential Oils by doTerra.

It is a website intended to offer the users a valuable experience by being able to address certain ailments in a targeted way, through the filter by ailment section in "What is the best Essential Oil for me", and also give the user access to the latest offers from doTerra.

The projects main beneifiary is my wife who seeked a platform in which she can try and connect with both potential customers and also collaborators.
The website allows her to present the products to the marked through an easy to use and update platform. It also positions contact elements in several places and ways through the website to create fast channels of engagement with the user.

The website is done, but there is a multitude of elements that we still intend to update and upgrade.

![Alt text](/static/readme/am-i-responsive.png)

## CONTENT

* [The 5 Planes strategy](#the-5-planes-strategy)
    * [Overview](#overview)
    * [The Strategy Plane](#the-strategy-plane)
        * [Planning](#planning)
        * [Kanban Board](#kanban-board)
            * [Kanban overview](#kanban-overiew)
            * [Epics](#epics)
            * [Stories](#stories)
            * [Stories prioritization](#stories-prioritization)
            * [Milestones](#milestones)
            * [Sprints](#sprints)
    * [The Scope Plane](#the-scope-plane)
    * [The Structure Plane](#the-structure-plane)
        * [Features](#features)
            * [Special features implemented](#special-features-implemented)
            * [Features implemented](#features-implemented)
            * [Features future implementation](#features-future-implementation)
    * [The Skeleton Plane](#the-strategy-plane)
        * [Wireframes](#wireframes)
        * [Databases](#databases)
        * [Security](#security)
            * [Security User](#security-user)
            * [Security Admin](#security-admin)
    * [The Surface Plane](#the-surface-plane)
        * [Theme](#theme)
        * [Colour Selection](#colour-selection)
        * [Font and text style](#font-and-text-style)
        * [Imagery](#imagery)
        * [Display size optimization](#display-size-optimization)
        * [Accessibility](#accessibility)
* [Deployment](#deployment-and-local-development)
    * [How do Deploy](#how-to-deploy)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Technologies](#technologies)
    * [Programming Languages](#programming-languages)
    * [IDE](#ide)
    * [Other](#other)
* [Testing and Validation](#testing-and-validation)
    * [HTML](#html)
    * [CSS](#css)
    * [Accessibility Test](#accessibility-test)
    * [Lighthouse](#lighthouse)
    * [Spellcheck](#spellcheck)
    * [JavaScript](#javascript)
    * [Local functionality tests](#local-functionality-tests)
    * [Fixed bugs](#fixed-bugs-and-current-errors)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Other](#other)
* [About Author](#about-author)
# The 5 planes strategy
## Overview

## The Strategy Plane

### Planning
Planning was done following an Agile methodology by creating 6 Sprints focused around 7 milestones. They where highly connected to each other following a natural logic in regards of timing and development steps.

Status as of 09.12.2023:
* Kanban category
![Alt text](/static/readme/kanban-status.png)
* Milestone status
![Alt text](/static/readme/milestone-status.png)
* Label status
![Alt text](/static/readme/label-status.png)
* Label by milestone status
![Alt text](/static/readme/labels-milestones-status.png)
* Status by milestone
![Alt text](/static/readme/status-milestones-status.png)


### Kanban Board
Board was designed to cover all planning aspects and offer a structured process to takle and work on my project.
![Alt text](/static/readme/kanban-board.png)

#### Kanban overview
Kanban board is structured around 7 Epics connected to differrent functionalities, modules and stages of the project.
![Alt text](/static/readme/epics.png)

#### Epics
In total we have 7 epics:
* EPIC 1: Setup and Deployment- As a developer, I can install basic dependencies, create the document hierarchy/structure and deploy the application to Heroku so that the development environment is set up, and the application is accessible online for testing and use.

* EPIC 2: Database Setup and Management - As a developer, I can create the database structure, define models, and perform migrations so that the application has a robust and efficient database system, ensuring complete and easy to maintain data.

* EPIC 3: User Interface Design - As a user, I can access a well-designed website and interact with a user-friendly interface so that my browsing experience is intuitive and visually appealing.

* EPIC 4: User Account Management - As a user, I can create, access, update, and delete my user account, and administrators can view, update, and delete user accounts** so that user information is managed securely, and users and administrators have control over account-related key activities.

* EPIC 5: Promotion Management - As a user, I can view, share, comment on promotions and manage my favorites so that I can engage with promotions. As a administrator I can add, edit, delete promotions, and moderate comments so that I can have control over the promotion content and user interactions.

* EPIC 6: Product Search, Filtering, and Management - As a user, I can search and filter products by ailment and price, save and remove products from my favorites, and comment on products so that I can find relevant products easily and engage with the product portfolio in an efficient manner. As an administrator, I can add, modify, and delete products so that the product database is kept up-to-date and accurate.

* EPIC 7: Testing and Readme documents - As a developer, I can perform and document comprehensive testing on the application to ensure its functionality, reliability, and security so that the application bugs are identified, fixed or document, the application is stable, and secure for users to use. As a developer, I can complete a comprehensive README documentation that allows me to capture all essential concept, development and must-know information related to the project so that potential users, developers, etc. will be able to obtain all relevant information to support the use and other further developments on the application.

#### Stories

Story list here: [STORIES](https://github.com/mtopircean/essentials-by-livia/issues)

Attached to the 7 epics I`ve created aproximatley 43 stories structured around various prioritization methods:
* Milestones
* Sprints
* Importance priority
* Story points
* Kanban category:
    * To Do : Stories to be worked on but not allocated to a priority section
    * In Progress: Stories being worked on
    * Done: Stories completed
    * Closed: Stories with all tasks closed and closure is validated
    * Nice to be done: Future developments
    * Might be done: If time allowed, still to be done
* Epics:
    * Epic 1: 3 stories
    * Epic 2: 3 stories 
    * Epic 3: 7 stories
    * Epic 4: 9 stories
    * Epic 5: 8 stories
    * Epic 6: 9 stories
    * Epic 7: 2 stories

All user stories where completed and closed, the only ones remaining would be the stories allocated in the Nice to be done and Might be done categories:

* Nice to be done:
    * USER STORY: Approve comments on promotion
    * USER STORY: Comment promotion
    * USER STORY: Comment product
    * USER STORY: Filter products by price
    * USER STORY: Delete comments on promotion

* Might be done: 
    * USER STORY: Share promotion


Stories where then broken down into a structure that allowed for Acceptance criteria to be defined, as well as the story to be broken down in tasks to follow a systematic development as well as a way to track progress.

Bellow an example of a story:
![Alt text](/static/readme/story-example.png)

#### Stories prioritization
My goal in the development of the project was to deploy an Agile methodology, allowing importance on the strategic prioritization of user stories. This involved aligning tasks to optimize delivery, considering dependencies, user expectations, and business scope. 

There where 3 main categories of points:
* 3 points: middle complexity/middle effort, which in essence where the first effort allocated and became the control level
* 2 points: lower complexity/lower effort stories
* 5 points: higher complexity/higher effort
Ex: Based on this prioritization framework, the following sequence outlines the order in which the user stories would have been addressed:

    * Install basic dependencies (2 story points)
    * Create database structure (5 story points)
    * Create models (5 story points)
    * Create homepage (5 story points)
    * Create user account (5 story points)
    * Testing (5 story points)
    * README (5 story points)
    * Heroku (3 story points)
    * Create promotions page (5 story points)
    * ... (etc. ......)

A second system of prioritization was allocating a complexity label...which at the end connected well wil the story points system.

Thirdly, millestones and sprints also played a crucial role in prioritizing my stories and keeping control on the timing of my project.

Example:
![Alt text](/static/readme/story-example.png)

#### Milestones
6 Milestones where created structured around key steps in development process and structured around a clear and well ballanced timing:
![Alt text](/static/readme/milestones.png)

#### Sprints
Overall 6 sprints where considered, also closely connected to the 6 milestones, having the same logic behind their setup as the milestones.

## The Scope Plane
This website was created with a key element in mind, to create an attractive and efficient interaction point between the website owner and the users. Interaction main objective is to:
* Convert users into customers
* Convert users into partners by enrolling them as doTera ambasadors
Various contact methods and points help support this. They are placed in various key elements of the website.

For the website owner, the key focus point is to provide value to the user through various methods:
* The user of a tool that is able to recommend products based on ailments(available for registered users)
* Promotions page which allows users to see fast and efficient the monthly star products/deals
This all has to be available for fast upload and update, and it is through various methods:
* Front: via the website interface
* Back: in the admin panel by manual input or using the import/export options

## The Structure Plane
Structure and features of the website are organized around 2 concepts, concepts set in order to provide value to both the user and owner:
* Owner friendly
    * Easy to manage(as automated as possible):
        - key feature being the import-export function
        - data easy to update and upload even from front end
        - admin pannel easy accessible from navbar and with key admin areas identifiable in the admin interface
        - give value to obtain value, clearly identiable through the product recommandation function accessible to logged users
    * Easy to connect with the user(one click away from the user)
    * Upgradable and scalable with ease
        - the reuse of different elements within pages(navbar, base, footer html)
        - integration of battery included elements like allauth
* User friendly
    * Easy to navigate 
    * Key elements always on like footer, whatsapp contact
    * Easy to use filter section
    * Key information the key of the pages, with elements easiley identifiable and visible
    * Mobile friendly: taking advantage of the powerfull bootstrap

### Features

#### Special features implemented
SELECTIVE RECOMMENDATION TOOL:

Why this feature is special is because it offers the admin the option to selectively allow users to access the Recommandation tool, which is the biggest selling point of the website.
In essence, the process is as follows:

- user tries to access the tool and lands on a page requesting to create an account or login(this effects also the button leading to the tool in front-page)
- user creates an account and receives a notification that account is pending approval
- admin validates
- now user can acess the account
OR:
- user loggs in and now can access the account

![Alt text](/static/readme/selective-recommandation-tool.gif)


IMPORT-EXPORT ADMIN FUNCTIONALITY:
- admin can do mass imports/exports of the databases for products, ailments, promotions, in order to allow increased efficiency

![Alt text](/static/readme/import-export.gif)

#### Features implemented
                                                            **EPIC**                                                            |                                                        **STORY**                                                         | **Beneficiary** |                    **Link to feature**                    |                                       **Feature**                                       | **Status**
:------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:---------------:|:---------------------------------------------------------:|:---------------------------------------------------------------------------------------:|:----------:
          [EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design           |       [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43490085): Create error pages       |      User       |            [Error pages Feature](#error-pages)            |                        Created custom 403, 404, 500 error pages                         | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |  [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491254): Update a user account - user  |      User       |  [User account User Feature](#user-account-user-feature)  |        User can updated their account details directly from their profile page.         | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |  [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492404): Delete user accounts - admin  |      Admin      | [User account Admin Feature](#user-account-admin-feature) |                 Admin can delete a user account from the admin section.                 | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |  [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491124): Access a user account - user  |      User       |  [User account User Feature](#user-account-user-feature)  | After account creation, user can access their account details in their profile section. | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |     [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43490848): Create a user account      |      User       |  [User account User Feature](#user-account-user-feature)  |                 Users can create a user account by using a custom form.                 | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |  [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492224): Update user accounts -admin   |      Admin      | [User account Admin Feature](#user-account-admin-feature) |             Admin can update a users account details from the admin section             | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |  [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491438): Delete a user account - user  |      User       |  [User account User Feature](#user-account-user-feature)  |            User can delete their account straight from the profile section.             | Implemented
         [EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management          |       [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492086): View user accounts       |      Admin      | [User account Admin Feature](#user-account-admin-feature) |                    Admin can see all user accounts in admin section                     | Implemented
           [EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management           |         [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493399): View promotion         |      User       |     [Promotion User Feature](#promotion-user-feature)     |                            Users can view active promotions                             | Implemented
           [EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management           |         [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494603): Add promotion          |      Admin      |    [Promotion Admin Feature](#promotion-admin-feature)    |               Admin can add a promotion from front-end and also back-end.               | Implemented
           [EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management           |        [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494783): Delete promotion        |      Admin      |    [Promotion Admin Feature](#promotion-admin-feature)    |              Admin can delete a promotion from front-end and also back-end              | Implemented
           [EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management           |         [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494316): Edit promotion         |      Admin      |    [Promotion Admin Feature](#promotion-admin-feature)    |               Admin can edit a promotion from front-end and also back-end               | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management |         [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501011): Modify product         |      Admin      |      [Product Admin Feature](#product-admin-feature)      |                Admin can edit a product from front-end and also back-end                | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management |   [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499482): Filter products by ailment   |      User       |       [Product User Feature](#product-user-feature)       |                           User can filter products by ailment                           | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management | [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43500688): Add a product to the database  |      Admin      |      [Product Admin Feature](#product-admin-feature)      |                Admin can add a product from front-end and also back-end.                | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management |   [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499279): Search products by ailment   |      User       |       [Product User Feature](#product-user-feature)       |         User can filter products by ailment, by using the search functionality          | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management |         [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501144): Delete product         |      Admin      |      [Product Admin Feature](#product-admin-feature)      |               Admin can delete a product from front-end and also back-end               | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management |   [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499704): Save product to favorites    |      User       |          [Favorites Feature](#favorites-feature)          |            User can save a product to their favorites in the profile section            | Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management | [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499821): Remove products from favorites |      User       |          [Favorites Feature](#favorites-feature)          |          User can remove a product from their favorites in the profile section          | Implemented
       [Epic 7](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368946): Testing and Readme documents       |            [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501838): Testing             |      Admin      |           [Unittest Feature](#unittest-feature)           |                       Write unittest for automated views testing                        | Implemented

#### Error pages

#### Favorites Feature
![Alt text](https://res.cloudinary.com/dgcwnjoh4/image/upload/v1702687524/gifs/favorite-feature_baplqu.gif)

#### Product Admin Feature
![Alt text](/static/readme/product-admin-feature.gif)

#### Product User Feature
![Alt text](https://res.cloudinary.com/dgcwnjoh4/image/upload/v1702687522/gifs/product-user-feature_hzrxcw.gif)

#### Promotion Admin Feature
![Alt text](/static/readme/promotion-admin-feature.gif)

#### Promotion User Feature
![Alt text](/static/readme/promotion-user-feature.gif)

#### User Account Admin Feature
![Alt text](/static/readme/admin-user-account-feature.gif)

#### User Account User Feature
![Alt text](/static/readme/admin-user-account-feature.gif)

#### Unittest Feature


#### Features future implementation

Future iteration will include this features. For the moment, Stories are also at a lower detail level, without tasks and major details.

                                                 **EPIC**                                                  |                                                        **STORY**                                                        | **Beneficiary** | **Link to feature** |                                                                      **Feature**                                                                       |      **Status**
:---------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|:---------------:|:-------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------:
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management | [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43495025): Approve comments on promotion |      Admin      |         n/a         |                                       Admin will have the ability to approve comments before they are displayed.                                       | Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management |       [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493955): Comment promotion       |      User       |         n/a         |                                       User will have in the future the ability to add a commend on a promotion.                                        | Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management |        [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43500159): Comment product        |      User       |         n/a         |                                        User will have in the future the ability to add a commend on a product.                                         | Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management |   [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499620): Filter products by price    |      User       |         n/a         | User will have in the future the ability to filter a product by price. Price value can be added now on the product, but it is currently not displayed. | Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management | [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43495274): Delete comments on promotion  |      Admin      |         n/a         |                                       Admin will have the ability to delete comments on a promotion and product.                                       | Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management |        [USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493641): Share promotion        |      User       |         n/a         |                                              User will have the ability to share a promotion or product.                                               | Future implementation


## The Structure Plane

## The Skeleton Plane
### Wireframes
To support both the functionality and the design part of the website, followin wireframes where created:
* Index Page
![Alt text](/static/readme/wireframes/index.png)
* About Me Page
![Alt text](/static/readme/wireframes/about-me.png)

* About Oils Page
![Alt text](/static/readme/wireframes/about-oils.png)

* Login Modal
![Alt text](/static/readme/wireframes/login-modal.png)

* Profile Page
![Alt text](/static/readme/wireframes/profile.png)

* Registration Page
![Alt text](/static/readme/wireframes/register.png)

* Registration confirmation Page
![Alt text](/static/readme/wireframes/registration-confirmation.png)

* Contact Page
![Alt text](/static/readme/wireframes/contact.png)

* Recommended product Page
![Alt text](/static/readme/wireframes/recommended.png)

* Recommended product Page for users logged out
![Alt text](/static/readme/wireframes/recommended-logged-out.png)

* Recommended product Page for users logged in but not approved
![Alt text](/static/readme/wireframes/recommended-not-approved.png)

* Promotions page
![Alt text](/static/readme/wireframes/promotions.png)

* Allauth customized forms Pages
![Alt text](/static/readme/wireframes/allauth-forms.png)

* Customized error pages
![Alt text](/static/readme/wireframes/error-pages.png)

* Modal to support add product and promotion from front page
![Alt text](/static/readme/wireframes/add-product-promotion-modal.png)



### Databases

Database links into Django user and links mainly into the AppUser database.
It was a conscious decission to allow the admin to be able to update only the Approved section from the backend inside the AppUser.
All other actions are to be taken within the User section to minimize potential disturbance to the database.

Databases all link into each other, Ailment having a Many to One relationship with AddProduct.

The only standalone database is AddPromotion which doesn`t need any specific input in other section/databases in order to run.

![Alt text](/static/readme/database-diagram.png)

### Security
#### Security User

The HTML template ensures user safety by controlling user access based on approval status. For instance, conditional checks are in place to restrict unauthorized access to certain sections, utilizing is_user_approved.
For example:

``` html
{% if is_user_approved or is_admin %}
    <!-- User-approved or admin-specific content here -->
{% else %}
    <!-- Content for unauthorized users -->
{% endif %}
```
The views in Django are protected with decorators, like for ex @login_required and @staff_member_required to ensure user authentication and administrative privilege.
``` python
@login_required
def favourite_selection(request, product_id):
    # Code to manage favorite products securely...
``` 

{% csrf_token %} tag generates a unique token for each form submission to protect data being sent by the user. For example:
``` html
<form method="POST" action="{% url 'filter_ailments' %}" id="ailment-filter-form">
    {% csrf_token %}
    <!-- Other form fields and buttons -->
</form>
```

The use of eventlisteners is present through the code, with the goal to promt the user on critical changes to their data:

``` html
<div id="account-actions" class="text-center" id="profile-button-container">
                            <form id="edit-profile-form" method="post" action="{% url 'edit_profile' %}">
                                {% csrf_token %}
                                <button id="save-profile" type="submit" onclick="return confirm('Are you sure you want to update your account?')">Save Changes</button>
                            </form>
                            <form id="delete-account-form" method="post" action="{% url 'delete_account' %}">
                                {% csrf_token %}
                                <button id="delete-account" type="submit" onclick="return confirm('Are you sure you want to delete your account?')">Delete Account</button>
                            </form>
                        </div>
```

#### Security Admin
Certain sections in the HTML are available only to admin users, like for example, controlled using conditional checks with user.is_staff.

``` html
{% if user.is_staff %}
    <!-- Content available only to admin users -->
{% else %}
    <!-- Content for non-admin users -->
{% endif %}
```
View functions in Django incorporate @staff_member_required to ensure only staff (admin) members can access and manage certain functionalities.

``` python
@staff_member_required
def user_approval(request):
    # Admin-only functionality to approve users...
```

The use of eventlisteners is present through the code, with the goal to promt the admin on critical changes to the forms/databases, like for example:
``` html
<form id="delete-product-form" action="{% url 'delete_product' product.id %}" method="post">
    {% csrf_token %}
    <!-- Other form fields and buttons -->
    <button id="delete-product" type="submit">Delete Product</button>
</form>
```

## The Surface Plane
### Theme
When considering the website theme the general idea was to provide a clean, modern look, but maintain also a good level of elegance.
This was achieved through a well though color selection, limitation on number of elements displayed, and a high use of bootstrap to allow proper alignment and element display in the page.
Photos and graphic elements used where aligned to the nature and health tematic, but again, maintaining the same clean direction.

### Colour Selection
Colours where selected in line with the theme, but also to offer a high level of accessibility and contrast. It has suffered several changes during the development process as I`ve tried to maintain data clear, easy to read and print. The choice was also due to the amount of features present on the website and the interest to create a separation, or a unique identifier to separate them visually.

List of colours used:
![Alt text](/static/readme/color-palette.png)

### Font and text style
Text and font used are consistent across the website with variances in regards of decoration and size. Font used was selected from Google Fonts:
![Alt text](/static/readme/font.png)

### Imagery
Logo was designed using Canva website.
Photos for website elements are taken from Pexels.
Product and promotion photos are taken from doTerra database/representative tools.

### Display size optimization
### Accessibility
From an accessibility perspective, my goal was to create a clean website with data easy to read, positioned in a relevant manner for the user. I`ve achieved this by:

Writing semantic HTML
Correct selection of text size, font and style in order to contrast well with the other elements of the page.
Highly visible and relevant logo.
Use of alt attribute connected to the logo.
Another area I was mindful of, was that all of the consideration above where not lost when using the website in smaller screen sizes.

Display size optimization:
![Alt text](/static/readme/am-i-responsive.png)

# Deployment
## How do Deploy
## How to Fork
## How to Clone

# Technologies
## Programming Languages
## IDE
## Other

# Testing and Validation
## HTML
## CSS
## Accessibility Test
## Lighthouse
## Spellcheck
## JavaScript
## Python
## Local functionality tests
## Fixed bugs

# Credits
## Code Used
## Other
* Deployment instructions in GitHub copied from kera-cudmore different repo and following the article written by her on how to write a readme.
* Inspiration on readme structure taken from kera-cudmore repo`s and following the article written by her on how to write a readme.

* Thanks to Graeme Taylor, my mentor for all his support during the development of the project.
* Thank you to the CI Tutor Team who supported in several instances by providing guidance on overcoming various challenges encountered during development. Massive support from all of the team and special thanks to: Roman, Gemma, John, Martin, Sarah, Jason, Joanne, Holly, Oisin....my apologies if I forgott someone....this is only due to my bad memory :).

# About Author
Marius Topircean is an aspiring software-developer on a journey to develop and learn his place into the developer community.

My contact details are:

Email: mtopircean@yahoo.com

Phone: +353857642212

Slack: Marius Topircean

GitHub: mtopircean

LinkedIn: [Marius Topircean](https://www.linkedin.com/in/marius-t-7b5592124)


