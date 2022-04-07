from datetime import datetime, timedelta
import calendar
from invalid_date import InvalidDate

class DateHandler():
    def __init__(self):
         self.end_of_the_month = self.__get_end_of_the_month()
         self.has_start_date = False
         self.has_end_date = False

    def handle_range_dates(self, start_date, end_date, most_recent_date):
        start_date, end_date = self.validate_range_dates(start_date, end_date)

        if not self.has_start_date and not self.has_end_date:
            end_date = most_recent_date
            start_date = (end_date - timedelta(days=365)).replace(day=1)
        if not self.has_start_date:
            start_date = (end_date - timedelta(days=365)).replace(day=1)
        if not self.has_end_date:
            end_date = (start_date + timedelta(days=365)).replace(day=1)
        
        return start_date, end_date


    def validate_range_dates(self,start_date, end_date):

        self.has_start_date = (start_date is not None) if type(start_date) is not str else (not start_date.isspace() and not not start_date) 
        self.has_end_date = (end_date is not None) if type(end_date) is not str else (not end_date.isspace() and not not end_date)
    

        start_date = datetime.strptime(start_date, '%d-%m-%Y').replace(day=1) if self.has_start_date else datetime(1900, 1, 1)
        end_date = datetime.strptime(end_date, '%d-%m-%Y').replace(day=1) if self.has_end_date else datetime(2100, 1, 1)

        if  start_date > end_date :
            raise InvalidDate(message='Start date later than end date', name='InvalidDatesRange')
            
        return start_date, end_date


    def __get_end_of_the_month(self):
        today = datetime.now()
        day = (calendar.monthrange(today.year, today.month))[1]
        return today.replace(day=day)
