SELECT passportInfo, price FROM ticket JOIN flightschedule on ticket.flight_id = flightschedule.id
  WHERE flightschedule.fs_flight_id = 'SU2 2' AND YEAR(saleDate) = 2020 AND MONTH(saleDate) = 3
 AND price = (SELECT MAX(price) FROM ticket JOIN flightschedule on ticket.flight_id = flightschedule.id
  WHERE flightschedule.fs_flight_id = 'SU2 2' AND YEAR(saleDate) = 2020 AND MONTH(saleDate) = 3)
