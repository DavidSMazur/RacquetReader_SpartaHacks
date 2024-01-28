import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

function CoachCard({ img, name }) {
  const handleSelect = () => {
    // Send the name variable in the API call
    // CALL API HERE!!!
    
    console.log("Selected coach:", name);
  };

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={img} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Button variant="primary" onClick={handleSelect}>Select</Button>
      </Card.Body>
    </Card>
  );
}

export default CoachCard;
