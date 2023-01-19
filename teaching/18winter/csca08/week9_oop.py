class Event():
    def __init__(self, title, start_time):
        ''' (Event, str, int) -> NoneType
        Initialize a new Event that starts at start_time and is named title.
        0 <= start_time < 24
        '''
        self._title = title
        self._start_time = start_time

    def __str__(self):
        ''' (Event) -> str
        Return a string representation of this Event.
        '''
        return "Event " + self._title + " starting at " + str(self._start_time)

    def __lt__(self, other):
        ''' (Event, Event) -> bool
        Return True if the Event self starts earlier than other,
        otherwise return False.
        '''
        return self._start_time < other._start_time

    def __eq__(self, other):
        ''' (Event, Event) -> bool
        Return True if the Event self starts at the same time as other,
        otherwise return False.
        '''
        return self._start_time == other._start_time


class Day():
    def __init__(self, day, month, year):
        ''' (Day, int, int, int) -> NoneType
        Initialize this calendar day.
        REQ: 1 <= day <= 31
        REQ: 1 <= month <= 12
        '''
        self._day = day
        self._month = month
        self._year = year
        self._events = []

    def __str__(self):
        ''' (Day) -> str
        Return a string representation of this day.
        '''
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)

    def schedule(self, event):
        ''' (Day, Event) -> NoneType
        Schedule event for this day.
        '''
        self._events.append(event)

    def get_events(self):
        ''' (Day) -> list of Event
        Return a list of Events of this Day.
        '''
        return self._events


if __name__ == '__main__':
    event1 = Event("CSCA08", 10)
    event2 = Event("MATA31", 12)
    event3 = Event("CSCA67", 9)
    print(event1)
    print(event2)
    print(event3)

    my_day = Day(9, 11, 2016)
    print(my_day)
    my_day.schedule(event1)
    my_day.schedule(event2)
    my_day.schedule(event3)

    print(event1 < event2)
    print(event1 == event2)
    print(event1 > event2)
    print(event1 != event2)

    my_events = sorted(my_day.get_events())
    for next_event in my_events:
        print(next_event)
