# Author:  Michael Savino

# Exercise 03
# Citibike comparison program

# This program will intake a file with city bike data and analyze it

# The program is written by looping into each file and counting different things

from datetime import datetime 

casualCount = 0
memberCount = 0

electricCount = 0
classicCount = 0

startStations = {}
endStations = {}

totalTrips = 0
avgTripDurations = 0

longestTripDuration = 0  
 
print() 
print("2024 Citibike Data")
print() 
with open("202401-citibike-tripdata.csv","r") as f:
    next(f)
    
    for line in f:
        data = line.split(",")
        member_type = data[12].strip()
        rideable_type = data[1].strip()
        start_station = data[4].strip()
        end_station = data[6].strip()
        started_at = data[2].strip()
        ended_at = data[3].strip()
        
        if member_type == "casual":
            casualCount += 1
        elif member_type == "member":
            memberCount += 1
            
        if rideable_type == "electric_bike":
            electricCount += 1
        elif rideable_type == "classic_bike":
            classicCount += 1
            
        if start_station:
            if start_station in startStations:
                startStations[start_station] += 1
            else:
                startStations[start_station] = 1
                
        if end_station:
            if end_station in endStations:
                endStations[end_station] += 1
            else:
                endStations[end_station] = 1
                
        hours_start = int(started_at[0:2])
        min_start = int(started_at[3:5])
        sec_start = round(float(started_at[6:]),0)
        
        hours_end = int(ended_at[0:2])
        min_end = int(ended_at[3:5])
        sec_end = round(float(ended_at[6:]),0)

        total_seconds_start = hours_start * 3600 + min_start * 60 + sec_start
        total_seconds_end = hours_end * 3600 + min_end * 60 + sec_end
        
        duration_seconds = total_seconds_end - total_seconds_start
        
        avgTripDurations += duration_seconds
        totalTrips += 1
        
        if duration_seconds > longestTripDuration:
            longestTripDuration = duration_seconds
        
    percentCasual = casualCount/(casualCount+memberCount)*100
    percentElectric = electricCount/(classicCount+electricCount)*100
    
    print(f"There are {casualCount} occasional users, {memberCount} have a subscription. Occasional users are {percentCasual:.2f}% of the total.")
    print(f"Electric bikes have been used {electricCount} times, while classic bikes have been used {classicCount} times. Electric bikes are {percentElectric:.2f}% of the total.")
    
    mostCommonStartStation = None
    mostCommonStartCount = 0
    for station, count in startStations.items():
        if count > mostCommonStartCount:
            mostCommonStartStation = station
            mostCommonStartCount = count
            
    mostCommonEndStation = None 
    mostCommonEndCount = 0
    for station, count in endStations.items():
        if count > mostCommonEndCount:
            mostCommonEndStation = station
            mostCommonEndCount = count
    
    print(f"The most popular start station is '{mostCommonStartStation}' with {mostCommonStartCount} rides")
    print(f"The most popular end station is '{mostCommonEndStation}' with {mostCommonEndCount} rides")
    
    avgTripDurations = avgTripDurations / totalTrips / 60
    longestTripDuration = longestTripDuration / 60  # Convert to minutes
    
    print(f"The average trip duration is {avgTripDurations:.2f} minutes")
    print(f"The longest trip was {longestTripDuration:.2f} minutes")
    print()

#-------------------------------------------------------------------------------------------------------------
print() 
print("2025 Citibike Data")
print() 
with open("202501-citibike-tripdata.csv","r") as f:
    next(f)
    
    for line in f:
        data = line.split(",")
        member_type = data[12].strip()
        rideable_type = data[1].strip()
        start_station = data[4].strip()
        end_station = data[6].strip()
        started_at = data[2].strip()
        ended_at = data[3].strip()
        
        if member_type == "casual":
            casualCount += 1
        elif member_type == "member":
            memberCount += 1
            
        if rideable_type == "electric_bike":
            electricCount += 1
        elif rideable_type == "classic_bike":
            classicCount += 1
            
        if start_station:
            if start_station in startStations:
                startStations[start_station] += 1
            else:
                startStations[start_station] = 1
                
        if end_station:
            if end_station in endStations:
                endStations[end_station] += 1
            else:
                endStations[end_station] = 1
                
                
        time_format = "%Y-%m-%d %H:%M:%S.%f"
        start_dt = datetime.strptime(started_at, time_format)
        end_dt = datetime.strptime(ended_at, time_format)
        
        duration = (end_dt - start_dt).total_seconds()
        
        avgTripDurations += duration
        totalTrips += 1
        
        if duration_seconds > longestTripDuration:
            longestTripDuration = duration_seconds
        
    percentCasual = casualCount/(casualCount+memberCount)*100
    percentElectric = electricCount/(classicCount+electricCount)*100
    
    print(f"There are {casualCount} occasional users, {memberCount} have a subscription. Occasional users are {percentCasual:.2f}% of the total.")
    print(f"Electric bikes have been used {electricCount} times, while classic bikes have been used {classicCount} times. Electric bikes are {percentElectric:.2f}% of the total.")
    
    mostCommonStartStation = None
    mostCommonStartCount = 0
    for station, count in startStations.items():
        if count > mostCommonStartCount:
            mostCommonStartStation = station
            mostCommonStartCount = count
            
    mostCommonEndStation = None 
    mostCommonEndCount = 0
    for station, count in endStations.items():
        if count > mostCommonEndCount:
            mostCommonEndStation = station
            mostCommonEndCount = count
    
    print(f"The most popular start station is '{mostCommonStartStation}' with {mostCommonStartCount} rides")
    print(f"The most popular end station is '{mostCommonEndStation}' with {mostCommonEndCount} rides")
    
    avgTripDurations = avgTripDurations / totalTrips / 60
    longestTripDuration = longestTripDuration / 60  # Convert to minutes
    
    print(f"The average trip duration is {avgTripDurations:.2f} minutes")
    print(f"The longest trip was {longestTripDuration:.2f} minutes")
    print()
