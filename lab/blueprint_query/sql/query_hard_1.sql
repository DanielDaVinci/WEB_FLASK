SELECT departureAirport, arrivalAirport, COUNT(*) as AmountTickets, SUM(price) as SumPrice
 FROM (SELECT departureAirport, arrivalAirport, flight.id as fl_id, price from flight JOIN flightschedule ON flight.id=fs_flight_id JOIN ticket ON flightschedule.id=ticket.flight_id
 WHERE YEAR(saleDate)=2020 AND MONTH(saleDate)=3) z
     GROUP BY fl_id
