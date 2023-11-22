import { Link } from "react-router-dom";

function ErrorPage() {

return(
    <section className="flex items-center h-full p-16 text-gray-800">
        <div className="container flex flex-col items-center justify-center px-5 mx-auto my-8">
            <div className="max-w-md text-center">
                <h2 className="mb-8 font-extrabold text-9xl dark:text-gray-500">
                    <span className="sr-only">Error</span>404
                </h2>
                <p className="text-2xl font-semibold md:text-3xl">Sorry, we couldn't find this page.</p>
                <Link rel="noopener noreferrer" className="px-8 py-3 font-semibold rounded" to="/">Back to the home page.</Link>
            </div>
        </div>
    </section>
    );
}
export default ErrorPage;