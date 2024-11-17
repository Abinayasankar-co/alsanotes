import { useRef } from "react";
import { useOnScreen } from "./CustomFunction";

const About = () => {
    const ref = useRef();
    const isVisible = useOnScreen(ref);

    return (
        <section ref={ref} className={`container mx-auto my-10 p-4 min-h-screen flex items-center fade-in ${isVisible ? 'visible' : ''}`}>
            <div className="w-full md:w-1/2">
                <h2 className="text-3xl font-bold mb-4 text-center text-yellow-500">About Us</h2>
                <p className="text-lg mb-4">
                     ALSA NOTES 
                    We are the Subproduct of MAARS working on producing the mosr relevant LLM based approaches to leverate things that make easier for Customers to connect, share and make fun with their findings 
                    Why We! We provide a Automative analyzing of your referencial model on Reasearch papers There you can find your time working on analyzing more precised data to scale your knowledge

                </p>
            </div>
            <div className="w-full md:w-1/2">
                <img src="https://placehold.co/600x400?text=About+Us+Image" alt="About Us image" className="w-full h-auto transform hover:scale-105 transition-transform duration-300" />
            </div>
        </section>
    );
};

export default About;