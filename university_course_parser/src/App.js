import React from 'react';
import logo from './logo.svg';
import './App.css';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from 'react';

function App() {
  const [textOutput, setTextOutput] = useState(["This is a test"]);
  const handleSubmit = (event) => {
    const input = document.getElementById("input-field").value;
    const options = {
      method: "GET",
      headers: {
        input: input
      }
    }

    console.log("hello");

    fetch("http://127.0.0.1:5000/process_query", options)
      .then((response) => response.json())
      .then((data) => {
          console.log(data);
          setTextOutput(data.output);
      })

  }
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <div>
        <p>{textOutput}</p>
      </div>
      <TextField id="input-field" label="Input" variant="outlined" style={{ marginBottom: '20px' }} />
      <Button variant="contained" color="primary" onClick={handleSubmit}>
        Submit
      </Button>
    </div>
  );
}

export default App;
