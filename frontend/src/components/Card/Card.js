import React from 'react';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import tennis from '../../images/djo.jpg';
import Butt from '../Butt/Butt';

function Cardy() {
  return (
    <Row className="justify-content-center align-items-center" style={{ minHeight: '70vh', paddingTop: '200px' }}>
      <Col md={4}>
        <Card style={{ width: '100%', backgroundColor: '#333', color: '#fff' }}>
          <Card.Body>
            <Card.Text>
              Combining computer vision and natural language processing, our machine learning tennis coach can do it all!
              Our MLCoach tracks the movements of a player, providing a visual representation of the overall performance of the player.
              Feeding natural language into a connected langchain agent, the MLcoach will be able to answer any questions about tennis through RAG,
              mimicking well-known coaches, and can deliver verbal feedback on the player's swings.
            </Card.Text>
            <Butt />
          </Card.Body>
        </Card>
      </Col>
      <Col md={4}>
        <Card style={{ width: '100%' }}>
          <Card.Img variant="top" src={tennis} style={{ width: '125%', height: 'auto' }} />
        </Card>
      </Col>
    </Row>
  );
}

export default Cardy;