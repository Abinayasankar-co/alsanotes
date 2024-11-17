

const Footer = () => (
    <footer className="bg-gray-800 text-gray-300 p-8">
        <div className="container mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
                <h3 className="text-xl font-bold mb-4">Contact Information</h3>
                <p>1234 Street Name, City, State, 12345</p>
                <p>Email: info@mywebsite.com</p>
                <p>Phone: (123) 456-7890</p>
            </div>
            <div>
                <h3 className="text-xl font-bold mb-4">Our Location</h3>
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.835434509374!2d144.9537353153167!3d-37.81627977975195!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf577d9f0b1b0b1b1!2sFederation%20Square!5e0!3m2!1sen!2sau!4v1611811572000!5m2!1sen!2sau"
                    width="100%"
                    height="200"
                    style={{ border: 0 }}
                    allowfullscreen=""
                    aria-hidden="false"
                    tabIndex="0"
                ></iframe>
            </div>
        </div>
        <div className="text-center mt-8">
            <p>&copy; 2024 MAARS.All rights reserved.</p>
        </div>
    </footer>
);

export default Footer