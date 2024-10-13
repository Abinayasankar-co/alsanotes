import { useEffect, useState } from 'react';

function DisplayImage() {
    const [base64Image, setBase64Image] = useState('');

    useEffect(() => {
        // Create a WebSocket connection
        const socket = new WebSocket('ws://localhost:8000/ws/image/example_image');  // Adjust URL if necessary

        // Connection opened
        socket.onopen = () => {
            console.log("WebSocket connection established.");
        };

        // Receive the image data
        socket.onmessage = (event) => {
            const receivedData = event.data;
            
            // Check if the server sent an error message
            if (receivedData.startsWith("Error")) {
                console.error(receivedData);
            } else {
                // Set the received Base64 string as the image source
                setBase64Image(receivedData);
            }
        };

        // Handle errors
        socket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        // Connection closed
        socket.onclose = () => {
            console.log("WebSocket connection closed.");
        };

        // Clean up WebSocket connection when the component unmounts
        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            <h1>Image from MongoDB</h1>
            {base64Image ? (
                <img src={`data:image/jpeg;base64,${base64Image}`} alt="From MongoDB" />
            ) : (
                <p>Loading image...</p>
            )}
        </div>
    );
}

export default DisplayImage;
