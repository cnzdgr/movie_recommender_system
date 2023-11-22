import TextField from '@mui/material/TextField';
import { AutoComplete } from "antd";
import {movieArray} from '../data/MovieArray';

function Dropdown({ value, onChange }) {
    
    const handleSelectionClick = (event, selectedValue) => {
        if (selectedValue === null) {
            onChange("")
        }else{
            onChange(selectedValue.label)
        }
    }

    return(
        <div>
            <AutoComplete 
            placeholder="Select Movie"
            options={movieArray}
            style={{ width: 320 }}
            onChange={handleSelectionClick}
            filterOption={true}
            />
        </div>
    )
};

export default Dropdown;