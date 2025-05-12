import React from "react";
import RV_card from "./Card/RV_card";
import "./RV_cards.css";
import reviews from "../../../../public/assets/people/Reviews/reviews.json";

const RV_cards = () => {
    return (
        <div className="RV_cards">
            {reviews.map((review) => (
                <RV_card 
                    key={review.id} 
                    id={review.id} 
                    RV_name={review.RV_name} 
                    RV_Description={review.RV_Description}
                    image={review.image} 
                />
            ))}
        </div>
    );
}

export default RV_cards;
