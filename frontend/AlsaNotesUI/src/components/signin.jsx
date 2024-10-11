import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Assuming react-router-dom is used for navigation

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
      const response = await fetch('https://your-backend-api-url.com/endpoint', {
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
    <div className="interactive-page">
      <h2>Submit Your Data</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="input">Enter something:</label>
          <input
            type="text"
            id="input"
            value={inputData}
            onChange={(e) => setInputData(e.target.value)}
            className="form-control"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
};

export default InteractivePage;
