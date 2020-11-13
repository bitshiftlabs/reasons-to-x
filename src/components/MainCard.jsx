import React,{useState} from "react";
import Button from "@material-ui/core/Button";
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

function MainCard(props) {
  const [reason,setReason]=useState(<img src={props.randomItem.img} alt="img" />);
  function showReason(){
    setReason((props.randomItem.list)[Math.floor(Math.random() *(props.randomItem.list).length)]);
  }
  return (
    <Box className="main-card">
      <Typography><h1>{props.randomItem.id.toUpperCase()}</h1></Typography>
      <Box className="reason-block">{reason}</Box>
      <Button className="button" onClick={showReason}>Find a Reason!</Button>
    </Box>
  );
}
export default MainCard;
