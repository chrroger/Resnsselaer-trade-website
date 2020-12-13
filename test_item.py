import Item_ as item
from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#Item class unit test

#Test the default constructor of the item
def testDefConstructor():
   ##create the item and check the validation
   if (item.Item()):
      return 1
   else:
      return 0
   
#Test the constructor of the item
def testConstructor():
   ##create the item and check the validation
   if (item.Item(2,'item',30,'08/02/10')):
      return 1
   else:
      return 0
   ##create the item and check the validation if time info is not completed
   if (item.Item(2,'item')):
      return 1
   else:
      return 0   
   
#Test getItem() function that edits the item name
def testGetItem():
      ##create the item
      x = item.Item()
      ## check if it is valid to change the item name
      assert x.item.getItem('basketball')
      
#Test getPrice() function that edots the item price
def testGetPrice():
   ##create the item
   x = item.Item()
   ## check if it is valid to change the item price
   assert x.item.getPrice(20)

#Test getDate() function that edits the itme post date
def testGetDate():
   ##create the item
   x = item.Item()
   ## check if it is valid to change the item post date
   assert x.item.getDate('12/01/20')


#Test addAttribute() function that adds attribute to an existing item
def testAddAttribute():
   ##create the item
   x = item.Item()
   ## we create an attribute 
   tmp = 'is totally new'
   assert item.addAttribute(tmp)  

#Test romoveAttribute() function that removes attribute from an existing item
def testRemoveAttribute():
   ##create the item
   x = item.Item()
   ## test the item cannot search the removed attribute
   tmp = 'is totally new'
   assert item.remove(tmp)

