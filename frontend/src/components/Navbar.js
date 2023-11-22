import { Link } from "react-router-dom";


function Navbar () {

    return(
        <nav className="bg-gray-100 border-gray-300">
        <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
            <div className="relative flex h-14 items-center justify-between">
                <div className="absolute inset-y-0 left-0 flex items-center">

                </div>
                <div className="flex flex-1 items-center items-stretch justify-start pl-4 sm:pl-0">
                <Link to='/'>
                <h2 className="text-lg sm:text-xl font-serif">Movie Recommender Web App </h2>
                </Link>
                </div>
                <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                <Link
                    to='https://github.com/cnzdgr/movie_recommender_system'
                    type="button"
                    data-te-ripple-init
                    data-te-ripple-color="light"
                    class=" focus:ring-0 active:shadow-lg hover:shadow hover:-translate-y-0.5 ">
                    <svg
                    class="w-5 h-5 text-black-500 fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24">
                    <path
                        d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"
                    ></path>
                    </svg>
                </Link>
                </div>
            </div>
        </div>

        </nav>
    );   
}

export default Navbar;