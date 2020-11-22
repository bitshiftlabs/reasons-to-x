import React, { useState } from "react";
import Header from "./Header";
import MainCard from "./MainCard";
import Reasons from "../reasons_list";
import { Box, MuiThemeProvider } from "@material-ui/core";
import SearchBar from "./SearchBar";
import { theme } from "./Theme";

function App() {
  const [value, setValue] = useState(null);
  let randomItem = Reasons[Math.floor(Math.random() * Reasons.length)];
  return (
    <Box>
      <MuiThemeProvider theme={theme}>
        <Header />
        <SearchBar
          Reasons={Reasons}
          prompt={randomItem.id}
          value={value}
          onChange={(val) => setValue(val) && MainCard(val)}
        />
        <MainCard item={value === null ? randomItem : value} />
      </MuiThemeProvider>
    </Box>
  );
}
export default App;
