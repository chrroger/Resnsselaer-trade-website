import psycopg2
import psycopg2.extras
import database_ as db
#Database class unit test

#Test the constructor of the database, and the connection
def testConstructor():
   ##create the database and check the validation
   if (db.create() and db.connect()):
      return 1
   else:
      return 0
   
#Test getItem() function that gets certain item name by giving certain item id
def testGetItem():
      ##create the database
      db.create()
      db.conect()
      ##the item id =0 has name 'test item 1'
      assert db.getItem(0)=="test item 1"
      assert db.getItem(1)=="test item 2"
      
#Test getPrice() function that gets certain item price by giving certain item id
def testGetPrice():
      ##create the database
      db.create()
      db.conect()
      ##the item id =0 has price 10
      assert db.getPrice(0)== 10
      assert db.getPrice(1)== 100

#Test getDate() function that gets certain item post date by giving certain item id
def testGetDate():
      ##create the database
      db.create()
      db.conect()
      ##the item id =0 has post date '12/01/20'
      assert db.getDate(0)== '12/01/20'
      assert db.getDate(1)== '12/02/20'


#Test search() function that searches item id date by giving certain comments
def testSearch():
   ##create the database
   db.create()
   db.conect()
   ##create a list to store the returned id list by search()
   tmp=[]
   tmp = db.search('toy')
   for i in tmp:
      ##here we have three items satisfy the search
      assert i in ['24, 26,27']

#Test add() function that adds item to the database
def testAdd():
   ##create the database
   db.create()
   db.conect()
   ## we create an item with the following attributes
   tmp = Item.Item(5,'pokeball', 20, '10/02/20')
   assert db.add(tmp)
   ## we create another item with some attributes missing, the add() still works
   tmp2 = Item.Item(5,'pokeball')
   assert db.add(tmp2)
   ## we create another item with all attributes missing, the add() will not work
   tmp3 = Item.Item()
   assert not db.add(tmp3)   

#Test romove() function that removes item from the database
def testRemove():
   ##create the database
   db.create()
   db.conect()
   ## test the database cannot search the removed item
   tmp = Item.Item(5,'pokeball', 20, '10/02/20')
   assert not db.search(db.remove(tmp))

