import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom'; // Assuming you're using react-router-dom for navigation
//import logo from './logo.png'; // Replace './logo.png' with the path to your logo image file
import 'bootstrap/dist/css/bootstrap.min.css';

function NavigationBar() {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" fixed="top"> {/* Fixed position */}
            <Container>
                <Navbar.Brand as={Link} to="/">Navbar</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="ml-auto">
                        <Nav.Link as={Link} to="/try-it">Try it</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavigationBar;
