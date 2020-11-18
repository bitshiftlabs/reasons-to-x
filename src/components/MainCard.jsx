import React,{useState} from "react";
import {Button, Typography, Box,} from "@material-ui/core";

function MainCard(props) {
  const [reason,setReason]=useState("");
  function showReason(){
    setReason(props.item.list[(Math.floor(Math.random() *(props.item.list).length))]);
  }
  return (
      <Box align="center" className="main-card">
      <Typography align="center" variant="h1">{props.item.id.toUpperCase()}</Typography>
      <img src={props.item.img} alt="img" />
      <Box className="reason-block">{(props.item.list).includes(reason)===false?"Click here ↓":reason}</Box>
   <Button className="button" onClick={showReason}>Find a Reason!</Button>
  </Box>
  );
}
export default MainCard;