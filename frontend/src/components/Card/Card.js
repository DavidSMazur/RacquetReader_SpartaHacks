import React from 'react';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
<<<<<<< HEAD
import tennis from '../../images/djo.jpg';
import Butt from '../../components/Butt/Butt';

function Cardy() {
  return (
    <Row className="justify-content-center align-items-center" style={{ minHeight: '70vh', paddingTop: "150px" }}>
      <Col md={4}>
        <Card style={{ width: '100%', background: "#222222", color:"white" }}>
=======
import tennis from '../../images/tennis.jpg';

function Cardy() {
  return (
    <Row className="d-flex justify-content-center align-items-center">
      <Col md={4}>
        <Card style={{ width: '100%' }}>
          <Card.Img variant="top" src={tennis} style={{ width: '100%', height: 'auto', minHeight: '100vh' }} />
        </Card>
      </Col>
      <Col md={8}>
        <Card style={{ width: '100%' }}>
>>>>>>> f98ff0f686434268c74fc14fb3b831d744b67abb
          <Card.Body>
            <Card.Text>
              Combining computer vision and natural language processing, our machine learning tennis coach can do it all!
              Our MLCoach tracks the movements of a player, providing a visual representation of the overall performance of the player.
              Feeding natural language into a connected langchain agent, the MLcoach will be able to answer any questions about tennis through RAG,
              mimicking well-known coaches, and can deliver verbal feedback on the player's swings.
            </Card.Text>
<<<<<<< HEAD
            <Butt />
          </Card.Body>
        </Card>
      </Col>
      <Col md={4}>
        <Card style={{ width: '100%' }}>
          <Card.Img variant="top" src={tennis} style={{ width: '122%', height: 'auto' }} />
        </Card>
      </Col>
=======
          </Card.Body>
        </Card>
      </Col>
>>>>>>> f98ff0f686434268c74fc14fb3b831d744b67abb
    </Row>
  );
}

<<<<<<< HEAD
export default Cardy;
=======
export default Cardy;
>>>>>>> f98ff0f686434268c74fc14fb3b831d744b67abb
