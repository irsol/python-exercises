# CRUD Review

## Udacity small "restaurant-menu" project.

## Operations with SQLAlchemy on an SQLite database.

### To connect to restaurantMenu.db, and create a session to interface with the database:

`from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()`

	
### CREATE
#### Create a new Restaurant and called it Pizza Pasta:

`myFirstRestaurant = Restaurant(name = "Pizza Pasta")
session.add(myFirstRestaurant)
sesssion.commit()`

#### Create a cheese pizza menu item and added it to the Pizza Pasta Menu:

`cheesepizza = menuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()`

### READ
#### Read out information in our database using the query method in SQLAlchemy:

`firstResult = session.query(Restaurant).first()
firstResult.name
items = session.query(MenuItem).all()
for item in items:
    print item.name`

### UPDATE
#### In order to update and existing entry in database, execute the following commands:

* Find Entry
* Reset value(s)
* Add to session
* Execute session.commit()

#### Find the veggie burger that belonged to the Urban Burger restaurant by 
executing the following query:

`veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"`

#### Then update the price of the veggie burger to $2.99:

`UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()`

### DELETE
#### To delete an item from database, follow the following steps:

* Find the entry
* Session.delete(Entry)
* Session.commit()
#### Deleted spinach Ice Cream from  Menu Items database with the following operations:

`spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit()`   
