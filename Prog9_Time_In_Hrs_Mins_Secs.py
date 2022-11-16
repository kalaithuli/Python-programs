# Time in hours, minutes and seconds
s = int(input("Enter the time in seconds "))
hrs = int(s/3600)
mins = int ((s % 3600)/60)
secs = int ((s % 3600) % 60)
print (hrs , "hours " , mins , "minutes " , secs , "seconds ")
