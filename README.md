# Essentials by Livia
The website was create to support users interested in alternative medicine, more specifically in Essential Oils by doTerra.

It is a website intended to offer the users a valuable experience by being able to address certain ailments in a targeted way, through the filter by ailment section in "What is the best Essential Oil for me", and also give the user access to the latest offers from doTerra.

The projects main beneifiary is my wife who seeked a platform in which she can try and connect with both potential customers and also collaborators.
The website allows her to present the products to the marked through an easy to use and update platform. It also positions contact elements in several places and ways through the website to create fast channels of engagement with the user.

The website is done, but there is a multitude of elements that we still intend to update and upgrade.

![Alt text](/static/readme/am-i-responsive.png)

## CONTENT

* [The 5 Planes strategy](#the-5-planes-strategy)
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
    * [External Python Modules](#external-python-modules)
    * [IDE](#ide)
    * [Other](#other)
* [Testing and Validation](#testing-and-validation)
    * [HTML](#html)
    * [CSS](#css)
    * [Accessibility Test](#accessibility-test)
    * [Lighthouse](#lighthouse)
    * [Spellcheck](#spellcheck)
    * [JavaScript](#javascript)
    * [Python](#python)
        * [Linter](#linter)
        * [Unittest](#unittest)
            * [Static Pages](#static-pages)
            * [Decorator Limitation](#decorator-limitations)
    * [Local functionality tests](#local-functionality-tests)
    * [Fixed bugs](#fixed-bugs-and-current-errors)
* [Credits](#credits)
    * [Code Used](#code-used)
    * [Other](#other)
* [About Author](#about-author)
# The 5 planes strategy
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

EDITOR FILTER FOR ADMIN:
- admin can navigate easier to the relevant section in the product list to edit the product. I`ve changed the filter to a product panel as the filter was irelevant for the administrator:

![Alt text](/static/readme/admin-navigator.png)


EASY CONTACT:
- Always on WhatsApp

![Alt text](/static/readme/on-wsapp.png)

PERSONALIZED PAGES:
Various pages are personalized to my websites style, like the registration form(although it uses allauth standards at some level...)
I`ve created a special form separate to allauth one:

```python
class CustomSignupForm(SignupForm):
    """
    Created customized sign up form including
    some specific elements to my application in addition to allauth own
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=300)
    phone_number = forms.CharField(max_length=20)
    username = forms.CharField(max_length=100)
    join_team = forms.BooleanField(required=False)
    i_want_to_know_more_about_the_products = forms.BooleanField(required=False)

    def save(self, request):
        # Save the user with the standard existing method
        user = super(CustomSignupForm, self).save(request)

        # Pull the cleaned data
        user_data = self.cleaned_data

        # Update the users with the input data
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.email = user_data['email']
        user.username = user_data['username']

        # Save the user
        user.save()

        # Creates the AppUser object
        app_user = AppUser.objects.create(
            user=user,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            phone_number=user_data['phone_number'],
            username=user_data['username'],
            join_team=user_data['join_team'],
            i_want_to_know_more_about_the_products=(
                user_data['i_want_to_know_more_about_the_products']
            )
        )

        return user
```

FEATURES----Intentional limitations:

- Admin has view only rights for AppUser in admin section. Any changes need to be operated in the User section in Admin.
- Only areas in the product section and promotion section are the descriptions. Anything else needs to be updated from administrator panel in order to avoid massive database disruption.

#### Features implemented

**EPIC**|**STORY**|**Beneficiary**|**Impact on beneficiary**|**Link to feature**|**Feature**|**Status**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
[EPIC 1](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366122): Setup and Deployment|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43485934): Install basic dependencies|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 1](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366122): Setup and Deployment|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43486612): Heroku deployment|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 1](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366122): Setup and Deployment|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43487110): Create a document hierarchy and structure|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 2](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366525): Database Setup and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43488004): Create models|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 2](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366525): Database Setup and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43488175): Migrate models|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 2](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366525): Database Setup and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43487683): Create database structure|Developer|Obtaining robust development process which will ensure easire future development.|n/a| |n/a
[EPIC 2](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43366525): Database Setup and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43488872): Create template for header, footer, and modals|Website owner|Allow easier future development|n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43488654): Create promotions page|User/Admin|Allow for a section to view promotions if user, post, edit, remove and add promotions if you are an administrator.|n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43490514): Create user registration form|User/Admin|Allow for a section for the user to register in order to save favorites and access the recommandation tool. Allow for the administrator to collect user data and use them to create a database of users.|n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=44232904): Create user account page|User|Allows the user to generate a self manageable account page.|n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43489328): Create recommendation tool layout|User/Admin| |n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43488488): Create homepage|User| |n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43489691): Create registration form|User| |n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43490085): Create error pages|User| |[Error pages Feature](#error-pages)|Created custom 403, 404, 500 error pages|Implemented
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43704528): Create about me page|User| |n/a| |n/a
[EPIC 3](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367302): User Interface Design|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43704731): Create about oils page|User| |n/a| |n/a
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491254): Update a user account - user|User| |[User account User Feature](#user-account-user-feature)|User can updated their account details directly from their profile page.|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492404): Delete user accounts - admin|Admin| |[User account Admin Feature](#user-account-admin-feature)|Admin can delete a user account from the admin section.|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491124): Access a user account - user|User| |[User account User Feature](#user-account-user-feature)|After account creation, user can access their account details in their profile section.|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43490848): Create a user account|User| |[User account User Feature](#user-account-user-feature)|Users can create a user account by using a custom form.|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492224): Update user accounts -admin|Admin| |[User account Admin Feature](#user-account-admin-feature)|Admin can update a users account details from the admin section|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491438): Delete a user account - user|User| |[User account User Feature](#user-account-user-feature)|User can delete their account straight from the profile section.|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43492086): View user accounts|Admin| |[User account Admin Feature](#user-account-admin-feature)|Admin can see all user accounts in admin section|Implemented
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491694): Create super-user|Admin| |n/a| |n/a
[EPIC 4](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367544): User Account Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43491915): Create admin environment|Admin| |n/a| |n/a
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493399): View promotion|User| |[Promotion User Feature](#promotion-user-feature)|Users can view active promotions|Implemented
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494603): Add promotion|Admin| |[Promotion Admin Feature](#promotion-admin-feature)|Admin can add a promotion from front-end and also back-end.|Implemented
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494783): Delete promotion|Admin| |[Promotion Admin Feature](#promotion-admin-feature)|Admin can delete a promotion from front-end and also back-end|Implemented
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43494316): Edit promotion|Admin| |[Promotion Admin Feature](#promotion-admin-feature)|Admin can edit a promotion from front-end and also back-end|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501011): Modify product|Admin| |[Product Admin Feature](#product-admin-feature)|Admin can edit a product from front-end and also back-end|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499482): Filter products by ailment|User| |[Product User Feature](#product-user-feature)|User can filter products by ailment|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43500688): Add a product to the database|Admin| |[Product Admin Feature](#product-admin-feature)|Admin can add a product from front-end and also back-end.|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499279): Search products by ailment|User| |[Product User Feature](#product-user-feature)|User can filter products by ailment, by using the search functionality|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501144): Delete product|Admin| |[Product Admin Feature](#product-admin-feature)|Admin can delete a product from front-end and also back-end|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499704): Save product to favorites|User| |[Favorites Feature](#favorites-feature)|User can save a product to their favorites in the profile section|Implemented
[EPIC 6](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368046): Product Search, Filtering, and Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499821): Remove products from favorites|User| |[Favorites Feature](#favorites-feature)|User can remove a product from their favorites in the profile section|Implemented
[Epic 7](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368946): Testing and Readme documents|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43502068): README|Admin| |n/a| |n/a
[Epic 7](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43368946): Testing and Readme documents|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43501838): Testing|Admin| |[Unittest Feature](#unittest-feature)|Write unittest for automated views testing|Implemented

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

Unitest basis was setup and can be found here, linking to the test area: [Unittest](#unittest)


#### Features future implementation

Future iteration will include this features. For the moment, Stories are also at a lower detail level, without tasks and major details.

**EPIC**|**STORY**|**Beneficiary**|**Link to feature**|**Feature**|**Status**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43495025): Approve comments on promotion|Admin|n/a|Admin will have the ability to approve comments before they are displayed.|Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493955): Comment promotion|User|n/a|User will have in the future the ability to add a commend on a promotion.|Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43500159): Comment product|User|n/a|User will have in the future the ability to add a commend on a product.|Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43499620): Filter products by price|User|n/a|User will have in the future the ability to filter a product by price. Price value can be added now on the product, but it is currently not displayed.|Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43495274): Delete comments on promotion|Admin|n/a|Admin will have the ability to delete comments on a promotion and product.|Future implementation
[EPIC 5](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43367676): Promotion Management|[USER STORY](https://github.com/users/mtopircean/projects/10?pane=issue&itemId=43493641): Share promotion|User|n/a|User will have the ability to share a promotion or product.|Future implementation

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

```html
{% if is_user_approved or is_admin %}
    <!-- User-approved or admin-specific content here -->
{% else %}
    <!-- Content for unauthorized users -->
{% endif %}
```
The views in Django are protected with decorators, like for ex @login_required and @staff_member_required to ensure user authentication and administrative privilege.
```python
@login_required
def favourite_selection(request, product_id):
    # Code to manage favorite products securely...
``` 

```html
{% csrf_token %}
```
tag generates a unique token for each form submission to protect data being sent by the user. 

For example:

```html
<form method="POST" action="{% url 'filter_ailments' %}" id="ailment-filter-form">
    {% csrf_token %}
    <!-- Other form fields and buttons -->
</form>
```

The use of eventlisteners is present through the code, with the goal to promt the user on critical changes to their data:

```html
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

```html
{% if user.is_staff %}
    <!-- Content available only to admin users -->
{% else %}
    <!-- Content for non-admin users -->
{% endif %}
```
View functions in Django incorporate @staff_member_required to ensure only staff (admin) members can access and manage certain functionalities.

```python
@staff_member_required
def user_approval(request):
    # Admin-only functionality to approve users...
```

The use of eventlisteners is present through the code, with the goal to promt the admin on critical changes to the forms/databases, like for example:

```html
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

!!!NOTE: Due to accessibility issues, changed color code for blue to #077386;

### Font and text style
Text and font used are consistent across the website with variances in regards of decoration and size. Font used was selected from Google Fonts:
![Alt text](/static/readme/font.png)

### Imagery
Logo was designed using Canva website.
Photos for website elements are taken from Pexels.
Product and promotion photos are taken from doTerra database/representative tools.

### Display size optimization
The use of Bootstrap has limited significantly the level of manual intervention I had to do in order to adapt the layout to various screen sizes.
My intervention was limited to an intervention on this two particular sizes, which managed to adapt to all screen variations under them:

``` css
@media (max-width: 767px)
```
``` css
@media (max-width: 992px) /*minor intervention for padding adjustment
```

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
Deployment of the website was done using HEROKU, and can be accessed here [ESSENTIALS BY LIVIA](https://essentials-by-livia-efe89c429260.herokuapp.com/).

## How to Fork
To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/essentials-by-livia](https://github.com/mtopircean/essentials-by-livia)
3. Click the Fork button in the top right corner.

## How to Clone
To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/essentials-by-livia](https://github.com/mtopircean/essentials-by-livia)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

# Technologies
## Programming Languages
1. HTML
2. CSS
3. JavaScript
4. JQuery
5. Python

## External Python Modules
* asgiref==3.7.2 : Installed with others
* cloudinary==1.36.0 : interaction with cloudinary media management
* diff-match-patch==20230430 : Installed with others
* dj-database-url==0.5.0 : supports database usage in Django
* dj3-cloudinary-storage==0.0.6: Django storage in cloudinary
* Django==3.2.22 : actual Django variant
* django-allauth==0.58.2 : Application managing authentification, registration and account management
* django-heroku==0.3.1 : simplifies deployment to Heroku
* django-import-export==3.3.1 : Excel import export database integration
* django-summernote==0.8.20.0 : Summernote integration
* et-xmlfile==1.1.0 : Used to read and write excels
* gunicorn==21.2.0 : Python server for running applications on web
* MarkupPy==1.14 : Installed with others
* oauthlib==3.2.2 : Installed with others
* odfpy==1.4.1 : Installed with others
* openpyxl==3.1.2 : Used to read and write excels
* psycopg2==2.9.9 : PostgresSQL adapter to interact with databases
* PyJWT==2.8.0 : Installed with others
* python3-openid==3.2.0 : Installed with others
* pytz==2023.3.post1 : Installed with others
* requests-oauthlib==1.3.1 : Python request library
* sqlparse==0.4.4 : Python parser
* tablib==3.5.0 : Installed with others
* whitenoise==6.6.0 : Supports serving of static files in Django apps
* xlrd==2.0.1 : Read and format data from excels
* xlwt==1.3.0 : Read and format data from excels


## IDE
1. GitHub: to store the source code.
2. GitPod: support to write majority of code, deploy via Heroku, and push data to store in GitHub. Gitpod was used also for debugging purposes.
3. Git: Used to push code

## Other
1. HEROKU: to deploy application and act as the app interface
2. CI Python Linter: to validate code format.
3. drawSQL: to create the database diagram
1. Canva: support with logo creation.
2. Font Awesome: support with icon for various html pages
3. Google Font: support with font style used for website text.
4. Balsamiq: support with wireframe creation.
7. Google DevTools: support with CSS styling, troubleshooting and responsive design development; support with testing function execution/js functionality.
8. Lighthouse: performance testing .
9. W3C Spell Checker: webpage spelling checks.
10. WAVE Web Accessibility Evaluation Tools: for accessibility evaluation.
11. CSS Validation Service: for CSS code evaluation and troubleshooting.
12. W3C Markup Validation Service: for HTML code evaluation and troubleshooting.
13. JSHint JavaScript Validator: to verify and improve Java Script code.
14. Colors: to create palette of colours in README.
15. Amiresponsive: to create a snapshot of the page responsiveness on different screen variations

# Testing and Validation
## HTML

* About me
![Alt text](/static/readme/about-me-html-test.png)

* Profile
![Alt text](/static/readme/profile-html-test.png)

* About oils
![Alt text](/static/readme/about-oils-html-test.png)

* Contact
![Alt text](/static/readme/contact-html-test.png)

* Index
![Alt text](/static/readme/index-html-test.png)

* Promotions
![Alt text](/static/readme/promotions-html-test.png)

* Register
![Alt text](/static/readme/register-html-test.png)

* What is the best essential oil for me (recommended.html) approved user
![Alt text](/static/readme/recommended-html-test.png)

* Error Pages
![Alt text](/static/readme/error-html-test.png)

## CSS

Code tested without any errors found:

![Alt text](/static/readme/css-validator.png)

## Accessibility Test
Majority of pages tested with the exception of pages which are user restricted that I was not able to test due to CSRF not allowing me to test.
For those, I`ve used the Lighthouse testing method.
* About me

![Alt text](/static/readme/about-me-accessibility.png)

* About oils

![Alt text](/static/readme/about-oils-accessibility.pngg)

* Contact

![Alt text](/static/readme/contact-accessibility.png)

* Index

![Alt text](/static/readme/index-accessibility.png)

* Password reset(generally applicable to allauth forms)

![Alt text](/static/readme/password-reset-accessibility.png)

* Promotions

![Alt text](/static/readme/promotions-accessibility.png)

* What is the best essential oil for me (recommended.html) - for users not logged in

![Alt text](/static/readme/recommended-not-logged-in-accessibility.png)

* Register
Which brought an issue present generally in allauth forms around labeling issues(since I`m using another form).

![Alt text](/static/readme/register-accessibility.png)

* What is the best essential oil for me (recommended.html) - not approved

Accessibility not perfect due to menu label not visible in mobile mode.

![Alt text](/static/readme/recommended-logged-in-not-appproved-accesibility.png)


* What is the best essential oil for me (recommended.html) approved

In addition to menu label not visible, the faded color on add to favorites reduces the score.

![Alt text](/static/readme/recommended-approved-accesibility.png)

* Profile

![Alt text](/static/readme/profile-desktop-lighthouse.png)

## Lighthouse
* About me

Desktop

![Alt text](/static/readme/about-me-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/about-me-mobile-lighthouse.png)

* Profile

Desktop

![Alt text](/static/readme/profile-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/profile-mobile-lighthouse.png)

* About oils

Desktop

![Alt text](/static/readme/about-oils-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/about-oils-mobile-lighthouse.png)

* Contact

Desktop

![Alt text](/static/readme/contact-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/contact-mobile-lighthouse.png)

* Index

Desktop

![Alt text](/static/readme/index-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/index-mobile-lighthouse.png)

* Allauth Forms

Desktop

![Alt text](/static/readme/allauth-forms-customized-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/allauth-forms-customized-mobile-lighthouse.png)

* Promotions

Desktop

![Alt text](/static/readme/promotions-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/promotions-mobile-lighthouse.png)

* What is the best essential oil for me (recommended.html) - for users not logged in

Desktop

![Alt text](/static/readme/recommended-not-logged-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/recommended-not-logged-mobile-lighthouse.png)

* Register

Desktop

![Alt text](/static/readme/recommended-logged-in-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/recommended-logged-in-mobile-lighthouse.png)

* What is the best essential oil for me (recommended.html) - not approved

Desktop

![Alt text](/static/readme/recommended-not-approved-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/recommended-not-approved-mobile-lighthouse.png)

* Register

Desktop

![Alt text](/static/readme/register-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/register-mobile-lighthouse.png)


* What is the best essential oil for me (recommended.html) approved

Desktop

![Alt text](/static/readme/recommended-logged-in-desktop-lighthouse.png)

Mobile

![Alt text](/static/readme/recommended-logged-in-mobile-lighthouse.png)


## Spellcheck

All pages, including the code have passed through word spellchecked and all issues corrected, except code command syntax. One particular spelling error was not corrected as it would have heavily affected the code. In various views which touch on the favorite section, there was the word favorite misspelled as favourite. For application integrity, this remained as it is and will be corrected in future itterations.
As a final check pages have passed through the W3C Spell Checked and the only words highlighted where specific names like doTerra, GDPR, WhatsApp, etc.

![Alt text](/static/readme/spellchecker.png)

## JavaScript
JSHINT:
script.js tested with following results:
![Alt text](/static/readme/jshint.png)

Variables marked as unused or undefined are in fact used and called on click in various areas of the code.
```JavaScript
/*jshint esversion: 6 */
/* global $ */
```
where used to manage following warnings from JSHint:
'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
one undefined variable $

## Python
### Linter
Following pages where tested with CI Linter: admin.py, forms.py, middleware.py, models.py, resources.py, test.py, urls.py, views.py:

![Alt text](/static/readme/linter-no-errors.png)


### Unittest

To run testing use local database!

To support basic testing activities, I`ve created unittest scenarios for the load of static pages and access restrictions where I have defined decorators in my views to limit interactions.
#### Static pages

TESTING CODE:

```python
class StaticPages(TestCase):

    def test_index_page_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_oils_view(self):
        response = self.client.get(reverse('about_oils'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-oils.html')
        
    def test_about_me_view(self):
        response = self.client.get(reverse('about_me'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-me.html')
        
    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_promotions_success_view(self):
        response = self.client.get(reverse('promotions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promotions.html')
        
    def test_recommended_view(self):
        response = self.client.get(reverse('recommended'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recommended.html')
    
    
    def test_data_protection_view(self):
        response = self.client.get(reverse('data_protection'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'data-protection.html')
        
    def test_404_error_view(self):
        response = self.client.get('/404/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        
    def test_403_error_view(self):
        response = self.client.get('/403/')
        self.assertEqual(response.status_code, 403)

    def test_500_error_view(self):
        with self.assertRaises(Exception):
            self.client.get('/500/')
```

Defined views to simulate the errors:
```python
def custom_403_handler(request, exception):
    return render(request, '403.html', status=403)

def simulated_403_view(request):
    return HttpResponseForbidden()

def simulated_500_view(request):
    raise Exception("Simulated 500 error")
```

Created urls
```python
#Urls created for testing purpose:
    path('403/', simulated_403_view, name='simulated_403'),
    path('500/', simulated_500_view, name='simulated_500'),

handler403 = custom_403_handler
```

Result:
```python
----------------------------------------------------------------------
Ran 11 tests in 0.144s

OK
...
```

#### Decorator limitations

Will become part of future development.
Thiw was not completed due to timing issues in handing over the project and the high complexity of the project.

## Local functionality tests

[TESTING.md](https://github.com/mtopircean/essentials-by-livia/blob/main/TESTING.md)

## Bugs

### Fixed bugs

* Connection not closing issue.
ISSUE:
Elephant SQL not closing connections.

Took inspiration on solution from stackoverflow and is reflected in the code bellow(an insert is also present in my settings file):

```python
class CloseConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.close_database_connection()
        return response

    def close_database_connection(self):
        if connection and connection.connection:
            connection.close()
```
```python
'website.middleware.CloseConnectionMiddleware',
```

* Arrow simbol for hidden expandable areas had to be changed to a symbol readable by the mobile devices, expecially in chrome
![Alt text](/static/readme/drop-down-arrow.png)

* Filter reset was managing to remove the filters when you where selecting a product as favorite, but wasn`t reseting the checked boxes.
Solution bellow manages to check the local storage for favorited items and if condition is meet, unchecks the filter boxes

```Javascript
if (localStorage.getItem('favoriteActionOccurred') === 'true') {
        $('.filter-checkbox').prop('checked', false);
        localStorage.removeItem('favoriteActionOccurred');
    }
```

* Filter list not staying on if click in the search ailment section and trying to type an ailment. Basically, keyboard in mobile overwrites the filter list.
Solution came as various lines of code overwritting the keyboard focus:

```Javascript
 var keyboardFocused = false;
```

### Open bugs

* Currently, once user regiters they are prompted to login again before account creation is confirmed.
* Once a user is prompted that the login details are incorect, if they choose to sign up or forgot pasword and want to return to previous page by pushing the back button, they receive an error:

![Alt text](/static/readme/redirect-one.png)
![Alt text](/static/readme/redirect-two.png)


* In filter section, once you add a product to favorites and page refreshes, the checked boxes for the filters remain active, but all products are displayed until you click on apply all again or clear all:
![Alt text](/static/readme/before-favorites.png)
![Alt text](/static/readme/after-favorites.png)

* Although not an issue/bug, using in limited scenarios url`s guided to a template, like bellow:

* Filtering function in the recommandation tool(What oil is suitable for me) acts a bit fidgety in mobile version.

```python
path('user-account.html', views.user_account,
         name='user_account'),
```

* In the profile page, if you have a product selected as favorite and you operate a change to your profile content, the page refreshes without the favorite item visible.
If you refresh the page again, it will show the product. I believe it to be a caching issue.

* HTML Validator has brought several issues, mostly due to data being pulled repetative through django inquiries and populating data in the page. I haven`t made massive changes as I do not have the time at the moment to optimize it. This will be done in future iterations.

* No console errors, just a message which I haven`t addressed due to time constraints:
![Alt text](/static/readme/message-console.png)

# Credits

## Code Used
* First of all thank you to all the Tutors and my mentor for their support. They have helped me with various solutions to my problems.

* Connection not closing issue.
ISSUE:

Elephant SQL not closing connections.

Took inspiration on solution from stackoverflow and is reflected in the code bellow(an insert is also present in my settings file):

```python
class CloseConnectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.close_database_connection()
        return response

    def close_database_connection(self):
        if connection and connection.connection:
            connection.close()
```
```python
'website.middleware.CloseConnectionMiddleware',
```

* Guidance has been taken from online enviorement on various solutions to issues, but no code was copied, just guidance on potential solutions.

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


