import { useState, useEffect } from 'react';
import { AutoComplete } from 'antd';
import {movieArray} from '../data/MovieArray';

function Dropdown(){
    console.log(movieArray)
    return(
        <div>
            <AutoComplete 
            style={{ width: 200}}
            placeholder="Type the movie that you liked..."
            options={movieArray.title}
            />
        </div>
    )
};

export default Dropdown;