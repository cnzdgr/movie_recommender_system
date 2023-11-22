import React, { useState, useEffect } from "react";
import Dropdown from "../components/Dropdown";
import RecommendationList from "../components/RecommendationList";
import HeroImg from '../images/logo.png' 
import axios from 'axios';

const apiEndPoint = "https://caring-legs-production.up.railway.app/predict"

function HomePage() {
    const [movie, setMovie] = useState("");
    const [recommendations, setRecommendations] = useState([])


    const handleSubmit = ((e) => {
        console.log("handle submit is working now")
        e.preventDefault();
        axios.post(apiEndPoint,     {
            "inputs": [
              {
                Movie: movie
              }
            ]
          })
          .then((response) => {
            setRecommendations(response.data.predictions)
          })
    })
    console.log(recommendations)
    
    return(
        <section className="bg-white">
            <div className="grid max-w-screen-xl px-8 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-10 lg:grid-cols-12 xl:px-11">
                <div className="mr-auto lg:col-span-7">
                <Dropdown value={movie} onChange= {(e) => {setMovie(e.target.value)}}/>
                
                <div>
              <button
                type="submit"
                onClick={handleSubmit}
                className="inline-block px-12 py-3 text-sm font-medium text-sky-700 border border-sky-700 rounded hover:bg-sky-700 hover:text-white active:bg-indigo-500 focus:outline-none focus:ring">
                Give me recommendations
              </button>
            </div>
            <RecommendationList recommendations={recommendations}/>

                    <div className="grid grid-cols-2 sm:grid-cols-3 xl:grid-cols-4">
                    </div>


                </div>
                <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
                    <img src={HeroImg} alt="mockup"/>
                </div>                
            </div>
        </section>
    )
}
export default HomePage;