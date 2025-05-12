import React from "react";
import "./RV_card.css";

const RV_card = (props) => {
    return (
        <div className="RV_Card" id={props.id}>
            <img src={props.image} alt={props.RV_name} />
            <h2>{props.RV_name}</h2>
            <p>{props.RV_Description}</p>
        </div>
    );
};

export default RV_card;
