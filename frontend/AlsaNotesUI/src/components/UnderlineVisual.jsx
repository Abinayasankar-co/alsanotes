import { useState,useEffect } from "react";

const UnderlineVisual = () =>{
    const [highlightStrings, setHighlightStrings] = useState([]); // to store strings to highlight
    const [content, setContent] = useState('This is a sample content to highlight certain words.');

    useEffect(() => {
      fetch(' ') 
       .then((response) => response.json())
       .then((data) => {
         setHighlightStrings(data.strings); // Assuming your API returns { strings: ['word1', 'word2'] }
       })
       .catch((error) => {
         console.error('Error fetching data:', error);
       });
    },   []);

    const highlightText = (text, highlightValues) => {
       if (!highlightValues.length) return text; // if there are no values to highlight, return text as-is
    
       // Create a regular expression to match any of the highlight values
       const regex = new RegExp(`(${highlightValues.join('|')})`, 'gi');
    
       return text.split(regex).map((part, index) =>
            highlightValues.includes(part.toLowerCase()) ? (
                   <mark key={index}>{part}</mark> // wrap highlighted parts in <mark>
            ) : (
            <span key={index}>{part}</span>
        )
        );
    };

    return(
        <div>

        </div>
    );

}

export default UnderlineVisual;