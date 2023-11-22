import { Link } from "react-router-dom";

function Footer () {
    return(

        <footer className=" bg-gray-800 mt-3 xl:mt-7">
            <div className="w-full ml-3 mx-auto container md:p-6 p-4 md:flex md:items-center md:justify-between">
            <span 
                className="text-sm text-gray-300 sm:text-center mx-10">© 2023 <a href="/" className="hover:underline"> </a> All Rights Reserved.
            </span>
            <div className="flex flex-wrap items-center mt-3 text-sm text-gray-300 sm:mt-0 mx-10">
 

                    <p> Contact: ozdogar@yahoo.com </p>
            </div>
            </div>
        </footer>
    );
}

export default Footer;