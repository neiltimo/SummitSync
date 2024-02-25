document.getElementById('upload-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var formData = new FormData();
  formData.append('meeting-file', document.getElementById('meeting-file').files[0]);

  fetch('/upload', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      console.log('Success:', data);
  })
  .catch((error) => {
      console.error('Error:', error);
  });
});

// Example function to fetch and display summaries
function fetchSummaries() {
  fetch('/summaries')
  .then(response => response.json())
  .then(data => {
      const list = document.getElementById('summary-list');
      list.innerHTML = ''; // Clear current list
      data.forEach(summary => {
          const listItem = document.createElement('li');
          listItem.textContent = summary; // Assuming 'summary' is a string. Adjust based on actual data structure.
          list.appendChild(listItem);
      });
  })
  .catch((error) => {
      console.error('Error:', error);
  });
}

// Call fetchSummaries to load summaries on page load
fetchSummaries();

document.getElementById('copyBtn').addEventListener('click', function() {
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = function(e) {
            const text = e.target.result;
            // Use the Clipboard API to copy the text
            navigator.clipboard.writeText(text).then(function() {
                console.log('Copying to clipboard was successful!');
            }, function(err) {
                console.error('Could not copy text: ', err);
            });
        };
        reader.readAsText(file);
    } else {
        console.log('No file selected');
    }
});

