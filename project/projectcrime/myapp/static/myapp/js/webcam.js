// Get a reference to the canvas element and its context
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

// Get a reference to the capture button
const captureBtn = document.getElementById('capture-btn');

// Add a click event listener to the capture button
captureBtn.addEventListener('click', () => {
  // Draw the current video frame onto the canvas
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert the canvas image to a data URL
  const dataURL = canvas.toDataURL();

  // Send the data URL to the server using an AJAX request
  $.ajax({
    url: '/save-image/',
    type: 'POST',
    data: { image: dataURL },
    success: function(response) {
      alert('Image saved successfully');
    },
    error: function(xhr, status, error) {
      alert('An error occurred while saving the image');
    }
  });
});
