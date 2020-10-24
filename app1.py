print("Sleep advice")
print()
while True:
  hrsleep=input("How many hours do you sleep a day?")
  
  if hrsleep> =8:
  	print("keep it up")
    print("It seems like you sleep sufficiently.However do remember to not get addicted to phones as they can affect your sleep.")
  
  else:
  	description = input("What is the reason why you sleep so less?")

 	 list_of_words = description.split()

  		feelings_list = []
  		encouragement_list = []
  		counter = 0
  
  	for each_word in list_of_words:
    
    	if each_word == "play"":
      		feelings_list.append("play")
      		encouragement_list.append("Save the playing for later")
      		counter += 2
    	if each_word == "study":
      		feelings_list.append("study")
      		encouragement_list.append("Good job for being so hardworking! But sleep is more important")
      		counter += 1
	if each_word == "read":
      		feelings_list.append("study")
      		encouragement_list.append("Reading is great,but do not get to addicted to it! Perhaps you could read it during other parts of the day?")
      		counter += 1
   	if each_word == "worry":
      		feelings_list.append("worry")
      		encouragement_list.append("What are you worried about? Maybe you can tell someone about it?")
      		counter += 1
      
    	if counter == 0:

      		output = "Sorry I don't really understand. Please use different words?"

 	  elif counter == 1:
    
      	output = "It seems that you like to " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "sleep is important :)"  

  	else:

        feelings = ""    
    	for i in range(len(feelings_list)-1):
      		feelings += feelings_list[i] + ", "
    		feelings += "and " + feelings_list[-1]
    
      		encouragement = ""    
    		for j in range(len(encouragement_list)-1):
            encouragement += encouragement_list[i] + ", "
    		encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are quite into " + feelings + ". Please always remember sleep is important and that"+ encouragement + "! Hope you will take this into account. :)"

  print()
  print(output)
  print()
