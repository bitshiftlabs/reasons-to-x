import React,{useState} from "react";
import {Button, Typography, Box} from "@material-ui/core";

function MainCard(props) {
  const [reason,setReason]=useState(<img src={props.randomItem.img} alt="loading..." />);
  function showReason(){
    setReason((props.randomItem.list)[Math.floor(Math.random() *(props.randomItem.list).length)]);
  }
  return (
    <Box align="center" className="main-card">
      <Typography align="center" variant="h1">{props.randomItem.id.toUpperCase()}</Typography>
      <Box className="reason-block">{reason}</Box>
      <Button className="button" onClick={showReason}>Find a Reason!</Button>
    </Box>
  );
}
export default MainCard;
