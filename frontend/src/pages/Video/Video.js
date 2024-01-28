import React, { useState } from 'react';
import NavigationBar from '../../components/NavigationBar/NavigationBar';
import Cursor from '../../components/Cursor/Cursor';
import { Button, Container, Row, Col, Image } from 'react-bootstrap';
import Serena from '../../images/serena.jpg';
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";

function Video() {
    const [videoFile, setVideoFile] = useState(null);
    const [videoURL, setVideoURL] = useState(null);
    const coaches = [
        { key: 1, name: 'Serena Williams', img:Serena  },
        { key: 2, name: 'Jane Doe', img: 'img2.jpg' },
    ];

    const handleFileChange = (event) => {
        setVideoFile(event.target.files[0]);
    }

    const handleUpload = (event) => {
        event.preventDefault();

        if(videoFile) {
            setVideoURL(URL.createObjectURL(videoFile));
        }
    }

    const imageStyle = {
        width: "100px", 
        height: "100px",
        objectFit: "cover"
    }
    const particlesInit = async (main) => {
        await loadFull(main);
    };
    return (
      <div id="c">
          <NavigationBar />
          <Particles
                style={{
                    position: "fixed",
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    zIndex: 0
                }}
                id="tsparticles"
                init={particlesInit}
                options={{
                    "background": {
                        color: "#000000", // Background color in hexadecimal format
                    },
                    "particles": {
                        "number": {
                          "value": 80,
                          "density": {
                            "enable": true,
                            "value_area": 800
                          }
                        },
                        "color": {
                          "value": "#1000FF"
                        },
                        "shape": {
                          "type": "circle",
                          "stroke": {
                            "width": 0,
                            "color": "#000000"
                          },
                          "polygon": {
                            "nb_sides": 5
                          },
                          "image": {
                            "src": "img/github.svg",
                            "width": 100,
                            "height": 100
                          }
                        },
                        "opacity": {
                          "value": 0.5,
                          "random": false,
                          "anim": {
                            "enable": false,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                          }
                        },
                        "size": {
                          "value": 3,
                          "random": true,
                          "anim": {
                            "enable": false,
                            "speed": 40,
                            "size_min": 0.1,
                            "sync": false
                          }
                        },
                        "line_linked": {
                          "enable": true,
                          "distance": 150,
                          "color": "#ffffff",
                          "opacity": 0.4,
                          "width": 1
                        },
                        "move": {
                          "enable": true,
                          "speed": 4,
                          "direction": "none",
                          "random": false,
                          "straight": false,
                          "out_mode": "out",
                          "bounce": false,
                          "attract": {
                            "enable": false,
                            "rotateX": 600,
                            "rotateY": 1200
                          }
                        }
                      },
                      "interactivity": {
                        "detect_on": "canvas",
                        "events": {
                          "onhover": {
                            "enable": true,
                            "mode": "repulse"
                          },
                          "onclick": {
                            "enable": true,
                            "mode": "push"
                          },
                          "resize": true
                        },
                        "modes": {
                          "grab": {
                            "distance": 400,
                            "line_linked": {
                              "opacity": 1
                            }
                          },
                          "bubble": {
                            "distance": 400,
                            "size": 40,
                            "duration": 2,
                            "opacity": 8,
                            "speed": 3
                          },
                          "repulse": {
                            "distance": 200,
                            "duration": 0.4
                          },
                          "push": {
                            "particles_nb": 4
                          },
                          "remove": {
                            "particles_nb": 2
                          }
                        }
                      },
                      "retina_detect": true
                }}
            />
          <Cursor />

          <Container fluid style = {{ zIndex: 1, position: 'relative' }}>
              <Row className="mt-4">
                  <Col sm={1}>
                  {coaches.map((coach) => (
                      <div className="mb-4 d-flex flex-column align-items-start">
                          <Image src={coach.img} roundedCircle style={imageStyle} />
                          <h4 style={{ color: 'white' }}>{coach.name}</h4>
                      </div>
                  ))}
                  </Col>

                  <Col sm={9}>
                    {videoURL && 
                          <video width="100%" height="auto" autoPlay muted>
                              <source src={videoURL} type="video/mp4"/>
                          </video>
                    }
                  </Col>

                  <Col sm={2} className="d-flex flex-column align-items-center">
                    <Button variant="primary" className="mb-2">Record</Button>
                    <input type="file" accept="video/*" onChange={handleFileChange} className="mb-2"/>
                    <Button variant="primary" onClick={handleUpload}>Submit</Button>
                  </Col>
              </Row>
          </Container>
      </div>
    )
}

export default Video;