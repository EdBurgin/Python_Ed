import os
location_Start = input("Bonjour! Warning: This will attempt to rename files with xy in the title. Please type in the number you wish the images titles to be renamed to. The program finds files with xy in the filename and renumbers the xy location starting from your input number. Currently set up for 3 channel sequences. (type here): ")

areYouSure = input("Are you sure you would like to preceed? (type here yes/no): ")

if (areYouSure == "yes"):
	ed = (os.getcwd())
	ed2 = os.path.split(ed)
	print("THE SPLIT OF THE FILE PATH IS: ", ed2[1])
	print ("The dir is: %s"%ed)


	for filename in os.listdir():
		if "xy" in filename:
			print(filename)
			name_parts = filename.split('xy')
			location = list(name_parts[1])
			location[0] = ""
			location_Start = str(location_Start)
			location[1] = location_Start
			location_Start = int(location_Start)
			name_channel = filename.split('c')
			# print("namechannel: ", name_channel)
			if(name_channel[1] == "3.tif"):
				location_Start += 1
				# print("before joinging: ",s)
			new_Name = "".join(location)
			final_name = name_parts[0] + "xy" + new_Name + "newfile"
			print("after joining: ", final_name)
			# newName = "150511 Matrix 4"+ ed2[1] + " meta " + filename
			# newName = "meta " + filename
			os.rename(filename, final_name)
			
			# print("RENAMED THE DAMN FILE FOR YOU")
		#print(len(filename))
		# if filename 
		# for i in filename:
			# print (i)
	for filename in os.listdir():
		if "newfile" in filename:
			name_parts = filename.split('newfile')
			final_name = name_parts[0]
			print("removing tags: ", final_name)
			os.rename(filename, final_name)
	end = input("press any key to exit. (here):")
else:
	print("cancelling rename of files ")
	end = input("press any key to exit! (here): )")
