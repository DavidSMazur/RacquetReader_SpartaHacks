import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
//import logo from './logo.png'; // Replace './logo.png' with the path to your logo image file
import 'bootstrap/dist/css/bootstrap.min.css';

function NavigationBar() {
    return (
        <Navbar bg="dark" variant = "dark" expand="lg" sticky="top">
      <Container>
        <Navbar.Brand href="/"> <span>RaquetReader</span></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/Video">Try It!</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    );
}

export default NavigationBar;
