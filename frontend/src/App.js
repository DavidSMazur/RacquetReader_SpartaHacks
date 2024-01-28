import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import Home from "./pages/Home/Home";
import Video from "./pages/Video/Video";


function App() {
  return (
    <Router>
      <div className="app-container">
        <Routes>
          <Route path = "/" element = {<Home />} />
          <Route path = "/video" element = {<Video />} />
        </Routes>      
      </div>
    </Router>
  );
}

export default App;