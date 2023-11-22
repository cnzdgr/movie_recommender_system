function RecommendationList({recommendations}){
    const renderedRecommendations = recommendations.map((recommendation) =>{
        return(
            <div>
                <h2>{recommendation[0]}</h2>
            </div>
        )
    });
    return(
        <div>
            {renderedRecommendations}
        </div>
    )
}

export default RecommendationList;