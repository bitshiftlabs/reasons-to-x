import React from "react";
import {Button,Typography,Box} from "@material-ui/core";

function OtherOptions(props) {
  return (
    <Box className="other-options">
      <Typography variant="h4">{props.id}</Typography>
      <Button variant="contained" >
      +
      </Button>
    </Box>
  );
}

export default OtherOptions;
