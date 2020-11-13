import React,{useState} from "react";
import Button from "@material-ui/core/Button";

function MainCard(props) {
  const [reason,setReason]=useState(<img src={props.randomItem.img} alt="img" />);
  function showReason(){
    setReason((props.randomItem.list)[Math.floor(Math.random() *(props.randomItem.list).length)]);
  }
  return (
    <div className="main-card">
      <h1>{props.randomItem.id.toUpperCase()}</h1>
      <div className="reason-block">{reason}</div>
      <Button className="button" onClick={showReason}>Find a Reason!</Button>
    </div>
  );
}
export default MainCard;
