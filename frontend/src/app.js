import React, { useState } from 'react';
import Editor from './editor';

function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [selectedBlock, setSelectedBlock] = useState(null);
  const [newText, setNewText] = useState('');
  const [userConfirmation, setUserConfirmation] = useState(false);

  const handleFileChange = (e) => {
    setPdfFile(e.target.files[0]);
  };

  const handleBlockSelect = (block) => {
    setSelectedBlock(block);
  };

  const handleReplaceText = () => {
    if (userConfirmation && newText.length <= selectedBlock.text.length * 1.2) {
      // Call backend to replace text
      console.log('Replacing text:', newText);
    } else {
      alert('Text length exceeds 120% or user confirmation is required.');
    }
  };

  return (
    <div className="App">
      <input type="file" onChange={handleFileChange} />
      {pdfFile && (
        <Editor
          pdfFile={pdfFile}
          onBlockSelect={handleBlockSelect}
          selectedBlock={selectedBlock}
          newText={newText}
          onNewTextChange={setNewText}
          onUserConfirmation={setUserConfirmation}
          onReplaceText={handleReplaceText}
        />
      )}
    </div>
  );
}
