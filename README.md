# Essentials by Livia
The website was create to support users interested in alternative medicine, more specifically in Essential Oils by doTerra.

It is a website intended to offer the users a valuable experience by being able to address certain ailments in a targeted way, through the filter by ailment section in "What is the best Essential Oil for me", and also give the user access to the latest offers from doTerra.

The projects main beneifiary is my wife who seeked a platform in which she can try and connect with both potential customers and also collaborators.
The website allows her to present the products to the marked through an easy to use and update platform. It also positions contact elements in several places and ways through the website to create fast channels of engagement with the user.

The website is done, but there is a multitude of elements that we still intend to update and upgrade.
## CONTENT

* [The 5 Planes strategy](#the-5-planes-strategy)
    * [Overview](#overview)
    * [The Strategy Plane](#the-strategy-plane)
        * [Objective](#objective)
        * [Planning](#planning)
        * [Kanban Board](#kanban-board)
            * [Kanban overview](#kanban-overiew)
            * [Epics](#epics)
            * [Stories](#stories)
            * [Stories prioritization](#stories-prioritization)
            * [Milestones](#milestones)
            * [Sprints](#sprints)
    * [The Scope Plane](#the-scope-plane)
        * [Features](#features)
            * [Features implemented](#features-implemented)
            * [Features future implementation](#features-future-implementation)
    * [The Structure Plane](#the-scope-plane)
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
### Objective

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
### Features

#### Features implemented

#### Features future implemented

## The Structure Plane

## The Skeleton Plane
### Wireframes

### Databases

### Security
#### Security User
#### Security Admin

## The Surface Plane
### Theme
### Colour Selection
### Font and text style
### Imagery
### Display size optimization
### Accessibility

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

# About Author


