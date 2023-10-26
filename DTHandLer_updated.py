#1)     
# Detect if timestamp is string datatime or Python datatime
# Then, they all will be converted to Python datetime
# Format: MM-DD-YYYY / MM-DD-YYYY HH:MM:SS (excluded timezone)
       
from datetime import datetime,timedelta
class DTHandLer:
    #constructor, hàm khởi tạo
    def __init__(self,date,second):
        self.date = date
        self.second = second 

    def convert_datetime(self):
        try :
            time = datetime.strptime(self.date,"%d-%m-%Y")
            time.strftime('%d-%m-%Y %H:%M:%S')
            timestamp = datetime.timestamp(time)
            convertPyDatetime = datetime.fromtimestamp(int(timestamp))
            formatMDY = convertPyDatetime.strftime("%m-%d-%Y")
            formatMDYS = convertPyDatetime.strftime("%m-%d-%Y, %H:%M:%S")
            return formatMDY, formatMDYS
        except:
            print("error converting!!!") 
        
#2
# monthNum_to_monthName is used for converting month number to month name, example: 12-01-2022 -> 12-Jan-2022
    def monthNum_to_monthName(self):
        monthNum_to_monthName = datetime.strptime(self.date,"%d-%m-%Y").strftime("%d-%b-%Y")
        return monthNum_to_monthName

# compare_date is used for calculate any string datetime with current time and return day number
    def compare_date(self) :
        convert = datetime.strptime(self.date, '%d-%m-%Y')
        currentTime = datetime.now()
        compare_date = currentTime - convert
        return abs(compare_date.days)
    
# conversion is used to convert from second to a time series
#example: 600s -> 0h 10m 0s
    def conversion(self):
        conversion = str(timedelta(seconds= self.second))
        x = conversion.split(':')
        return x[0] + ' h ' + x[1] + ' m ' + x[2] + ' s'
#string_to_SQLServer is used to convert string datetime into SQL server datetime
    def string_to_SQLServer(self):
        stringtoSQLServer = datetime.strptime(self.date, '%d-%m-%Y').strftime('%Y-%m-%d')
        return stringtoSQLServer
# next_week_day is used to find next week day from a datetime input
# example: next_week_day of 12.2.2023 is 13.2.2023
    def next_week_day(self):
        convert_date = datetime.strptime(self.date, '%d-%m-%Y')

        next_weekday = convert_date - timedelta(days= convert_date.weekday() -7)
        return next_weekday.date()
# 7) 
# Create a list/container to store the timestamps input from user with these function
class List_Timestamps():
    #hàm khởi tạo
    def __init__(self, timestamps):
        self.timstamps = timestamps
        self.listTimestamp = []
    # a) print all timestamps
    def print_listTimestamps(self):
        print(self.listTimestamp) 
    # b) append new timestamp
    def append_timestamps(self):
        List_Timestamps.append()
        return self.listTimestamp
    # c) delete the specific timestamp
    def delete_timestamp(self):
        deltime = input("enter timestamp you want to delete: ")
        try :
            self.listTimestamp.remove(deltime)
        except:
            print("timestamp not found in the listtimestamps")         
    # d) print out the youngest datetime  
    def print_youngest_datetime (self):
        for i in range(0 ,len(self.listTimestamp)):
            minDateTime = self.listTimestamp[0] # gán datetime min = datetime min của list
            min = datetime.now() - datetime.strptime(self.listTimestamp[0], '%d-%m-%Y') # gán min( số ngày tính từ 0 đến now ) để so sánh với min [i]
            if ((datetime.now() - datetime.strptime(self.listTimestamp[i], '%d-%m-%Y')) < min): # so sánh với min
                min = (datetime.now() - datetime.strptime(self.listTimestamp[i], '%d-%m-%Y')) # gán min (số ngày mới)
                minDateTime = self.listTimestamp[i] # gán giá trị datetime min mới       
        return minDateTime   
            
        

#Test task 1 - 6   
x = DTHandLer(date='3-12-2023',second= 250)

print("Format: MM-DD-YYYY / MM-DD-YYYY HH:MM:SS : ", DTHandLer.convert_datetime(x))
print("month number to month name: ",DTHandLer.monthNum_to_monthName(x))
print("calculate any string datetime with current time: ",DTHandLer.compare_date(x))
print("convert from second to a time series: ",DTHandLer.conversion(x))
print("convert string datetime into SQL server datetime: ",DTHandLer.string_to_SQLServer(x))
print("next week day from a datetime input: ",DTHandLer.next_week_day(x))

#test task 7 
list = List_Timestamps("")   
list.listTimestamp.append("08-03-2015")
list.listTimestamp.append("08-03-2012")
list.listTimestamp.append("08-03-2017")
list.listTimestamp.append("08-03-2018")
list.print_listTimestamps()
list.delete_timestamp()
print("listTimestamps after deletion:")
list.print_listTimestamps()
print("the youngest datetime: ",List_Timestamps.print_youngest_datetime(list))