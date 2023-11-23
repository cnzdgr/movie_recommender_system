function RecommendationList({recommendations}){
    const renderedRecommendations = recommendations.map((recommendation) =>{
        return(
            <div class="flex my-1 hover:bg-blue-lightest rounded divide-y divide-dashed">
            <div class=" text-center py-1">
              <p class="text-3xl p-0 text-grey-dark">&bull;</p>
            </div>
            <div class="w-4/5 py-3 px-1">
              <p class="hover:text-blue-dark">{recommendation[0]}</p>
            </div>
            <div class="w-1/5 text-right p-3">
              <p class="text-sm text-grey-dark">{((1-recommendation[1])*100).toFixed(1)}%</p>
            </div>
          </div>
        )
    });
    return(
        <div class="w-full max-w-screen-xl mx-auto ">
            <div class="border-b border-grey-light  bg-grey-lighter pt-3">
                <div class="bg-white max-w-sm shadow-lg rounded-lg overflow-hidden">
                    <div class="sm:flex sm:items-center pl-4 pr-4">
                        <div class="flex-grow">
                            <h3 class="font-normal pl-2 py-2 pt-4 leading-tight">Recommendations (acc. to vote similarity %):</h3>
                            <div class="w-full">
                                {renderedRecommendations}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default RecommendationList;