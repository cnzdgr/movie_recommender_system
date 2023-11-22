import { useState, useEffect } from 'react';
import { AutoComplete } from 'antd';
import {movieArray} from '../data/MovieArray';

function Dropdown({ value, onChange }) {
    const handleSelectionClick = (option) => {
        onChange(option);
    }

    const renderedOptions = movieArray.map((movie) => {
        return(
            <option
                className={movie.title === value ? "cursor-pointer shadow-md underline ml-1 grid grid-cols-8" : "cursor-pointer hover:underline ml-1 grid grid-cols-8"}

                onClick={() => handleSelectionClick(movie.title)}
                key={movie.title}>
                <h2 className="col-span-7"> {movie.title}  </h2>
                <p className="col-span-1"> </p>

            </option>
        );
    })
    return(
        <div>
            <select
            className="p-1 rounded-lg bg-gray-50 border border-gray shadow w-full lg:w-2/5 mb-4"
            placeholder=""
            onChange= {onChange}
            >
            {renderedOptions}
            </select>
            
        </div>
    )
    }
export default Dropdown;