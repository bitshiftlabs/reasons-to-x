import React from "react";
import Button from "@material-ui/core/Button";

function MainCard(props) {
  return (
    <div className="main-card">
      <h1>{props.randomItem.id.toUpperCase()}</h1>
      <img src={props.randomItem.img} alt="img" />
      <Button className="button">Find a Reason!</Button>
    </div>
  );
}
export default MainCard;
