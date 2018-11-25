import string

from datetime import datetime, timedelta
from dateutil.parser import parse

class Book():
    '''The Book class. '''
    
    def __init__(self, title, author, year, pages, start_date, end_date):
        '''Attributes of the Book class. 
            The year, start_date, and end_date attributes 
            have to be parsed as date objects. 
            Title and Author have to be capitalized. 
            Number of pages is actual length of content to be read, 
            counted from the beginning of the Prologue, up to the end 
            of the Epilogue. 
            More attributes may be added if needed. '''
        
        caps = string.capwords
        
        self.title = caps(title)
        self.author = caps(author)
        self.year = year
        self.pages = int(pages)
        self.start_date = start_date
        self.end_date = end_date
        
        
    def __repr__(self):
        '''String representation for each defined Book object. 
            Note that start_date and end_date are not included, 
            as they are not primarily for description or 
            identification purposes.'''
        
        return("{}, {}\n{}\n{} pages".format(
                self.title, self.author, self.year, self.pages))
    
    def sched(self):
        '''Start and end dates. These have to be parsed as date objects. 
            Some timedelta functionality, as well as elaborate 
            calculations of reading speed, will be included in the future.
            That's actually the whole point of defining these attributes.'''
        
        return("SCHEDULE: {} - {}".format(self.start_date, self.end_date))
    
    def duration(self):
        '''Reading duration.'''
        
        timefmt = '%b %d %Y'
        
        parsed_start_date = datetime.strptime(self.start_date, timefmt)
        parsed_end_date = datetime.strptime(self.end_date, timefmt)
        
        time_delta = parsed_end_date - parsed_start_date
        
        self.duration = int(time_delta.days)
        
        return("DURATION: {} days".format(self.duration))
    
    def speed(self):
        '''Reading speed. Number of pages divided by reading duration.'''
        
        self.speed = int(self.pages / self.duration)
        
        return("SPEED: {} PAGES/DAY".format(self.speed))
    
    def textfile(self, filename):
        '''Open, read, write, append text file/s. 
            The duration() and speed() methods have to be called first, so that 
            certain attributes are rendered properly in the text file.'''
        
        f = open(filename, 'a')
        
        Book.duration(self)
        Book.speed(self)
        
        f.write("{}\n{}\n{}\n{} pages\n\nSCHEDULE: {} - {}\nDURATION: {} days\nSPEED: {} pages/day\n\n".format(
                                    self.title, self.author, self.year, 
                                    self.pages, self.start_date, self.end_date, 
                                    self.duration, self.speed))
        f.write("-----*-----*-----\n\n")
            
        f.close()
        
if __name__ == '__main__':
    
    book1 = Book("Venice: A New History", 
                "Thomas Madden", 
                "2012", 
                "427", 
                "Oct 22 2017", 
                "Nov 8 2017")
    
    book2 = Book("Framing the Early Middle Ages", 
                "Christopher Wickham", 
                "2007", 
                "831", 
                "Nov 15 2017", 
                "Jan 2 2018")
    
    
    book1.textfile('books.txt')
    book2.textfile('books.txt')