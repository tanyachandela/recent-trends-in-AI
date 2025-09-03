async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.statusText);
        }

        const result = await response.json();
        document.getElementById('result').innerText = "Prediction: " + result.prediction;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('result').innerText = "⚠️ Something went wrong! Check if backend is running.";
    }
}

