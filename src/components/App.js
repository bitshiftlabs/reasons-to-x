import React from "react";
import Header from "./Header";
import MainCard from "./MainCard";
import OtherOptions from "./OtherOptions";
import Reasons from "../reasons_list";
import Box from '@material-ui/core/Box';

function App() {
  return (
    <Box>
      <Header />
      <MainCard randomItem={Reasons[Math.floor(Math.random() * Reasons.length)]} />
      {Reasons.map((e) => (
        <OtherOptions key={e.key} id={e.id} />
      ))}
    </Box>
  );
}
export default App;
