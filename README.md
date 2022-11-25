# Coding-Assignment

### REST-API Coding Test<br><br>

## Running the project locally
#### 1) First clone the repo to local computer
```
git clone https://github.com/irfaniskandar-23/Coding-Assignment.git
```

#### 2) Install requirements
```
 pip install -r requirements.txt
```

#### 3) Create database
```
python manage.py migrate
```

#### 4) Add template directory in project setting template section
```
'DIRS': [os.path.join(BASE_DIR, 'template')]
```

#### 5) Admin
```
python manage.py createsuperuser
```

#### 6) Run development server
```
python manage.py runserver
```

#### 7) urls
> Django REST API Root : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)<br>
> Inventory List (frontend) : [http://127.0.0.1:8000/inventory/](  http://127.0.0.1:8000/inventory/)<br>
> Inventory Detail (frontend) : [http://127.0.0.1:8000/inventory/1](http://127.0.0.1:8000/inventory/1)<br>
> Inventory List (Backend/API)  : [http://127.0.0.1:8000/api/inventory/](http://127.0.0.1:8000/api/inventory/)<br>
> Inventory Detail (Backend/API)  : [http://127.0.0.1:8000/api/inventory/1](http://127.0.0.1:8000/api/inventory/1)<br>


#### 8) Output <br>

##### 1) Inventory List (Frontend)
<img
  src="/output/Inventory_List (FrontendI).png"
  alt="Alt text"
  title="InventoryList (Frontend)"
  style="display: inline-block; margin: 0 auto; width: 100px height: 50px" >
  
  
  
##### 2) Inventory Detail (Frontend)
<img
  src="/output/Inventory_Detail (Frontend).png"
  alt="Alt text"
  title="InventoryList (Frontend)"
  style="display: inline-block; margin: 0 auto; width: 100px height: 50px" >

