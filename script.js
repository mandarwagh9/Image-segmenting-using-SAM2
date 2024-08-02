document.getElementById('uploadBtn').addEventListener('click', async () => {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Please select an image file.');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.combined_mask) {
            document.getElementById('combinedMask').src = result.combined_mask;
        }
        
        const individualMasksContainer = document.getElementById('individualMasks');
        individualMasksContainer.innerHTML = '';
        
        result.individual_masks.forEach(maskUrl => {
            const img = document.createElement('img');
            img.src = maskUrl;
            img.alt = 'Individual Mask';
            individualMasksContainer.appendChild(img);
        });
    } catch (error) {
        console.error('Error:', error);
    }
});
