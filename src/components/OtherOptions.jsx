import React from "react";
import Button from "@material-ui/core/Button";
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';

function OtherOptions(props) {
  return (
    <Box className="other-options">
      <Typography>{props.id}</Typography>
      <Button variant="contained" color="primary">
      +
      </Button>
    </Box>
  );
}

export default OtherOptions;
