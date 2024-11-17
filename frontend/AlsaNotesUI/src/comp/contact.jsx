import { useRef} from "react";
import { useOnScreen } from "./CustomFunction";

const Contact = () => {
    const ref = useRef();
    const isVisible = useOnScreen(ref);

    return (
        <section ref={ref} className={`container mx-auto my-10 p-4 min-h-screen flex items-center justify-center fade-in ${isVisible ? 'visible' : ''}`}>
            <div className="w-full max-w-lg">
                <h2 className="text-3xl font-bold mb-4 text-yellow-500 text-center">Contact Us</h2>
                <form className="space-y-4">
                    <div>
                        <label className="block text-lg font-medium ">Name</label>
                        <input type="text" className="w-full p-2 border border-gray-700 rounded bg-gray-200 text-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-500" />
                    </div>
                    <div>
                        <label className="block text-lg font-medium">Email</label>
                        <input type="email" className="w-full p-2 border border-gray-700 rounded bg-gray-200 text-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-500" />
                    </div>
                    <div>
                        <label className="block text-lg font-medium">Message</label>
                        <textarea className="w-full p-2 border border-gray-700 rounded bg-gray-200 text-gray-300 focus:outline-none focus:ring-2 focus:ring-yellow-500"></textarea>
                    </div>
                    <button type="submit" className="w-full bg-yellow-500 text-gray-900 px-4 py-2 rounded hover:bg-yellow-600 transition-colors duration-300">Submit</button>
                </form>
            </div>
        </section>
    );
};

export default Contact