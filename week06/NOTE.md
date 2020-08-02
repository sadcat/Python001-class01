- Django
  - a MVC web framework. prefer to use 2.2.13 LTS
  - organized by project and app.
    - project - app1 -> url: base_url/app1
    - project - app2 -> url: base_url/app2
  - create a project
    - ```django-admin startproject MyDjango```
    - create an app
      - ```python manage.py startapp index```
  - run development server
    - python manage.py runserver
    - python manage.py runserver 0.0.0.0:80
  - manage.py
    - ```python manage.py``` to show available commands.
- <project_folder>/settings.py
  - DEBUG=True
    - verbose log
    - single user
  - INSTALLED_APPS & MIDDLEWARE
    - sequence sensitive
      - load: top -> bottom
      - return: bottom -> top
  - Add your add to the bottom of INSTALLED_APPS
  - TEMPLATES:
    - BACKEND can change to jinja if needed
  - DATABASE
    - ENGINE: django.db.backends.mysql
  - database & models
    - settings.py -> DATABASE/ENGINE
    - create a model, e.g.
      ```
        from django.db import models
        
        class Movie(models.Model):
          title = models.CharField(max_length=256)
          created_at = models.DateTimeField()
          updated_at = models.DateTimeField()
      ```
    - create migration by model
      - ```python manage.py makemigrations```
    - migrate to db
      - ```python manage.py migrate```
    - inspect db
      - ```python manage.py inspectdb```
    - mysql trick
      - ```mysql> select * from t1 limit 2\G```
    - reverse migration
      - ```python manage.py migrate <app_name> zero```
  - route
    - https://docs.djangoproject.com/en/3.0/topics/http/urls/
    - top level: <project_folder>/urls.py
      ```
      from django.contrib import admin
      from django.urls import path, include
    
      urlpatterns = [
          path('admin/', admin.site.urls),
          # pattern: <app_name>.<url_module>
          # app: index
          # url_module: index/urls.py
          path('', include('index.urls'))
      ]
      ```   
    - app level: <project_folder>/<app_folder>/urls.py
      ```
      from django.urls import path, re_path
      from . import views
      urlpatterns = [
        # views = views.py
        # match <base_url>/index/ to views.index method
        path('', views.index),

        # match <base_url>/index/nnnn.html, n is 0-9 to views.year method
        # and assign (?P<year>[0-9]{4}) to variable
        re_path('(?P<year>[0-9]{4}).html', views.year, name='urlyear')

        # match <base_url>/index/any_int to views.year method
        path('<int:year>', views.year)
      ]
      ```
  - view
    - each method represents a controller method which is referred in urls.py
    - render a html template by ```return render(request, 'some.html')```
    - ```some.html``` is in <app_folder>/templates
    - ```render(request,'some.html', locals())'``` pass all local variable to template
    ```
    # views.py
    from django.shortcuts import render
    from django.http import HttpResponse
    
    # **kwargs is defined and assigned in route
    def year(request, **kwargs):
      return render(request, 'yearview.html')
    ```
  - render template and build-in template tags
    - raw http response
    ```
    return HttpResponse('string')
    ```
    - https://docs.djangoproject.com/en/2.2/ref/templates/builtins/
    - loop and use var
    ```html
    {% for book in n %}
    <div>bookname: {{ book.name }}   <br>
           author: {{ book.author }} <br>
           stars:  {{ book.stars }}  
    </div>
    {% endfor %}
    ```

- python module & package explained
  - module: a .py file
      - executable module
        ```python
        # module func
        def func():
          pass
        
        if __name__ == '__main__':
          func()
        ```
  - package: a dir containing many .py files
    - ```__init__.py```
  - refer to module
    - from MyPackage import Module1 as M1
    - from . import Module1
    - from .Pkg2 import M2

- register_converter(cls, 'name')
