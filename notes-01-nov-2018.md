# 01-nov-2018

### 1 - Django tutorial

- https://docs.djangoproject.com/en/2.1/intro/tutorial01  
- Key Points
  - You write your classes, containing fields with defined types
  - Django converts them to SQL tables and does the sync thing  ( by default it uses sqlite, but there is a MongoDB version out there too)
  - views are written in a template language with DSL embeeded for if and for loops ( quite similar to Meteor in this )
  - Admin panel is provided beforehand
  - There was no client side discussion in tutorial. I am assuming to provide rich interface, JS needs to get invovled. May be some different frontend framework than it's using by default.
  - There was no dynamic reactivity in the tutorial. Request stuff- Response stuff: server side rendering.
  - Good for quick development of simple Apps
- Files(default)
  - urls.py: Contains the routing and stuff, multiple present in the project
  - from urls.py(not literally) it goes to views.py which contains views which refer to templates
  - while rendering template or doing other stuff, models.py models are updated,queried
  - manage.py is control center during development, can be used to runserver and get shell directly into application and running tests
