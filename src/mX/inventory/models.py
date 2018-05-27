from django.db import models

# Parts (Parts Bookings model for Inventory App)
#  | - Alternates (Many to Many Field to itself)
#  | - Description
#  | - P/N
#  | - S/N
#  | - B/N
#  | - Purchase Price
#  | - Sales Price
#  | - Location
#  | - Quantity (Automatically set as 1 if S/N is written)
#  | - 

# Consumables
#  | - Spec
#  | - Name
#  | - Batch Number
#  | - Quantity
#  | - Purchase Price
#  | - Sales Price 

# Parts Booking
#  | - Part (FK)
#  | - Task (FK)
