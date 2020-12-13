import User_ as user
from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#User class unit test

#Test the default constructor of the user
def testDefConstructor():
   ##create the user and check the validation
   if (user.User()):
      return 1
   else:
      return 0
   
#Test the constructor of the user
def testConstructor():
   ##create the user and check the validation
   if (user.User(1,'Mingzhen',[],[],[])):
      return 1
   else:
      return 0
   ##create the user and check the validation if time info is not completed
   if (user.User(2,'Mingzhen')):
      return 1
   else:
      return 0   
   
#Test getuser() function that edits the user name
def testGetuser():
      ##create the user
      x = user.user()
      ## check if it is valid to change the user name
      assert x.user.getuser('HaiRong')


#Test addSellHistory() function that adds attribute to an existing user
def testAddSellHistory():
   ##create the user
   x = user.user()
   ## we create a sell history list with the sold item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is added to the user class
   assert user.addSellHistory(tmp)  
   
#Test addBuyHistory() function that adds attribute to an existing user
def testAddBuyHistory():
   ##create the user
   x = user.user()
   ## we create a sell history list with the bought item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is added to the user class
   assert user.addBuyHistory(tmp)  

#Test addFavouriteList() function that adds attribute to an existing user
def testAddFavouriteList():
   ##create the user
   x = user.user()
   ## we create a sell history list with the favourated item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is added to the user class
   assert user.addFavouriteList(tmp) 


#Test removeSellHistory() function that removes attribute to an existing user
def testremoveSellHistory():
   ##create the user
   x = user.user()
   ## we create a sell history list with the sold item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is removeed to the user class
   assert user.removeSellHistory(tmp)  
   
#Test removeBuyHistory() function that removes attribute to an existing user
def testremoveBuyHistory():
   ##create the user
   x = user.user()
   ## we create a sell history list with the bought item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is removeed to the user class
   assert user.removeBuyHistory(tmp)  

#Test removeFavouriteList() function that removes attribute to an existing user
def testremoveFavouriteList():
   ##create the user
   x = user.user()
   ## we create a sell history list with the favourated item id
   tmp = []
   tmp.append(3)
   tmp.append(5)
   tmp.append(7)
   ##check if it is removeed to the user class
   assert user.removeFavouriteList(tmp) 