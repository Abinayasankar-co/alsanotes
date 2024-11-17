import { useState } from "react";

const Carousel = () => {
            const [currentIndex, setCurrentIndex] = useState(0);
            const images = [
                "https://placehold.co/1920x1080?text=Image+1",
                "https://placehold.co/1920x1080?text=Image+2",
                "https://placehold.co/1920x1080?text=Image+3"
            ];

            const nextSlide = () => {
                setCurrentIndex((currentIndex + 1) % images.length);
            };

            const prevSlide = () => {
                setCurrentIndex((currentIndex - 1 + images.length) % images.length);
            };

            return (
                <div className="relative w-full h-screen mt-20">
                    <img src={images[currentIndex]} alt={`Carousel image ${currentIndex + 1}`} className="w-full h-full object-cover" />
                    <button onClick={prevSlide} className="absolute top-1/2 left-0 transform -translate-y-1/2 bg-gray-800 text-white p-2">
                        <i className="fas fa-chevron-left"></i>
                    </button>
                    <button onClick={nextSlide} className="absolute top-1/2 right-0 transform -translate-y-1/2 bg-gray-800 text-white p-2">
                        <i className="fas fa-chevron-right"></i>
                    </button>
                </div>
            );
        };



export default Carousel;