import React, { useState, useEffect } from 'react';
import { Menu, Home, Info, ChevronDown, MapPin, Mail, Phone, LogIn, UserPlus } from 'lucide-react';


const colors = {
  primary: '#1a1a1a',    // Rich black
  secondary: '#f5f5f5',  // Off white
  accent: '#0047AB',     // Deep blue
  gold: '#FFD700',       // Premium gold
  grey: '#808080',       // Professional grey
};

const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('jwt');
    setIsAuthenticated(!!token);
  }, []);

  return isAuthenticated;
};

const Navbar = ({ onMenuClick }) => {
  const isAuthenticated = useAuth();
  const [currentPage, setCurrentPage] = useState('home');
  
  return (
    <nav className="flex items-center justify-between p-4 bg-gray-900 text-white">
      <div className="flex items-center gap-4">
        <Menu className="cursor-pointer hover:text-yellow-400" size={24} onClick={onMenuClick} />
        <img src="/api/placeholder/40/40" alt="Logo" className="w-10 h-10" />
      </div>
      
      <div className="flex items-center gap-6">
        <Home 
          className={`cursor-pointer ${currentPage === 'home' ? 'text-yellow-400' : 'hover:text-yellow-400'}`} 
          size={20} 
          onClick={() => setCurrentPage('home')}
        />
        <span 
          className={`cursor-pointer ${currentPage === 'about' ? 'text-yellow-400' : 'hover:text-yellow-400'}`}
          onClick={() => setCurrentPage('about')}
        >
          About
        </span>
        
        <div className="relative group">
          <div className="flex items-center gap-1 cursor-pointer hover:text-yellow-400">
            Services
            <ChevronDown size={16} />
          </div>
          <div className="absolute hidden group-hover:block w-48 bg-gray-800 p-2 rounded-md">
            <div className="py-1 px-2 hover:bg-gray-700 cursor-pointer">Service 1</div>
            <div className="py-1 px-2 hover:bg-gray-700 cursor-pointer">Service 2</div>
          </div>
        </div>
        
        <div className="flex items-center gap-4">
          {!isAuthenticated ? (
            <>
              <button className="px-4 py-2 rounded bg-blue-600 hover:bg-blue-700">
                <LogIn className="inline mr-2" size={16} />
                Login
              </button>
              <button className="px-4 py-2 rounded bg-yellow-500 hover:bg-yellow-600">
                <UserPlus className="inline mr-2" size={16} />
                Sign Up
              </button>
            </>
          ) : (
            <button className="px-4 py-2 rounded bg-green-600 hover:bg-green-700">
              Dashboard
            </button>
          )}
        </div>
      </div>
    </nav>
  );
};

// Sidebar Component
const Sidebar = ({ isOpen }) => {
  const menuItems = ['Language', 'Quiz', 'PPT Formation', 'Keyword Extraction'];
  
  return (
    <div className={`fixed left-0 top-0 h-full w-64 bg-gray-800 text-white transform ${isOpen ? 'translate-x-0' : '-translate-x-full'} transition-transform duration-300 ease-in-out`}>
      <div className="p-4">
        {menuItems.map((item, index) => (
          <div key={index} className="py-2 px-4 hover:bg-gray-700 cursor-pointer rounded">
            {item}
          </div>
        ))}
      </div>
    </div>
  );
};

// Carousel Component
const Carousel = () => {
  const [current, setCurrent] = useState(0);
  const images = [
    '/api/placeholder/800/400',
    '/api/placeholder/800/400',
    '/api/placeholder/800/400',
    '/api/placeholder/800/400'
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % images.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="relative w-full h-96 overflow-hidden">
      {images.map((src, index) => (
        <div
          key={index}
          className={`absolute w-full h-full transition-opacity duration-500 ${
            index === current ? 'opacity-100' : 'opacity-0'
          }`}
        >
          <img src={src} alt={`Slide ${index + 1}`} className="w-full h-full object-cover" />
        </div>
      ))}
    </div>
  );
};

// Content Section Component
const ContentSection = () => {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <div>
          <img src="/api/placeholder/500/300" alt="Feature" className="rounded-lg shadow-lg" />
        </div>
        <div>
          <h2 className="text-3xl font-bold mb-4">Transform Your Business</h2>
          <p className="text-gray-600 mb-6">
            Experience innovative solutions designed to elevate your business to new heights.
            Our premium services combine cutting-edge technology with expert insights.
          </p>
          <button className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            Learn More
          </button>
        </div>
      </div>
    </div>
  );
};

// Footer Component
const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-12">
      <div className="container mx-auto px-4 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div>
          <h3 className="text-2xl font-bold mb-4">Company Info</h3>
          <div className="space-y-4">
            <div className="flex items-center gap-2">
              <MapPin size={20} />
              <span>123 Business Avenue, Tech City</span>
            </div>
            <div className="flex items-center gap-2">
              <Mail size={20} />
              <span>contact@company.com</span>
            </div>
            <div className="flex items-center gap-2">
              <Phone size={20} />
              <span>+1 (555) 123-4567</span>
            </div>
          </div>
        </div>
        <div>
          <h3 className="text-2xl font-bold mb-4">Quick Links</h3>
          <div className="grid grid-cols-2 gap-4">
            <a href="#" className="hover:text-yellow-400">About Us</a>
            <a href="#" className="hover:text-yellow-400">Services</a>
            <a href="#" className="hover:text-yellow-400">Contact</a>
            <a href="#" className="hover:text-yellow-400">Privacy Policy</a>
          </div>
        </div>
      </div>
    </footer>
  );
};

// Main App Component
const App = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [currentView, setCurrentView] = useState('home');
  
  // Protected view check
  const isAuthenticated = useAuth();
  
  const renderView = () => {
    if (currentView === 'dashboard' && !isAuthenticated) {
      return <div className="text-center py-12">Please login to view dashboard</div>;
    }
    
    return (
      <>
        <Carousel />
        <ContentSection />
      </>
    );
  };
  
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar 
        onMenuClick={() => setSidebarOpen(!sidebarOpen)}
        onNavigate={setCurrentView}
      />
      <Sidebar isOpen={sidebarOpen} />
      <main className="pt-16">
        {renderView()}
      </main>
      <Footer />
    </div>
  );
};

export default App;