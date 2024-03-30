class students:
    
    def __init__(self,name,physics,chemistry,maths):
        self.name=name
        self.physics= physics
        self.chemistry= chemistry
        self.maths= maths

s1=students("humayun",94,90,100)

s2=students("wajih",90,80,100)

s3=students("aemon",90,99,95)

marksofPhysics=s1.physics+s2.physics+s3.physics//3 
print(marksofPhysics)
marksofChemistry=s1.chemistry+s2.chemistry+s3.chemistry//3
print(marksofChemistry)
marksofMaths=s1.maths+s2.maths+s3.maths//3
print(marksofMaths)

averageofstudents=marksofPhysics+marksofChemistry+marksofMaths//3 


print(averageofstudents)