// Import necessary modules from Next.js
import Head from 'next/head'
import Link from 'next/link';

function FlightsPage() {
  // Array containing flight data
  const flights = [
    { id: 1, number: 'DL123', destination: 'New York', origin: 'Atlanta', departureTime: '10:00 AM' },
    { id: 2, number: 'AA456', destination: 'Los Angeles', origin: 'Chicago', departureTime: '12:00 PM' },
    { id: 3, number: 'UA789', destination: 'San Francisco', origin: 'Houston', departureTime: '3:00 PM' },
    { id: 4, number: 'SW123', destination: 'Las Vegas', origin: 'Denver', departureTime: '5:00 PM' },
    { id: 5, number: 'FR456', destination: 'Miami', origin: 'Orlando', departureTime: '8:00 PM' }
  ];

  return (
    <div>
      <p>Update this to create a table showing the flight number, destination, origin, and departure time</p>
      <p>The flight number should contain a link navigating to flights/id where id is the id of the flight I.E. 1</p>
    </div>
  );
}

export default FlightsPage;