def visualize_segmentation(mail_filename, path, segmented_filename):
	## @parameter mail_filename : Path to the mail on wich we try the algorithm.
	## @parameter path : The sequence of 0 and 1 that the Viterbi algorithm returns.
	## @parameter visualized_mail_filename : The path on which we write the mail with the v
    ## return: True if the header corresponds to the
	visu = open(segmented_filename, 'w') 
	if(mail_filename.endswith(".dat")):
		mail_filename = mail_filename[:-4] + ".txt" 
	mail = open(mail_filename, 'r')
	mail_content = mail.read()
	visu.write(mail_content[:path.sum()])
	visu.write("------CUT------")
	visu.write(mail_content[path.sum():])
	visu.close()
	mail.close()
	return 0