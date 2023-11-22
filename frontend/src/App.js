
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import ErrorPage from './pages/ErrorPage';


function App() {
  return (
    <div className="flex flex-col h-screen justify-between">
    <BrowserRouter >
    <Navbar/>
      <div className="mb-auto" >
        <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path='*' element={<ErrorPage />}/>
        </Routes>
      </div>
      <Footer/>
      </BrowserRouter>
      </div>
  );
}

export default App;