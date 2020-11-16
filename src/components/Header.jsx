import React from 'react';
import Box from '@material-ui/core/Box';

const Header = () => (
  <Box className="header">
    <img src={process.env.PUBLIC_URL+"/images/download.png"} alt="logo" />
  </Box>
)
export default Header;
