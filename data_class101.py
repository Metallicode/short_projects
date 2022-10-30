#https://rszalski.github.io/magicmethods/

from collections import namedtuple
from csv import DictReader
import dataclasses
'''

print(f"namedtuple {'%'*50}")

#immutable
##Unpack Tuples

Point = namedtuple('Point_z', ['x', 'y', 'f'])



p1 = Point(x=1, y=2, f=print)



x, y, z = p1

print(x)
print(y)
print(z)


print(p1[0], p1[1])
print(p1.x, p1.y)
p1.f("namedtuple can have a function!")
print(dir(p1))
print(p1)
'''
















#################################################################
'''
print(f"normal {'%'*50}")


class InventoryItem_normal:
	def __init__(self, name: str, unit_price: float, items_in_stock:int=0):
		self.name = name
		self.unit_price = unit_price
		self.items_in_stock = items_in_stock

	def total_item_in_stock_cost(self) -> float:
		return self.unit_price * self.items_in_stock
		
		
	


@dataclasses.dataclass
class InventoryItem:
	name: str
	unit_price: float
	items_in_stock: int = 0

	def total_item_in_stock_cost(self) -> float:
 		return self.unit_price * self.items_in_stock


itemn = InventoryItem_normal("car", 5000, 3)

print(itemn)

print(dir(itemn))

itemn2 = InventoryItem_normal("car", 5000, 3)

print(itemn == itemn2)
print(itemn is itemn2)


print(f"dataclass {'%'*50}")

item = InventoryItem("car", 5000, 3)
item2 = InventoryItem("car", 5000, 3)

print(item)


print(dir(item))

print(item == item2)
print(item is item2)
'''



#################################################################

print(f"DictReader {'%'*50}")

with open('data.csv') as f:

	reader = DictReader(f, delimiter=',')
	print(dir(reader))
	rows = list(reader)
	print(type(rows[0]))	
	print(rows[0].keys())
	print(rows[0]["Data_value"])
	print(rows[0])



	


