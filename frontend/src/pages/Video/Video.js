import React, { useState } from 'react';
import NavigationBar from '../../components/NavigationBar/NavigationBar';
import Cursor from '../../components/Cursor/Cursor';
import { Button, Container, Row, Col, Image, Form } from 'react-bootstrap';
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import Ric from '../../images/coaches/richardwilliams.jpg';
import Nick from '../../images/coaches/nick.webp';
import Ivan from '../../images/coaches/ivan.webp';
import Goran from '../../images/coaches/nick.webp';
import Boris from '../../images/coaches/boris.webp';

function Video() {
    const [videoFile, setVideoFile] = useState(null);
    const [videoURL, setVideoURL] = useState(null);
    const [userInput, setUserInput] = useState(''); // State to hold user input
    const [response, setResponse] = useState(''); // State to hold response

    const coaches = [
        { key: 1, name: 'Richard Williams', img:Ric  },
        { key: 2, name: 'Goran Ivanisevic', img: Goran },
        { key: 3, name: 'Boris Becker', img: Boris },
        { key: 4, name: 'Nick Bollettieri', img: Nick },
        { key: 5, name: 'Ivan Lendl', img: Ivan },
    ];

    const handleFileChange = (event) => {
        setVideoFile(event.target.files[0]);
    }

    const handleUpload = async (event) => {
      event.preventDefault();

      if (videoFile) {
          const formData = new FormData();
          formData.append('video', videoFile);

          try {
              // Upload the video to backend
              const response = await fetch('http://your-backend-api-url/process_video', {
                  method: 'POST',
                  body: formData,
              });

              if (!response.ok) {
                  throw new Error('Failed to upload video');
              }

              // Assuming the backend API returns a video URL
              const processedVideoURL = await response.text();
              setVideoURL(processedVideoURL);

              // Download the video file
              const a = document.createElement('a');
              a.href = processedVideoURL;
              a.download = 'output_video.mp4';
              document.body.appendChild(a);
              a.click();
              document.body.removeChild(a);
          } catch (error) {
              console.error('Error:', error);
          }
      }
  };
  const handleUserInput = (event) => {
    setUserInput(event.target.value); // Update user input state
};

const handleSubmit = (event) => {
    event.preventDefault();
    // Send user input to backend API and set response state with the received response
    // For example:
    // fetch('http://your-backend-api-url/process_input', {
    //     method: 'POST',
    //     body: JSON.stringify({ input: userInput }),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // })
    // .then(response => response.text())
    // .then(data => setResponse(data))
    // .catch(error => console.error('Error:', error));
};


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
                            "speed": 1
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
          <h3 style={{ color:"#32CD32", paddingTop: "50px", paddingBottom: "50px" }}>Choose your Coach!</h3>
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

                    <input type="file" accept="video/*" onChange={handleFileChange} className="mb-2"/>
                    <Button variant="primary" onClick={handleUpload}>Submit</Button>
                  </Col>

                  <Col sm={12} className="d-flex flex-column align-items-center">
    <Form onSubmit={handleSubmit} style={{ width: '100%' }}>
        <Form.Group controlId="userInput">
            <Form.Label style={{ color:"white" }}>Talk to your Coach:</Form.Label>
            <Form.Control type="text" value={userInput} placeholder="How can I improve my serve?" onChange={handleUserInput} />
        </Form.Group>
        <Button variant="primary" type="submit">Submit</Button>
    </Form>
    <div>{response}</div> {/* Display response */}
</Col>
              </Row>
          </Container>
      </div>
    )
}

export default Video;