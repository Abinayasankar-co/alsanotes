import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button, Container, Row, Col, Image } from 'react-bootstrap';
// Assuming react-router-dom is used for navigation

const InteractivePage = () => {
  const [inputData, setInputData] = useState('');
  const navigate = useNavigate(); // Hook for navigation

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    // Prepare the data to send to the backend
    const data = {
      input: inputData,
    };

    try {
      
       // Make the POST request to the backend
       const response = await fetch('http://localhost:8000/v1/data_receiver', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), // Send the input data
      });

      const result = await response.json();

      // Display the backend response in an alert
      alert(`Response from server: ${result.message}`);

      // Check for the JWT token in localStorage
      const token = localStorage.getItem('jwtToken');
      if (token) {
        // Redirect to the homepage if the token is present
        navigate('/');
      } else {
        alert('JWT token not found, cannot redirect to homepage.');
      }
    } catch (error) {
      console.error('Error while making POST request:', error);
      alert('Something went wrong. Please try again.');
    }
  };

  return (
    <Container fluid className="vh-100 d-flex justify-content-center align-items-center bg-dark">
    <Col md={4} className="p-5 bg-secondary rounded">
        <div className="text-center mb-4">
            <Image src="logo.png" alt="Logo" fluid style={{ maxWidth: '80px' }} />
        </div>
        <h2 className="text-center text-white mb-4">Create an account</h2>
        <p className="text-center text-light">
            Already have an account? <a href="/login" className="text-info">Log in</a>
        </p>
        <Form>
            <Form.Group className="mb-3" controlId="firstName">
                <Form.Control type="text" placeholder="First name" />
            </Form.Group>
            <Form.Group className="mb-3" controlId="lastName">
                <Form.Control type="text" placeholder="Last name" />
            </Form.Group>
            <Form.Group className="mb-3" controlId="email">
                <Form.Control type="email" placeholder="Email" />
            </Form.Group>
            <Form.Group className="mb-3" controlId="password">
                <Form.Control type="password" placeholder="Enter your password" />
            </Form.Group>
            <Form.Group className="mb-3" controlId="terms">
                <Form.Check type="checkbox" label="I agree to the Terms & Conditions" />
            </Form.Group>
            <Button variant="primary" type="submit" className="w-100">
                Create account
            </Button>
        </Form>
        <div className="text-center mt-3 text-white">Or register with</div>
        <div className="d-flex justify-content-between mt-2">
            <Button variant="danger" className="w-45">Google</Button>
            <Button variant="dark" className="w-45">Apple</Button>
        </div>
    </Col>
    <a href="/" className="text-white mt-3 d-block text-center">Back to website</a>
</Container>
      );
};

export default InteractivePage;
