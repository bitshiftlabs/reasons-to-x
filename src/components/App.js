import React, { useState } from "react";
import Header from "./Header";
import MainCard from "./MainCard";
import OtherOptions from "./OtherOptions";
import Reasons from "../reasons_list";
import Box from '@material-ui/core/Box';
import SearchBar from "./SearchBar";

function App() {
  const [value,setValue]=useState(null)
  let randomItem=Reasons[(Math.floor(Math.random() *Reasons.length))];
  return (
    <Box>
      <Header />
      <SearchBar Reasons={Reasons} prompt={randomItem.id} value={value} onChange={val => setValue(val)&&MainCard(val)}/>
      <MainCard item={value===null?randomItem:value}
      />
      {Reasons.map((e) => (
        <OtherOptions key={e.key} id={e.id} />
      ))}
    </Box>
  );
}
export default App;
