import React from 'react';
import logo from './logo.svg';
import './App.css';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import { useState } from 'react';
import { MuiFileInput } from 'mui-file-input'
import { Stack } from '@mui/material';

function App() {
  const [textOutput, setTextOutput] = useState(["This is a test"]);
  const [file, setFile] = useState(null);
  const [fileUploaded, setFileUploaded] = useState(false);

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

  const handleFileUpload = (event) => {
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/upload_pdf', {
            method: 'POST',
            body: formData
    })
    setFileUploaded(!fileUploaded);
  }
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
      <div>
        <p>{textOutput}</p>
      </div>
      <Stack spacing={2} direction='row'>

        
        {fileUploaded === false && (<MuiFileInput inputProps={{ accept: '.pdf' }} value={file} onChange={ (newValue) => setFile(newValue)}/>)}
        {fileUploaded === false && ((<Button variant="contained" color="primary" onClick={handleFileUpload}>Submit</Button>))}

        {fileUploaded === true && (<TextField id="input-field" label="Input" variant="outlined" style={{ marginBottom: '20px' }} />)}
        {fileUploaded === true && ((<Button variant="contained" color="primary" onClick={handleSubmit}>Submit</Button>))}
      </Stack>
    </div>
  );
}

export default App;
