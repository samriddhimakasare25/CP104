"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Samriddhi Makasare
ID:      169065096
Email:   maka5096@mylaurier.ca
__updated__ = "2023-09-25"
-------------------------------------------------------
"""
# Imports

# Constants

foundationLength = float(input("Foundation length (m) : "))
foundationWidth = float(input("Foundation width (m) :"))
foundationHeight = float(input("Foundation height (m) :"))
wallHeight= float(input("Wall height (m): "))
costConcrete = float(input("Cost of concrete ($/m^3):"))
costBricks= float(input("Cost of bricks ($/m^2): "))

volumeFoundation =foundationLength * foundationWidth * foundationHeight
totalCostConcrete =costConcrete * volumeFoundation
wallArea=2*(wallHeight*foundationWidth+wallHeight*foundationLength)
totalCostBricks = wallArea*costBricks 
totalCost = totalCostConcrete+totalCostBricks 

print (f"Concrete needed for foundation (m^3):{volumeFoundation:.2f}")
print(f"Cost of concrete : ${totalCostConcrete:,.2f}")
print(f"Bricks needed for walls (m^2):{wallArea:.2f}")
print(f"Cost of bricks : ${totalCostBricks:,.2f}")
print(f"Total cost: ${totalCost:,.2f}")
