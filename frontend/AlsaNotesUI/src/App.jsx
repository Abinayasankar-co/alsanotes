import {Route,Routes} from 'react-router-dom';
import Login from './comp/Login';
import Home from './comp/home';
import '../src/index.css'

const App = () => {
  return (
    <div>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path="/login" element={<Login/>}/>
    </Routes>
   </div>
  );
}

export default App;