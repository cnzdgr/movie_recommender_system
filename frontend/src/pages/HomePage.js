import React, { useState } from "react";
import Dropdown from "../components/Dropdown";
import RecommendationList from "../components/RecommendationList";
import HeroImg from '../images/logo.png' 
import axios from 'axios';

const apiEndPoint = "https://caring-legs-production.up.railway.app/predict"

function HomePage() {
    const [movie, setMovie] = useState("");
    const [recommendations, setRecommendations] = useState([])
    const [isSent, setIsSent] = useState(false);

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
            setIsSent(true);
          })
    })
    
    return(
        <section className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div className="grid grid-cols-12 ml-3 sm:ml-0">
                <div className=" col-span-12 sm:col-span-5 lg:col-span-5 xl:col-span-5 ">
                    <h2 className="mt-3 mb-2">Select a Movie You Liked</h2>
                    <Dropdown value={movie} onChange= {(e) => {setMovie(e)}}/>
                    <div>
                        <button
                        type="submit"
                        onClick={handleSubmit}
                        className="inline-block w-80 mt-1 px-12 py-3 text-sm font-medium text-sky-700 border border-sky-700 rounded hover:bg-sky-700 hover:text-white active:bg-indigo-500 focus:outline-none focus:ring">
                        Give me recommendations
                        </button>
                        <img className="object-cover  h-48 w-58 mt-8 ml-5" src={HeroImg} alt="mockup"/>

                    </div>
                </div>
                <div class="col-span-12 lg:col-span-5 ">
                    {(!isSent) && <div className="mt-5 mr-6">
                            <p className="italic">A movie recommendation engine using collaborative filtering.</p>
                            <p className="italic">Currently it only contains popular movies that are released on or before July-2017. </p>
                            <p className="italic">Select a movie and click the button to see your movie recommendations. </p>
                    </div>}
                {isSent && <RecommendationList recommendations={recommendations.slice(1)}/>}
                </div>                
            </div>
        </section>
    )
}
export default HomePage;