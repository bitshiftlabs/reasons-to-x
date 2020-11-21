import React, { useState } from "react";
import {
  Button,
  Typography,
  Card,
  createMuiTheme,
  responsiveFontSizes,
  CardMedia,
} from "@material-ui/core";

let theme = createMuiTheme();
theme = responsiveFontSizes(theme);

function MainCard(props) {
  const [reason, setReason] = useState("");
  function showReason() {
    setReason(
      props.item.list[Math.floor(Math.random() * props.item.list.length)]
    );
  }
  return (
    <Card align="center" className="main-card">
      <Typography theme={theme} align="center" variant="h1" gutterBottom>
        {props.item.id.toUpperCase()}
      </Typography>
      <CardMedia className="card-img">
        <img src={props.item.img} alt="img" />
      </CardMedia>
      <Typography
        theme={theme}
        variant="subtitle1"
        gutterBottom
        className="reason-block"
      >
        {props.item.list.includes(reason) === false ? "Click here ↓" : reason}
      </Typography>
      <Button className="button" onClick={showReason}>
        Find a Reason!
      </Button>
    </Card>
  );
}
export default MainCard;
