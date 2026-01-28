import os 

class CritterImage:
	def __init__(self , path , title ):
		self.path = path 
		self.title = title

CRITTERS = [
	

	
	 ]


critters_folder =  "./content/media/images/critters/"
for file in os.listdir(critters_folder):
	title = os.path.splitext(file)[0]
	ci = CritterImage(
		
		path = os.path.join(critters_folder , file) , 
		title = title
		)
	CRITTERS.append(ci)