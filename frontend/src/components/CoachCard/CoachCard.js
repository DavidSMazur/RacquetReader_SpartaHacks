import React from 'react'
import Card from 'react-bootstrap/Card';

function CoachCard({ img, name, description }) {
  return (
    <Card style={{ width: '18rem' }} onClick={() => console.log("You clicked on", name)} >
      <Card.Img variant="top" src={img} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Card.Text style={{  }}>{description}</Card.Text>
      </Card.Body>
    </Card>
  )
}

export default CoachCard