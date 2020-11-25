# MealPlanner

## Authors

Antonio Silva Paucar, Lindsay Marean, Bria Gray, Max Aguirre

## Description

This is a tool for planning communal meals. The application was designed built with communal housing and hiking trips in mind.

With the app, the user can create "meal plans," with which they can plan meals (Breakfast, Lunch, Snacks, Dinner) for any number of days they want.

The current functionality of the application allows users to create "dishes" and cook profiles, which can then be set to each meal.

Our application is hosted on Heroku, and can be accessed by going to https://meal-planner-app1.herokuapp.com/

For information on how the application works, see "Program Structure and Build Process Summary" below

## Usage

For a detailed user's guide with screenshots, see docs/User_guide.pdf. 

Briefly, there are two types of users, a planner and a cook. A planner builds a mealplan template ("Create a meal plan") by naming a plan, selecting start and end dates, and selecting needed meals for each date. The planner may optionally populate the plan with cooks and recipes to be assigned to different meals. A cook signs up ("Sign up on a meal plan") by selecting the mealplan, and then scrolling to a particular meal. Menu items and cooks can be added either with a pulldown option (for prepopulated cooks and recipes) or with text entry. Users can also view cook information and a formatted display of entered recipes.

In the future, we'd like to add password-protected user profiles, emailing a mealplan's customized URL to a planner, the ability to import recipes from other sites with compatible APIs, the ability to adjust ingredient amounts for group size, shopping list generation, and recipe sheets. 

## Program Structure and Build process Summary

As mentioned above, the application is hosted on Heroku, and can be accessed by going to https://meal-planner-app1.herokuapp.com/

For a more detailed explanation of the application build process, see docs/build.txt

For directory structure of the repository, see docs/directory_structure.txt

For information on how the different parts of the progran work together, see docs/program_structure.txt
