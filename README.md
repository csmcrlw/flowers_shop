# flowers_shop
Flowers shop with text-to-speech function
# Installation
To use the project you should create & activate virtual environment first

For Windows:
```
python -m venv venv
venv\Scripts\activate
```

For MacOS & Linux:
```
python3 -m venv venv
source venv/bin/activate
```

Then, install requirements.txt:
```
pip install -r requirements.txt
```
# Migrations
To create a database for your project, run these commands:
```
python manage.py makemigrations
python manage.py migrate
```
# Let's run it!
To run the project, use this command:
```
python manage.py runserver
```
# REST API

**For all users:**
| pattern                    | type                |                                                           description |
| -------------------------- |:-------------------:| ---------------------------------------------------------------------:|
| /products/products/        |             GET     |                                              shows a list of products |
| /products/categories/      |               GET   |                                            shows a list of caregories |
| /products/products/{id}/   |        GET          |                                    detail information about a product |
| /products/categories/{id}/ |        GET          |                                   detail information about a category |
| /cart/cart/                |        POST         |                                                         create a cart |
| /cart/user/login/          |        POST         |                                                               sign in |
| /cart/user/register/       |        POST         |                                                               sign up |

**For admins & cart owners:**
| pattern                    | type                |                                                           description |
| -------------------------- |:-------------------:| ---------------------------------------------------------------------:|
| /cart/cart/                |             GET     |                                            shows a cart list to admin |
| /cart/cart/{id}/           |               GET   |                                            shows a cart to owner user |
| /cart/cart/{id}/           | POST, PATCH         |                                                          edits a cart |
| /cart/cart/{id}/           |        DELETE       |                                                        deletes a cart |
| /cart/cart/{id}/index/     |        GET          |                                                    **text-to-speech** |

**For admins only:**
| pattern                    | type                |                                                           description |
| -------------------------- |:-------------------:| ---------------------------------------------------------------------:|
| /products/products/        |            POST     |                                                     creates a product |
| /products/categories/      |              POST   |                                                    creates a category |
| /products/products/{id}/   | PUT, PATCH          |                                                       edits a product |
| /products/categories/{id}/ |  PUT, PATCH         |                                                      edits a category |
| /products/products/{id}/   | PUT, PATCH          |                                                       edits a product |
| /products/categories/{id}/ |  PUT, PATCH         |                                                      edits a category |
| /products/products/{id}/   | DELETE              |                                                     deletes a product |
| /products/categories/{id}/ |  DELETE             |                                                    deletes a category |
