SELECT departureAirport, MONTH(departureDateTime) as MonthDeparture, COUNT(ticket.id) as AmountTickets
FROM flight JOIN flightschedule ON flight.id=fs_flight_id JOIN ticket ON flightschedule.id=ticket.flight_id
 WHERE YEAR(departureDateTime)=2020
     GROUP BY departureAirport, MONTH(departureDateTime)
