import React, { useState, useEffect } from "react";
import "./App.css";
import SearchIcon from "./search.svg"

import MovieCard from "./MovieCard";

const API_URL = "http://www.omdbapi.com?apikey=a65eebdf";

const App = () => {

  const [movies, setMovies] = useState([]);
  const [seachTern, setSeactTerm] = useState("");

  const searchMovies = async (title) => {
    const response = await fetch(`${API_URL}&s=${title}`);
    const data = await response.json();

    setMovies(data.Search);
  };

  useEffect(() => {
    searchMovies("naruto");
  }, []);

  return (

    <div className="app">

      <h1>  JS_Entertainment   </h1>
      
      <div className="search">
        <input
          placeholder="Search for Movies"
          value={seachTern}
          onChange={(e) => setSeactTerm(e.target.value)}
        />
        

        <img
          src={SearchIcon}
          alt="Search"
          onClick={() => searchMovies(seachTern)}
        />
      </div>

      

      {
        movies?.length > 0
          ? (
            <div className="container">
              {
                movies.map((movie) => (
                  <MovieCard movie={movie} />
                ))
              }
            </div>
          ) :
          (
            <div>
              <h1>No Movies Found</h1>
            </div>
          )
      }

    </div>

  );
};

export default App;