import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import Home from "./pages/Home/Home";
import NLP from "./pages/NLP/NLP";
import Video from "./pages/Video/Video";
import NavigationBar from "./components/NavigationBar/NavigationBar";


function App() {
  return (
    <Router>
      <div className="app-container">
        <NavigationBar />
        <Routes>
          <Route path = "/" element = {<Home />} />
          <Route path = "/nlp" element = {<NLP />} />
          <Route path = "/video" element = {<Video />} />
        </Routes>      
      </div>
    </Router>
  );
}

export default App;
