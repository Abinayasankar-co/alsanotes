import Navbar from './navbar'
import About from './About';
import Carousel from './Carousel';
import Contact from './contact';
import Footer from './Footer';


const Home = () =>{

    return(
        <>
          <Navbar />
    <Carousel />
    <About />
    <Contact />
    <Footer />
        </>
    );


}

export default Home;