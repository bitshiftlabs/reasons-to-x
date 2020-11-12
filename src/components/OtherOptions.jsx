import React from "react";
import Button from "@material-ui/core/Button";

function OtherOptions(props) {
  return (
    <div className="other-options">
      <h4> {props.id}</h4>
      <Button variant="contained" color="primary">
      +
      </Button>
    </div>
  );
}

export default OtherOptions;
